import subprocess
import sys
from pathlib import Path


def run_iqtree(
    alignment,
    model="MFP+MERGE",
    partitions=None,
    bootstrap=1000,
    alrt=1000,
    threads="AUTO",
    redo=True
):
    """
    Executa IQ-TREE a partir de um alinhamento FASTA
    """

    alignment = Path(alignment)

    if not alignment.exists():
        sys.exit(f"❌ Alinhamento não encontrado: {alignment}")

    cmd = [
        "iqtree2",
        "-s", str(alignment),
        "-m", model,
        "-bb", str(bootstrap),
        "-alrt", str(alrt),
        "-nt", str(threads)
    ]

    if partitions:
        partitions = Path(partitions)
        if not partitions.exists():
            sys.exit(f"❌ Arquivo de partições não encontrado: {partitions}")
        cmd.extend(["-p", str(partitions)])

    if redo:
        cmd.append("-redo")

    print("\n🔹 Executando IQ-TREE:")
    print(" ".join(cmd))

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("\n❌ ERRO no IQ-TREE:")
        print(result.stderr)
        sys.exit(1)

    print("\n✅ IQ-TREE finalizado com sucesso")
    print(result.stdout)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit(
            "Uso:\n"
            "python rodar_iqtree.py alinhamento.fasta [particoes.nex]\n"
        )

    alignment = sys.argv[1]
    partitions = sys.argv[2] if len(sys.argv) == 3 else None

    run_iqtree(
        alignment=alignment,
        model="MFP+MERGE",
        partitions=partitions,
        bootstrap=10000,
        alrt=10000,
        threads="AUTO",
        redo=True
    )

