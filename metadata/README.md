# Metadados e Esquemas

Esta pasta contém **esquemas de metadados** e templates para padronização de dados do instituto.

## Estrutura

```
metadata/
└── schemas/        # Esquemas e templates de metadados
```

## Conteúdo

### Esquemas Disponíveis

1. **Darwin Core** (`schemas/darwin_core_template.csv`)
   - Padrão internacional para dados de biodiversidade
   - Uso: Dados de espécimes da coleção
   - Documentação: https://dwc.tdwg.org/terms/

2. **EML - Ecological Metadata Language**
   - Para metadados ecológicos
   - Uso: Datasets ecológicos, projetos de campo

3. **Metadata JSON** (`/docs/templates/metadata_template.json`)
   - Template JSON genérico
   - Uso: Projetos científicos, datasets diversos

## Padrões Seguidos

- **Darwin Core**: TDWG Biodiversity Information Standards
- **EML**: Knowledge Network for Biocomplexity
- **ISO 19115**: Geographic Information - Metadata
- **DataCite**: Para DOIs de datasets

## Como Usar

1. Escolha o esquema apropriado para seus dados
2. Copie o template
3. Preencha com suas informações
4. Valide usando ferramentas apropriadas
5. Inclua no seu projeto/dataset

## Validação

### Darwin Core
- GBIF Data Validator: https://www.gbif.org/tools/data-validator
- IPT: Integrated Publishing Toolkit

### EML
- EML Parser & Validator online

### JSON
- JSONLint: https://jsonlint.com/
- Schema validators

## Criando Novos Esquemas

Se precisar criar novo esquema:
1. Documente claramente campos e tipos
2. Inclua exemplos
3. Adicione validação
4. Crie README explicativo
5. Compartilhe com equipe para revisão

## Metadados Mínimos

Todo dataset deve incluir:
- ✅ Título
- ✅ Autores/criadores
- ✅ Data de criação
- ✅ Descrição
- ✅ Palavras-chave
- ✅ Licença
- ✅ Contato

## Recursos

- TDWG: https://www.tdwg.org/
- DataCite Metadata Schema: https://schema.datacite.org/
- Dublin Core: https://www.dublincore.org/

Ver também:
- `/docs/templates/` - Templates adicionais
- `/DATA_POLICY.md` - Política de dados e metadados
