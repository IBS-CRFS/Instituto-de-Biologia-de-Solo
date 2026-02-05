import argparse
import sys
from pathlib import Path

from Bio import AlignIO


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera partições de códons a partir de um alinhamento PRANK.")
    parser.add_argument(
        "alignment",
        nargs="?",
        default="alinhamento_prank.best.nuc.fas",
        help="Alinhamento nucleotídico (default: alinhamento_prank.best.nuc.fas)",
    )
    parser.add_argument(
        "--output",
        default="codon_partitions.nex",
        help="Arquivo de partições (default: codon_partitions.nex)",
    )

    args = parser.parse_args()

    aln_path = Path(args.alignment)
    if not aln_path.exists():
        sys.exit(f"❌ Alinhamento não encontrado: {aln_path}")

    alignment = AlignIO.read(aln_path, "fasta")
    aln_len = alignment.get_alignment_length()

    # Validar que todas as sequências têm o mesmo comprimento
    lengths = {len(rec.seq) for rec in alignment}
    if len(lengths) != 1:
        sys.exit(f"❌ Sequências com comprimentos distintos no alinhamento: {sorted(lengths)}")

    if aln_len % 3 != 0:
        sys.exit(f"❌ Comprimento do alinhamento não é múltiplo de 3: {aln_len}")

    out_path = Path(args.output)
    with open(out_path, "w") as out:
        out.write("#nexus\n")
        out.write("begin sets;\n")
        out.write(f"    charset codon1 = 1-{aln_len}\\3;\n")
        out.write(f"    charset codon2 = 2-{aln_len}\\3;\n")
        out.write(f"    charset codon3 = 3-{aln_len}\\3;\n")
        out.write("end;\n")

    print(f"✅ Partições geradas em: {out_path}")


if __name__ == "__main__":
    main()

