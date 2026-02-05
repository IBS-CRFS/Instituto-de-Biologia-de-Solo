# Pipeline MACSE + IQ-TREE

Guia rápido para rodar o alinhamento codon-aware e a árvore filogenética a partir de FASTAs.

## Requisitos
- Python 3 (usa o script `run_pipeline_macse_iqtree.py`)
- Java (para MACSE)
- `macse_v2.07.jar` na mesma pasta do script ou informar caminho via flag
- IQ-TREE2 disponível no PATH (`iqtree2`)

## Entradas
- Um ou mais arquivos FASTA com sequências de DNA (codificante). O script concatena tudo antes de alinhar.

## Saídas principais
- `<prefix>.macse.nt.clean.fasta` — alinhamento MACSE nucleotídico com `!` limpos para `-`
- `<prefix>.macse.nt.clean.trimmed.fasta` — opcional: alinhamento recortado na região comum (se `--trim-common-overlap`)
- `<prefix>.partitions.nex` — partições de códons (1/2/3)
- IQ-TREE: `<prefix>.macse.nt.clean[.trimmed].fasta.iqtree / .treefile / .log`

## Uso básico
Na pasta `scripts/`:

```bash
python run_pipeline_macse_iqtree.py \
  --keep-terms 3 \
  --bootstrap 1000 \
  --alrt 1000 \
  --threads AUTO \
  --prefix ./alinhamento_macse \
  *.fasta
```

## Opções úteis
- `--keep-terms N` : quantos termos do cabeçalho manter (separa por espaço e junta com `_`). Default 3.
- `--macse-jar PATH` : caminho para `macse_v2.07.jar` (default: mesmo diretório do script).
- `--java BIN` : binário do Java (default: `java`).
- `--genetic-code INT` : código genético para MACSE (default 5 = mitocôndria invertebrados).
- `--model STRING` : modelo para IQ-TREE (default `MFP+MERGE`).
- `--bootstrap INT` : replicados UFBoot (default 1000).
- `--alrt INT` : replicados SH-aLRT (default 1000).
- `--threads AUTO` : threads para IQ-TREE (default AUTO).
- `--trim-common-overlap` : recorta o alinhamento para a região sobreposta sem gaps nas extremidades, mantendo quadro de códons.
- `--prefix PATH` : prefixo para todos os outputs (pode incluir diretório).

## Exemplos
1) Rodar um FASTA único, recortando para região comum:
```bash
python run_pipeline_macse_iqtree.py --trim-common-overlap --prefix ./alinh_teste sample.fasta
```

2) Vários FASTAs, sem recorte, mantendo 4 termos no cabeçalho:
```bash
python run_pipeline_macse_iqtree.py --keep-terms 4 --prefix ./alinh_full genes/*.fasta
```

3) Alterar bootstrap e modelo:
```bash
python run_pipeline_macse_iqtree.py --bootstrap 5000 --alrt 1000 --model GTR+F+I+G4 *.fasta
```

## Notas sobre o recorte (`--trim-common-overlap`)
- O script encontra o primeiro/último sítio não-gap em cada sequência, toma a interseção (janela comum) e ajusta ao quadro de códons.
- Se não houver sobreposição suficiente, ele aborta com erro.
- A partição é gerada a partir do alinhamento final (recortado, se ativado).

## Logs e diagnósticos
- MACSE: `<prefix>.macse.log`
- IQ-TREE: `<prefix>.macse.nt.clean[.trimmed].fasta.log`
- Esquema de partições/modelos: `<prefix>.partitions.nex.best_scheme.nex` e `<prefix>.partitions.nex.best_model.nex`

## Dicas
- Se IQ-TREE avisar sobre composição distinta em algumas sequências, revise essas entradas.
- Sequências idênticas são detectadas; algumas podem ser ignoradas na busca, mas retornam no consenso.
- Para cabeçalhos longos, ajuste `--keep-terms` para evitar truncamentos pelo IQ-TREE.

## Caminhos padrão
- Rodando de `scripts/`, o default `--prefix ./alinhamento_macse` grava os arquivos na própria pasta `scripts/`.


/home/nathan/Documents/GitHub/IBS/.venv/bin/python /home/nathan/Documents/GitHub/IBS/projects/Troglobius_BR/scripts/run_pipeline_macse_iqtree.py --trim-common-overlap --prefix /home/nathan/Documents/GitHub/IBS/projects/Troglobius_BR/scripts/alinhamento_teste_trim /home/nathan/Documents/GitHub/IBS/projects/Troglobius_BR/scripts/todas_sequencias.fasta

cd /home/nathan/Documents/GitHub/IBS/projects/Troglobius_BR/scripts && /home/nathan/Documents/GitHub/IBS/.venv/bin/python run_pipeline_macse_iqtree.py todas_sequencias.fasta --macse-jar macse_v2.07.jar --trim-common-overlap --prefix alinhamento_macse_atual --keep-terms 3