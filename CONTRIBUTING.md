# Guia de Contribuição

Obrigado pelo interesse em contribuir para o **Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos**! Este documento fornece diretrizes para contribuir com dados, código, documentação e melhorias.

## Índice

- [Código de Conduta](#código-de-conduta)
- [Como Contribuir](#como-contribuir)
- [Reportando Problemas](#reportando-problemas)
- [Submetendo Dados](#submetendo-dados)
- [Contribuindo com Código](#contribuindo-com-código)
- [Melhorando a Documentação](#melhorando-a-documentação)
- [Padrões e Boas Práticas](#padrões-e-boas-práticas)
- [Processo de Revisão](#processo-de-revisão)

## Código de Conduta

### Nossa Promessa

No interesse de promover um ambiente aberto e acolhedor, comprometemo-nos a tornar a participação em nosso projeto e comunidade uma experiência livre de assédio para todos, independentemente de:
- Idade, tamanho corporal, deficiência
- Etnia, identidade e expressão de gênero
- Nível de experiência, educação, status socioeconômico
- Nacionalidade, aparência pessoal, raça
- Religião ou identidade e orientação sexual

### Comportamento Esperado

- Usar linguagem acolhedora e inclusiva
- Respeitar diferentes pontos de vista e experiências
- Aceitar críticas construtivas com elegância
- Focar no que é melhor para a comunidade
- Demonstrar empatia com outros membros

### Comportamento Inaceitável

- Uso de linguagem ou imagens sexualizadas
- Trolling, comentários insultuosos ou depreciativos
- Assédio público ou privado
- Publicar informações privadas de terceiros sem permissão
- Outras condutas consideradas inapropriadas em ambiente profissional

## Como Contribuir

Existem várias formas de contribuir:

### 1. Reportar Problemas
- Erros nos dados
- Bugs em scripts
- Problemas na documentação
- Sugestões de melhorias

### 2. Submeter Dados
- Novos conjuntos de dados
- Atualizações de dados existentes
- Correções taxonômicas
- Dados complementares

### 3. Contribuir com Código
- Scripts de análise
- Ferramentas de processamento
- Visualizações
- Automações

### 4. Melhorar Documentação
- Correções e clarificações
- Novos tutoriais
- Traduções
- Exemplos de uso

## Reportando Problemas

### Antes de Criar uma Issue

1. **Busque issues existentes**: Verifique se o problema já foi reportado
2. **Verifique a documentação**: O problema pode estar documentado
3. **Teste na versão mais recente**: Confirme se o problema persiste

### Criando uma Issue

Use os templates fornecidos e inclua:

#### Para Erros nos Dados
```markdown
**Descrição do erro**
Descrição clara do problema nos dados

**Localização**
- Arquivo: [caminho/arquivo.csv]
- Linha(s): [número(s)]
- Campo(s): [nome(s) do(s) campo(s)]

**Erro esperado vs. observado**
- Esperado: [valor correto]
- Observado: [valor incorreto]

**Evidência**
Links para referências taxonômicas, literatura, etc.

**Contexto adicional**
Qualquer informação relevante
```

#### Para Bugs em Scripts
```markdown
**Descrição do bug**
Descrição clara do problema

**Como reproduzir**
Passos para reproduzir o comportamento:
1. Execute '...'
2. Com parâmetros '...'
3. Veja erro '...'

**Comportamento esperado**
O que deveria acontecer

**Ambiente**
- OS: [ex: Ubuntu 22.04]
- Versão do R/Python: [ex: R 4.3.0]
- Pacotes e versões: [ex: dplyr 1.1.0]

**Logs e mensagens de erro**
```
[cole aqui]
```
```

## Submetendo Dados

### Requisitos Mínimos

Todos os conjuntos de dados devem incluir:

1. **Dados em formato aberto**: CSV, TXT, JSON (preferível a formatos proprietários)
2. **Metadados completos**: Seguindo template fornecido
3. **Dicionário de dados**: Descrição de todas as variáveis
4. **Licença clara**: CC0 ou CC BY 4.0
5. **Informações de citação**: Como citar os dados

### Estrutura de Submissão

Organize sua contribuição seguindo esta estrutura:

```
submissions/
└── [seu_nome]_[data_submissao]/
    ├── README.md                  # Descrição geral
    ├── metadata.json              # Metadados estruturados
    ├── data/
    │   ├── raw/                   # Dados brutos originais
    │   └── processed/             # Dados processados (opcional)
    ├── scripts/                   # Scripts de processamento (opcional)
    └── documentation/
        ├── data_dictionary.csv    # Dicionário de dados
        └── methods.md             # Métodos de coleta/geração
```

### Template de Metadados

Copie e preencha o template em `/docs/templates/metadata_template.json`:

```json
{
  "title": "Título descritivo do conjunto de dados",
  "creators": [
    {
      "name": "Nome Completo",
      "affiliation": "Instituição",
      "orcid": "0000-0000-0000-0000"
    }
  ],
  "description": "Descrição detalhada do conjunto de dados",
  "keywords": ["palavra-chave1", "palavra-chave2"],
  "license": "CC0-1.0 ou CC-BY-4.0",
  "temporal_coverage": "YYYY-MM-DD/YYYY-MM-DD",
  "spatial_coverage": {
    "description": "Área de estudo",
    "coordinates": "bounding box ou WKT"
  },
  "taxonomic_coverage": ["taxa incluídos"],
  "methodology": "Breve descrição dos métodos",
  "related_publications": ["DOI ou referência"],
  "funding": "Agências financiadoras",
  "version": "1.0.0",
  "last_updated": "YYYY-MM-DD"
}
```

### Padrões de Dados

#### Dados de Biodiversidade (Darwin Core)

Para dados de ocorrência, siga o padrão Darwin Core. Campos obrigatórios:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| occurrenceID | Identificador único | "urn:uuid:..." |
| scientificName | Nome científico completo | "Homo sapiens Linnaeus, 1758" |
| decimalLatitude | Latitude em graus decimais | -23.5505 |
| decimalLongitude | Longitude em graus decimais | -46.6333 |
| eventDate | Data de coleta (ISO 8601) | 2024-01-15 |
| basisOfRecord | Tipo de registro | "PreservedSpecimen" |

Consulte `/metadata/schemas/darwin_core_template.csv` para template completo.

#### Formatos de Arquivo

**Preferidos:**
- CSV (UTF-8, vírgula ou ponto-e-vírgula como separador)
- JSON (para dados estruturados complexos)
- TXT (texto simples)
- XML (para formatos padronizados)

**Aceitáveis:**
- Excel (.xlsx) - será convertido para CSV
- Shapefiles (para dados espaciais) - complementados com GeoJSON

**Evitar:**
- Formatos proprietários sem especificação aberta
- Formatos binários não documentados

### Processo de Submissão

1. **Fork o repositório**
   ```bash
   # Via interface do GitHub ou
   gh repo fork nathanufpb/Instituto-de-Biologia-de-Solo
   ```

2. **Crie um branch para sua submissão**
   ```bash
   git checkout -b submission/nome-descritivo
   ```

3. **Adicione seus dados e metadados**
   - Siga a estrutura descrita acima
   - Valide metadados usando ferramentas fornecidas

4. **Commit com mensagem descritiva**
   ```bash
   git add .
   git commit -m "Add: [título do dataset] - [breve descrição]"
   ```

5. **Push e crie Pull Request**
   ```bash
   git push origin submission/nome-descritivo
   ```
   - Preencha o template de PR
   - Marque revisores relevantes

## Contribuindo com Código

### Configuração do Ambiente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo.git
   cd Instituto-de-Biologia-de-Solo
   ```

2. **Configure ambiente virtual (se usar Python)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Configure ambiente R (se usar R)**
   ```R
   install.packages("renv")
   renv::restore()
   ```

### Padrões de Código

#### Python
- Siga [PEP 8](https://pep8.org/)
- Use type hints quando possível
- Docstrings no formato Google/NumPy
- Teste com `black` e `flake8`

```python
def process_occurrence_data(data: pd.DataFrame, 
                           validate: bool = True) -> pd.DataFrame:
    """
    Process occurrence data according to Darwin Core standard.
    
    Args:
        data: Raw occurrence data
        validate: Whether to validate against Darwin Core terms
        
    Returns:
        Processed and validated DataFrame
        
    Raises:
        ValueError: If required fields are missing
    """
    # Implementation
    pass
```

#### R
- Siga [Tidyverse Style Guide](https://style.tidyverse.org/)
- Use roxygen2 para documentação
- Organize em funções modulares

```r
#' Process Occurrence Data
#'
#' @param data Raw occurrence data frame
#' @param validate Logical, whether to validate
#' @return Processed data frame
#' @export
process_occurrence_data <- function(data, validate = TRUE) {
  # Implementation
}
```

### Testes

Sempre inclua testes para código novo:

**Python (pytest):**
```python
def test_process_occurrence_data():
    """Test basic occurrence data processing."""
    raw_data = pd.DataFrame({...})
    result = process_occurrence_data(raw_data)
    assert not result.empty
    assert "scientificName" in result.columns
```

**R (testthat):**
```r
test_that("process_occurrence_data works correctly", {
  raw_data <- data.frame(...)
  result <- process_occurrence_data(raw_data)
  expect_false(nrow(result) == 0)
  expect_true("scientificName" %in% names(result))
})
```

### Documentação de Código

- Comente código complexo
- Documente todas as funções públicas
- Inclua exemplos de uso
- Mantenha README atualizado

## Melhorando a Documentação

### Tipos de Documentação

1. **README e guias**: Markdown claro e conciso
2. **Tutoriais**: Passo-a-passo com exemplos
3. **Referência**: Documentação técnica detalhada
4. **FAQs**: Perguntas frequentes

### Estrutura de Tutoriais

```markdown
# Título do Tutorial

## Objetivo
O que você aprenderá

## Pré-requisitos
- Item 1
- Item 2

## Passo 1: [Ação]
Explicação e código

## Passo 2: [Ação]
Explicação e código

## Resultado Esperado
O que você deve obter

## Próximos Passos
Links para tutoriais relacionados
```

## Padrões e Boas Práticas

### Versionamento Semântico

- **MAJOR** (1.0.0): Mudanças incompatíveis
- **MINOR** (0.1.0): Nova funcionalidade compatível
- **PATCH** (0.0.1): Correções de bugs

### Mensagens de Commit

Siga [Conventional Commits](https://www.conventionalcommits.org/):

```
tipo(escopo): descrição curta

Descrição mais detalhada se necessário.

Fixes #123
```

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `data`: Adição/modificação de dados
- `refactor`: Refatoração de código
- `test`: Testes
- `chore`: Manutenção

**Exemplos:**
```
feat(metadata): add Darwin Core validation function
fix(data): correct coordinates for specimens XYZ
docs(readme): update citation instructions
data: add soil fauna dataset from 2024 survey
```

### Nomenclatura de Arquivos

- **Letras minúsculas**: use snake_case
- **Sem espaços**: use underscores
- **Datas**: formato ISO 8601 (YYYY-MM-DD)
- **Versões**: inclua versão quando relevante

```
# Bom
soil_fauna_data_2024-01-15_v1.0.csv
metadata_species_list.json
process_darwin_core.R

# Evite
Soil Fauna Data.csv
metadata (1).json
ProcessDarwinCore-FINAL-v2.R
```

## Processo de Revisão

### O que Esperamos

1. **Verificação de qualidade**: Dados estão corretos e completos?
2. **Conformidade com padrões**: Segue Darwin Core e outros padrões?
3. **Documentação adequada**: Metadados suficientes?
4. **Licenciamento claro**: Licença apropriada especificada?
5. **Código funcional**: Scripts executam sem erros?

### Timeline

- **Resposta inicial**: 5-7 dias úteis
- **Revisão completa**: 2-4 semanas (dependendo da complexidade)
- **Feedback**: Fornecido através de comentários no PR

### Após Aprovação

1. **Merge**: Sua contribuição é integrada
2. **Crédito**: Você é adicionado como contribuidor
3. **Release**: Incluído na próxima versão
4. **DOI**: Atualizado no Zenodo

## Reconhecimento

Todas as contribuições são reconhecidas:
- Listagem no arquivo CONTRIBUTORS.md
- Menção em releases notes
- Coautoria em publicações de dados (quando aplicável)

## Dúvidas?

- **Issues**: Para discussões públicas
- **Email**: [email] para questões privadas
- **Documentação**: Consulte `/docs` para mais informações

---

Agradecemos sua contribuição para a ciência aberta e reprodutível!
