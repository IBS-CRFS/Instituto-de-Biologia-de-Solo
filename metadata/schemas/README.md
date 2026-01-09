# Esquemas de Metadados

Templates e **esquemas padrão** para metadados de dados biológicos e científicos.

## Arquivos

### darwin_core_template.csv
Template com todos os campos do padrão Darwin Core para dados de biodiversidade.

**Uso**: Dados de espécimes da coleção de referência

**Campos principais**:
- Occurrence (ocorrência)
- Taxon (taxonomia)
- Location (localização)
- Event (evento de coleta)
- MeasurementOrFact (medições)

**Documentação**: https://dwc.tdwg.org/terms/

### Como Usar Darwin Core

1. Copie o arquivo template
2. Preencha uma linha por espécime
3. Use codificação UTF-8
4. Datas em formato ISO 8601 (YYYY-MM-DD)
5. Coordenadas em graus decimais (WGS84)
6. Valide antes de publicar

### Outros Esquemas

Para adicionar novos esquemas de metadados:
- EML (Ecological Metadata Language)
- ISO 19115 (Geographic metadata)
- DataCite (DOI metadata)
- Dublin Core (Generic metadata)

## Validação

Antes de usar dados em produção:

**Darwin Core**:
```bash
# Use GBIF Data Validator
# https://www.gbif.org/tools/data-validator
```

**CSV Geral**:
```bash
# Valide formato CSV
csvlint seu_arquivo.csv
```

## Campos Obrigatórios

### Darwin Core Occurrence
- `catalogNumber` - Número único do espécime
- `basisOfRecord` - Tipo de registro
- `scientificName` - Nome científico
- `eventDate` - Data de coleta
- `decimalLatitude`, `decimalLongitude` - Coordenadas

### Campos Recomendados
- Classificação taxonômica completa
- Identificador (identifiedBy)
- Localidade detalhada
- Método de coleta
- Preparação do espécime

## Integração

Dados no padrão Darwin Core podem ser:
- Publicados no GBIF
- Compartilhados com SiBBr
- Integrados em bancos internacionais
- Citados com DOI via Zenodo

## Ajuda

Para dúvidas sobre metadados:
- **Email**: dados@ibs.br
- **Documentação**: `/docs/templates/`
- **GBIF BR**: https://www.gbif.org/pt/

Ver também:
- `/colecao-referencia/darwin-core/` - Dados da coleção
- `/metadata/README.md` - Visão geral de metadados
