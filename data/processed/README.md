# Dados Processados (Processed Data)

Pasta para **dados limpos, processados e prontos para análise**.

## O Que Vai Aqui

✅ **Sim**:
- Dados limpos (outliers removidos, valores corrigidos)
- Dados padronizados/normalizados
- Dados agregados ou sumarizados
- Matrizes de dados para análise
- Dados em formato adequado para software específico
- Tabelas derivadas dos dados brutos

❌ **Não**:
- Dados brutos originais (vão em `/data/raw/`)
- Resultados de análises (vão em `/results/`)
- Figuras ou gráficos (vão em `/results/figures/`)
- Scripts de processamento (vão em `/scripts/`)

## Rastreabilidade

Todo dado processado deve ser:
- **Reproduzível**: Script em `/scripts/` que gera a partir do raw
- **Documentado**: README explica processamento
- **Versionado**: Via Git ou changelog

## Organização

```
processed/
├── community_matrix.csv      # Matriz espécie × sítio
├── environmental_vars.csv    # Variáveis ambientais padronizadas
├── diversity_metrics.csv     # Índices calculados
├── soil_properties_clean.csv # Dados de solo limpos
└── README.txt               # Descreve cada arquivo
```

## Nomenclatura

Use nomes descritivos que indicam conteúdo:
```
tipo_descritor_versao.extensao

Exemplos:
community_matrix_v1.csv
soil_chemistry_standardized.csv
abundance_aggregated_by_site.csv
```

## Documentação

Cada arquivo processado precisa:

**No README ou metadados**:
- Origem (qual raw data)
- Processamento aplicado
- Script usado (com versão/commit)
- Data do processamento
- Responsável
- Unidades e códigos

**Exemplo**:
```
community_matrix.csv
- Origem: raw/field_data/*.csv
- Processamento: Agregação por espécie e sítio
- Script: scripts/01_create_community_matrix.R
- Data: 2024-01-20
- Por: João Silva
- Unidades: Abundância (ind/m²)
```

## Formato

Prefira formatos abertos e análise-ready:
- ✅ CSV (padronizado, UTF-8)
- ✅ TSV (tab-separated)
- ✅ JSON (dados estruturados)
- ✅ Parquet (grandes volumes)
- ✅ HDF5 (dados multidimensionais)

Para formatos específicos:
- R: RDS, RData
- Python: pickle, feather
- GIS: GeoJSON, Shapefiles

## Controle de Qualidade

Antes de considerar dados como "processados":
- ✅ Verificar valores ausentes
- ✅ Conferir tipos de dados
- ✅ Validar ranges esperados
- ✅ Verificar consistência
- ✅ Documentar decisões de limpeza

## Versionamento

Quando atualizar dados processados:
- Incremente versão no nome: `_v1`, `_v2`
- OU use Git para versionamento automático
- Documente mudanças em CHANGELOG
- Mantenha versão anterior se usada em análises publicadas

## Workflow Típico

```
1. Raw data → 2. Script de limpeza → 3. Processed data → 4. Análise
   (/raw/)        (/scripts/)            (/processed/)      (gera /results/)
```

## Reprodutibilidade

Para garantir reprodutibilidade:

```R
# Exemplo em R
raw_data <- read.csv("data/raw/field_data.csv")
processed_data <- clean_and_process(raw_data)
write.csv(processed_data, "data/processed/field_data_clean.csv")
```

**Importante**: O script deve ser executável por outro pesquisador!

## Metadados

Inclua arquivo de metadados:
- `data_dictionary.csv` - Descrição de cada variável
- `processing_log.txt` - Log do processamento
- `README.md` - Visão geral

## Compartilhamento

Ao compartilhar dados processados:
1. Inclua scripts que geraram
2. Inclua metadados completos
3. Especifique software/versões usadas
4. Forneça exemplo de uso
5. Atribua DOI se possível

Ver também:
- `/data/raw/README.md` - Dados brutos
- `/scripts/README.md` - Scripts de processamento
- `/docs/templates/metadata_template.json` - Template de metadados
