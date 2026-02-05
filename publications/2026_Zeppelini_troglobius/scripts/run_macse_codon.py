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


def ensure_jar(path_str: str) -> Path:
    jar = Path(path_str)
    if not jar.exists():
        fail(f"JAR do MACSE não encontrado: {jar}")
    return jar


def concatenate_fastas(inputs: list[Path], output: Path) -> None:
    with open(output, "w") as fout:
        for p in inputs:
            if not p.exists():
                fail(f"Arquivo FASTA não encontrado: {p}")
            with open(p) as fin:
                for line in fin:
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


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    ap = argparse.ArgumentParser(description="Alinhamento codon-aware com MACSE (gc_def=5 para COI de invertebrados)")
    ap.add_argument("fastas", nargs="+", help="FASTA(s) de entrada a concatenar e alinhar")
    ap.add_argument("--prefix", default=str(script_dir / "alinhamento_macse"), help="Prefixo de saída (default: alinhamento_macse)")
    ap.add_argument("--macse-jar", default=str(script_dir / "macse_v2.07.jar"), help="Caminho do JAR do MACSE (default: macse_v2.07.jar na pasta do script)")
    ap.add_argument("--java", default="java", help="Binário do Java (default: java no PATH)")
    ap.add_argument("--genetic-code", type=int, default=5, help="Código genético (default 5: mitocôndria invertebrados)")

    args = ap.parse_args()

    java_bin = ensure_executable(args.java)
    macse_jar = ensure_jar(args.macse_jar)

    inputs = [Path(p) for p in args.fastas]
    prefix = Path(args.prefix)
    prefix.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_fasta = Path(tmpdir) / "concatenado.fasta"
        concatenate_fastas(inputs, tmp_fasta)
        run_macse(java_bin, macse_jar, tmp_fasta, prefix, genetic_code=args.genetic_code)

    info("Use o alinhamento NT do MACSE diretamente para gerar partições e rodar o IQ-TREE.")


if __name__ == "__main__":
    main()
