# Darwin Core - Dados da Coleção

Esta pasta contém os dados da **Coleção de Referência da Fauna de Solos** no padrão **Darwin Core**.

## Conteúdo

### occurrences.csv
Arquivo principal com registros de ocorrência de todos os espécimes da coleção. Cada linha representa um espécime catalogado.

**Campos principais**:
- `catalogNumber`: Número de catálogo único (ex: IBS-0001)
- `scientificName`: Nome científico completo
- `basisOfRecord`: Sempre "PreservedSpecimen"
- `decimalLatitude`, `decimalLongitude`: Coordenadas de coleta
- `eventDate`: Data de coleta
- `identifiedBy`: Quem identificou o espécime

### taxonomy.csv
Informações taxonômicas detalhadas incluindo sinonímias e referências bibliográficas.

### measurements.csv
Medidas morfológicas dos espécimes seguindo o padrão Darwin Core MeasurementOrFact.

## Padrão Darwin Core

O Darwin Core é um padrão internacional mantido pela TDWG (Biodiversity Information Standards) para dados de biodiversidade.

**Documentação oficial**: https://dwc.tdwg.org/terms/

## Como Adicionar Dados

1. Abra o arquivo CSV correspondente
2. Adicione uma nova linha com os dados do espécime
3. Preencha todos os campos obrigatórios
4. Use o formato ISO 8601 para datas (YYYY-MM-DD)
5. Coordenadas em graus decimais (WGS84)
6. Salve com codificação UTF-8

## Validação

Antes de publicar, valide os dados usando:
- **GBIF Data Validator**: https://www.gbif.org/tools/data-validator
- **IPT (Integrated Publishing Toolkit)**: Para geração de Darwin Core Archive

## Publicação

Os dados são publicados em:
- **GBIF** (Global Biodiversity Information Facility)
- **SiBBr** (Sistema de Informação sobre a Biodiversidade Brasileira)

Ver instruções completas em `/colecao-referencia/README.md`
