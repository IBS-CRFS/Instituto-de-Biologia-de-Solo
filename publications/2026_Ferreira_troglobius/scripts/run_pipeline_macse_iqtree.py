import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    sys.exit(f"❌ {msg}")


def info(msg: str) -> None:
    print(f"[INFO] {msg}")


def ensure_executable(name: str) -> str:
    path = shutil.which(name)
    if path is None:
        fail(f"{name} não encontrado no PATH")
    return path


def ensure_file(path_str: str, label: str) -> Path:
    p = Path(path_str)
    if not p.exists():
        fail(f"{label} não encontrado: {p}")
    return p


def normalize_header(line: str, keep_terms: int) -> str:
    """Mantém até keep_terms termos do cabeçalho, unidos por '_'."""
    name = line[1:].strip()
    if not name:
        return line
    tokens = name.split()
    trimmed = "_".join(tokens[:keep_terms]) if tokens else ""
    return f">{trimmed}\n"


def concatenate_fastas(inputs: list[Path], output: Path, keep_terms: int) -> None:
    with open(output, "w") as fout:
        for p in inputs:
            if not p.exists():
                fail(f"Arquivo FASTA não encontrado: {p}")
            with open(p) as fin:
                for line in fin:
                    if line.startswith(">"):
                        fout.write(normalize_header(line, keep_terms))
                    else:
                        fout.write(line)


def run_macse(java_bin: str, macse_jar: Path, fasta_in: Path, prefix: Path, genetic_code: int) -> Path:
    out_nt = prefix.with_suffix(".macse.nt.fasta")
    out_aa = prefix.with_suffix(".macse.aa.fasta")
    log_path = prefix.with_suffix(".macse.log")

    cmd = [
        java_bin,
        "-jar",
        str(macse_jar),
        "-prog",
        "alignSequences",
        "-gc_def",
        str(genetic_code),
        "-seq",
        str(fasta_in),
        "-out_NT",
        str(out_nt),
        "-out_AA",
        str(out_aa),
    ]

    info("Executando MACSE (codon-aware)...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    log_path.write_text(res.stdout + "\n" + res.stderr)

    if res.returncode != 0:
        fail(f"MACSE retornou erro. Veja o log: {log_path}")

    if not out_nt.exists():
        fail(f"Saída nucleotídica não encontrada após MACSE: {out_nt}")

    info(f"Log MACSE: {log_path}")
    info(f"Alinhamento NT: {out_nt}")
    return out_nt


def clean_alignment(inp: Path) -> Path:
    text = inp.read_text()
    cleaned = text.replace("!", "-")
    out = inp.with_suffix(".clean.fasta")
    out.write_text(cleaned)
    info(f"Alinhamento limpo ( '!' -> '-' ): {out}")
    return out


def trim_common_overlap(aln_path: Path, enforce_codon: bool = True) -> Path:
    gap_chars = {"-", "."}

    records: list[tuple[str, str]] = []
    header: str | None = None
    seq_parts: list[str] = []

    with open(aln_path) as fin:
        for line in fin:
            if line.startswith(">"):
                if header is not None:
                    records.append((header, "".join(seq_parts)))
                header = line.strip()
                seq_parts = []
            else:
                seq_parts.append(line.strip())
    if header is not None:
        records.append((header, "".join(seq_parts)))

    if not records:
        fail(f"Alinhamento vazio: {aln_path}")

    lengths = {len(seq) for _, seq in records}
    if len(lengths) != 1:
        fail(f"Sequências com comprimentos distintos: {sorted(lengths)}")

    starts: list[int] = []
    ends: list[int] = []
    for _, seq in records:
        first = next((i for i, c in enumerate(seq) if c not in gap_chars), None)
        last = next((i for i in range(len(seq) - 1, -1, -1) if seq[i] not in gap_chars), None)
        if first is None or last is None:
            fail("Sequência com apenas gaps; não há região sobreposta comum")
        starts.append(first)
        ends.append(last)

    start = max(starts)
    end = min(ends)
    if start > end:
        fail("Não há região sobreposta sem gaps em todas as sequências")

    if enforce_codon:
        start += (3 - start % 3) % 3
        if start > end:
            fail("Janela comum ficou vazia após ajustar quadro de leitura")
        span = end - start + 1
        remainder = span % 3
        end -= remainder
        if end < start:
            fail("Janela comum ficou vazia após ajustar múltiplos de 3")

    trimmed = aln_path.with_suffix(".trimmed.fasta")
    with open(trimmed, "w") as out:
        for h, seq in records:
            out.write(f"{h}\n")
            out.write(seq[start : end + 1] + "\n")

    info(
        "Alinhamento recortado na região sobreposta: "
        f"{trimmed} (colunas {start + 1}-{end + 1})"
    )
    return trimmed


def fasta_lengths(path: Path) -> list[int]:
    lengths = []
    current = []
    with open(path) as fin:
        for line in fin:
            if line.startswith(">"):
                if current:
                    lengths.append(len("".join(current)))
                    current = []
            else:
                current.append(line.strip())
    if current:
        lengths.append(len("".join(current)))
    return lengths


def write_partitions(aln_path: Path, output: Path) -> None:
    lengths = fasta_lengths(aln_path)
    if not lengths:
        fail(f"Alinhamento vazio: {aln_path}")
    unique_lengths = set(lengths)
    if len(unique_lengths) != 1:
        fail(f"Sequências com comprimentos distintos: {sorted(unique_lengths)}")
    aln_len = unique_lengths.pop()
    if aln_len % 3 != 0:
        fail(f"Comprimento do alinhamento não é múltiplo de 3: {aln_len}")

    with open(output, "w") as out:
        out.write("#nexus\n")
        out.write("begin sets;\n")
        out.write(f"    charset codon1 = 1-{aln_len}\\3;\n")
        out.write(f"    charset codon2 = 2-{aln_len}\\3;\n")
        out.write(f"    charset codon3 = 3-{aln_len}\\3;\n")
        out.write("end;\n")

    info(f"Partições geradas: {output}")


def run_iqtree(aln: Path, partitions: Path, model: str, bootstrap: int, alrt: int, threads: str) -> None:
    cmd = [
        "iqtree2",
        "-s",
        str(aln),
        "-m",
        model,
        "-bb",
        str(bootstrap),
        "-alrt",
        str(alrt),
        "-nt",
        str(threads),
        "-p",
        str(partitions),
        "-redo",
    ]

    info("Executando IQ-TREE...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        fail("IQ-TREE retornou erro")


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    ap = argparse.ArgumentParser(description="Pipeline completo: MACSE -> limpeza -> partições -> IQ-TREE")
    ap.add_argument("fastas", nargs="+", help="FASTA(s) de entrada a concatenar e alinhar")
    ap.add_argument("--prefix", default=str(script_dir / "alinhamento_macse"), help="Prefixo de saída (default: alinhamento_macse)")
    ap.add_argument("--macse-jar", default=str(script_dir / "macse_v2.07.jar"), help="Caminho do JAR do MACSE")
    ap.add_argument("--java", default="java", help="Binário do Java")
    ap.add_argument("--genetic-code", type=int, default=5, help="Código genético (default 5: mitocôndria invertebrados)")
    ap.add_argument("--model", default="MFP+MERGE", help="Modelo para IQ-TREE (default: MFP+MERGE)")
    ap.add_argument("--bootstrap", type=int, default=1000, help="UFBoot replicates (default: 1000)")
    ap.add_argument("--alrt", type=int, default=1000, help="SH-aLRT replicates (default: 1000)")
    ap.add_argument("--threads", default="AUTO", help="Threads para IQ-TREE (default: AUTO)")
    ap.add_argument("--keep-terms", type=int, default=3, help="Quantos termos do cabeçalho FASTA manter (default: 3)")
    ap.add_argument(
        "--trim-common-overlap",
        action="store_true",
        help="Recorta o alinhamento para a região comum sem gaps nas extremidades (mantém quadro de códons)",
    )

    args = ap.parse_args()

    java_bin = ensure_executable(args.java)
    macse_jar = ensure_file(args.macse_jar, "JAR do MACSE")

    inputs = [Path(p) for p in args.fastas]
    prefix = Path(args.prefix)
    prefix.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_fasta = Path(tmpdir) / "concatenado.fasta"
        concatenate_fastas(inputs, tmp_fasta, args.keep_terms)
        aln_macse = run_macse(java_bin, macse_jar, tmp_fasta, prefix, genetic_code=args.genetic_code)

    aln_clean = clean_alignment(aln_macse)

    final_aln = aln_clean
    if args.trim_common_overlap:
        final_aln = trim_common_overlap(aln_clean)

    partitions = prefix.with_suffix(".partitions.nex")
    write_partitions(final_aln, partitions)
    run_iqtree(final_aln, partitions, args.model, args.bootstrap, args.alrt, args.threads)

    info("Pipeline concluído.")
    info(
        "Arquivos principais:\n"
        f"  Alinhamento limpo: {aln_clean}\n"
        f"  Alinhamento usado no IQ-TREE: {final_aln}\n"
        f"  Partições: {partitions}\n"
        f"  IQ-TREE: {final_aln}.iqtree / .treefile / .log"
    )


if __name__ == "__main__":
    main()
