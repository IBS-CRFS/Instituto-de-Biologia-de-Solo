# Diretório de Dados

Este diretório contém os conjuntos de dados utilizados e produzidos pelo Instituto de Biologia do Solo.

## Estrutura

- **`raw/`**: Dados brutos originais, não processados e imutáveis
- **`processed/`**: Dados processados, limpos e prontos para análise

## Organização de Dados Brutos (`raw/`)

### Princípios

1. **Imutabilidade**: Dados brutos NUNCA devem ser modificados
2. **Documentação**: Sempre acompanhados de metadados
3. **Formato original**: Preservar formato original da coleta/geração
4. **Backup**: Manter cópias de segurança

### Convenções de Nomenclatura

```
[projeto]_[tipo]_[data]_[versao].[extensao]

Exemplos:
- mata_atlantica_ocorrencias_2024-01-15_v1.csv
- coleta_campo_ambiental_2023-12-20_v1.xlsx
- laboratorio_morfometria_2024-02-01_v1.csv
```

## Organização de Dados Processados (`processed/`)

### Transformações Comuns

- Limpeza de dados (remoção de erros, duplicatas)
- Padronização (formatos, unidades, nomenclatura)
- Harmonização taxonômica
- Agregação e sumarização
- Conversão para padrões (Darwin Core)

### Documentação Obrigatória

Cada dado processado deve incluir:

1. **README**: Descrição do processamento
2. **Script**: Código que gerou os dados processados
3. **Metadados**: Informações sobre transformações
4. **Changelog**: Histórico de versões

### Exemplo de Estrutura

```
processed/
└── mata_atlantica_fauna_dwc/
    ├── README.md                    # Descrição
    ├── occurrences.csv              # Dados em Darwin Core
    ├── metadata.json                # Metadados
    ├── data_dictionary.csv          # Dicionário de dados
    └── processing_script.R          # Script de processamento
```

## Formatos de Arquivo Recomendados

### Preferidos (Abertos e Interoperáveis)

| Tipo | Formato | Extensão | Notas |
|------|---------|----------|-------|
| Tabular | CSV | .csv | UTF-8, separador definido |
| Estruturado | JSON | .json | Para metadados complexos |
| Texto | TXT | .txt | Texto simples |
| Espacial | GeoJSON | .geojson | Dados geográficos |
| Taxonômico | DwC-A | .zip | Darwin Core Archive |

### Aceitáveis

| Tipo | Formato | Extensão | Notas |
|------|---------|----------|-------|
| Tabular | Excel | .xlsx | Apenas para raw; converter para CSV |
| Estatístico | RDS | .rds | Objetos R, incluir CSV também |
| Espacial | Shapefile | .shp | Incluir GeoJSON também |

### Evitar

- Formatos proprietários sem especificação aberta
- Formatos binários não documentados
- PDFs para dados tabulares

## Metadados

### Arquivo metadata.json

Cada conjunto de dados deve ter um arquivo `metadata.json` com:

```json
{
  "title": "Título do conjunto de dados",
  "description": "Descrição detalhada",
  "source": "raw/arquivo_original.csv",
  "processing_date": "2024-01-15",
  "processed_by": "Nome (ORCID)",
  "license": "CC0-1.0",
  "format": "CSV",
  "encoding": "UTF-8",
  "records": 1500,
  "fields": 25,
  "temporal_coverage": "2023-01-01/2023-12-31",
  "spatial_coverage": "Mata Atlântica, Brasil",
  "taxonomic_coverage": ["Annelida", "Arthropoda"],
  "related_publication": "DOI ou referência",
  "version": "1.0.0",
  "changelog": "Versão inicial"
}
```

### Dicionário de Dados

Arquivo `data_dictionary.csv` descrevendo cada campo:

```csv
field_name,description,type,unit,allowed_values,missing_value
sampleID,Identificador único da amostra,string,,NA,
date,Data de coleta,date,ISO8601,,
latitude,Latitude em graus decimais,numeric,degrees,,-999
species,Nome científico,string,,,NA
abundance,Número de indivíduos,integer,count,0-1000,
```

## Controle de Qualidade

### Checklist para Dados Brutos

- [ ] Arquivo em formato aberto ou conversível
- [ ] Nome do arquivo segue convenções
- [ ] Metadados completos fornecidos
- [ ] Proveniência documentada
- [ ] Backup realizado

### Checklist para Dados Processados

- [ ] Script de processamento incluído e executável
- [ ] Transformações documentadas
- [ ] Validações aplicadas (taxonomia, geografia, etc.)
- [ ] Dados seguem padrões (Darwin Core quando aplicável)
- [ ] Dicionário de dados criado
- [ ] Metadados atualizados
- [ ] Testes de qualidade executados

## Padrões de Dados

### Darwin Core

Para dados de biodiversidade, use Darwin Core. Campos essenciais:

**Núcleo de Ocorrência:**
- occurrenceID
- scientificName
- decimalLatitude, decimalLongitude
- eventDate
- basisOfRecord

Ver: `/metadata/schemas/darwin_core_template.csv`

### Ecological Metadata Language (EML)

Para datasets ecológicos complexos, considere EML:
- https://eml.ecoinformatics.org/

## Dados Sensíveis

### Tipos de Sensibilidade

1. **Espécies ameaçadas**: Coordenadas exatas podem facilitar coleta ilegal
2. **Propriedade privada**: Localidades específicas de áreas privadas
3. **Dados pessoais**: Informações identificáveis (LGPD)

### Tratamento

- **Generalização**: Arredondar coordenadas (0.1° ou município)
- **Omissão**: Remover campos sensíveis
- **Restrição de acesso**: Disponibilizar mediante solicitação
- **Documentação**: Indicar generalizações em metadados

Campos Darwin Core relevantes:
- `dataGeneralizations`: Descrever generalizações aplicadas
- `informationWithheld`: Informações omitidas e razão

## Versionamento

### Quando Versionar

- Correções de erros
- Adição de novos registros
- Mudanças nos métodos de processamento
- Atualizações taxonômicas

### Formato de Versão

Usar Semantic Versioning:
- **MAJOR.MINOR.PATCH** (ex: 2.1.3)
- MAJOR: Mudanças incompatíveis
- MINOR: Adições compatíveis
- PATCH: Correções

### Histórico

Manter arquivo CHANGELOG.md para cada dataset versionado.

## Tamanho de Arquivos

### Limites do GitHub

- Arquivos individuais: Máximo 100 MB
- Repositório total: Recomendado < 1 GB

### Dados Grandes

Para datasets > 50 MB:
1. **Zenodo**: Upload direto (recomendado)
2. **GitHub LFS**: Git Large File Storage
3. **Fragmentação**: Dividir em arquivos menores

Incluir no repositório GitHub:
- Metadados completos
- Amostra dos dados (primeiras 1000 linhas)
- Link para dados completos

## Ferramentas Úteis

### Validação de Dados

**R:**
```r
# Validar Darwin Core
install.packages("bdverse")
library(bdDwC)
bdDwC::darwinize_names(data)

# Validar coordenadas
library(CoordinateCleaner)
clean_coordinates(data)
```

**Python:**
```python
# Validar Darwin Core
import pygbif
from dwca.read import DwCAReader

# Validar CSV
import pandas as pd
import pandera as pa
```

### Conversão de Formatos

**CSV para Darwin Core Archive:**
- [IPT - Integrated Publishing Toolkit](https://www.gbif.org/ipt)
- Pacote R: `finch`

**Excel para CSV:**
```r
library(readxl)
data <- read_excel("data.xlsx")
write.csv(data, "data.csv", row.names = FALSE, fileEncoding = "UTF-8")
```

## Contribuindo com Dados

Ver [CONTRIBUTING.md](../CONTRIBUTING.md) para:
- Processo de submissão
- Templates e checklists
- Padrões de qualidade
- Revisão e aprovação

## Repositórios Externos

Além deste repositório, dados podem ser compartilhados em:

- **GBIF**: Dados de biodiversidade
- **GenBank**: Sequências genéticas
- **Dryad**: Dados de publicações
- **Zenodo**: Qualquer tipo de dado científico
- **SiBBr**: Sistema de Informação sobre Biodiversidade Brasileira

## Recursos

- [Darwin Core](https://dwc.tdwg.org/)
- [GBIF Data Quality](https://www.gbif.org/data-quality-requirements)
- [FAIR Principles](https://www.go-fair.org/fair-principles/)
- [EML Documentation](https://eml.ecoinformatics.org/)

## Contato

Dúvidas sobre dados:
- Issues: [GitHub Issues]
- Email: [email institucional]
