# Dados Brutos (Raw Data)

Pasta para armazenamento de **dados brutos originais imutáveis**.

## Princípio Fundamental

> **Dados brutos NUNCA devem ser modificados após serem colocados aqui.**

## O Que Vai Aqui

✅ **Sim**:
- Planilhas de campo originais
- Dados diretos de equipamentos
- Imagens/fotos originais não editadas
- Sequências genéticas brutas
- Arquivos de sensores
- Transcrições originais
- Dados recebidos de colaboradores

❌ **Não**:
- Dados limpos ou processados
- Análises ou resultados
- Figuras ou gráficos
- Dados agregados ou sumarizados

## Organização

Organize por:
- **Tipo de dado**: `field_data/`, `lab_data/`, `sequences/`
- **Data de coleta**: `2024-01/`, `2024-02/`
- **Local**: `site_A/`, `site_B/`
- **Experimento**: `experiment_1/`, `experiment_2/`

Exemplo:
```
raw/
├── field_data/
│   ├── 2024-01-15_site_A.csv
│   └── 2024-01-20_site_B.csv
├── lab_measurements/
│   └── soil_analysis_batch1.xlsx
└── images/
    └── specimens/
```

## Nomenclatura

Use nomes descritivos:
```
YYYY-MM-DD_tipo_local_descritor.extensao

Exemplos:
2024-01-15_soil_siteA_pH.csv
2024-02-10_photo_specimen_IBS001.jpg
2024-03-05_sequence_16S_batch2.fasta
```

## Metadados

Sempre inclua arquivo de metadados:
- `README.txt` ou `METADATA.txt` na pasta
- Descreva: origem, método de coleta, unidades, códigos
- Data e responsável pela coleta
- Equipamentos utilizados

## Formato

Prefira formatos abertos e duráveis:
- ✅ CSV (não Excel quando possível)
- ✅ TXT
- ✅ JSON
- ✅ TIFF (imagens)
- ✅ FASTA, FASTQ (sequências)

Evite formatos proprietários quando possível:
- ⚠️ XLSX (use CSV)
- ⚠️ DOCX (use TXT ou Markdown)
- ⚠️ SAS, SPSS (exporte para CSV)

## Backup

Dados brutos devem ter:
- ✅ Backup em pelo menos 2 locais diferentes
- ✅ Cópia fora do site (nuvem ou outro local)
- ✅ Verificação periódica de integridade
- ✅ Controle de versão (Git para arquivos pequenos)

## Compartilhamento

Ao compartilhar dados brutos:
1. Mantenha originais intactos
2. Forneça cópia, não o original
3. Inclua metadados completos
4. Especifique licença
5. Atribua DOI se possível (Zenodo, Dryad)

## Processamento

Para processar dados:
1. **Leia** dados de `/data/raw/`
2. **Processe** usando scripts em `/scripts/`
3. **Salve** resultados em `/data/processed/`
4. **Documente** processamento no script

## Versionamento

Se precisar "versionar" dados brutos (não recomendado):
- Use nomes diferentes para cada versão
- Documente razão da nova versão
- Mantenha todas as versões

Melhor: Mantenha dados brutos intactos e versione apenas scripts de processamento.

Ver também:
- `/data/processed/README.md` - Dados processados
- `/scripts/README.md` - Scripts de processamento
- `/DATA_POLICY.md` - Política de dados
