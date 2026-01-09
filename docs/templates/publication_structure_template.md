# Template para Estrutura de Publicação

Este template define a estrutura padrão para organizar dados e materiais relacionados a publicações científicas.

## Estrutura de Diretórios

```
publications/
└── YYYY_primeiro-autor_journal-abreviado/
    ├── README.md
    ├── metadata.json
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── scripts/
    │   ├── 01_data_preparation.R
    │   ├── 02_analysis.R
    │   └── 03_visualization.R
    ├── results/
    │   ├── figures/
    │   ├── tables/
    │   └── supplementary/
    ├── docs/
    │   └── methods_extended.md
    └── environment/
        ├── renv.lock (para R)
        ├── requirements.txt (para Python)
        └── environment.yml (para Conda)
```

## Nomenclatura

**Formato**: `YYYY_primeiro-autor_journal-abreviado`

**Exemplos**:
- `2024_silva_ecology`
- `2023_santos_nature-ecology-evolution`
- `2024_oliveira_soil-biology-biochemistry`

## Conteúdo dos Arquivos

### README.md

```markdown
# [Título da Publicação]

## Citação

[Citação completa da publicação]

DOI: [DOI da publicação]

## Autores

- Autor 1 (ORCID)
- Autor 2 (ORCID)
- ...

## Resumo

[Resumo da publicação]

## Dados

### Descrição dos Dados

Descrição dos conjuntos de dados incluídos e sua relevância para a publicação.

### Arquivos de Dados

- `data/raw/`: Dados originais não processados
- `data/processed/`: Dados processados e análises

## Scripts

Descrição dos scripts incluídos e ordem de execução:

1. `01_data_preparation.R`: Limpeza e preparação dos dados
2. `02_analysis.R`: Análises estatísticas principais
3. `03_visualization.R`: Geração de figuras

## Reprodutibilidade

### Ambiente Computacional

- R version: [versão]
- RStudio version: [versão] (opcional)
- Sistema Operacional: [sistema]

### Pacotes Requeridos

Lista de pacotes e versões (veja `renv.lock` ou `requirements.txt`)

### Como Reproduzir

```bash
# Passo 1: Configurar ambiente
Rscript -e "renv::restore()"

# Passo 2: Executar scripts em ordem
Rscript scripts/01_data_preparation.R
Rscript scripts/02_analysis.R
Rscript scripts/03_visualization.R
```

## Resultados

- Figuras principais estão em `results/figures/`
- Tabelas em `results/tables/`
- Material suplementar em `results/supplementary/`

## Licença

Dados: [CC0/CC BY 4.0]
Código: [MIT/GPL/etc]

## Contato

[Nome do autor correspondente]
[Email]
[ORCID]

## Agradecimentos

[Financiamento e agradecimentos]
```

### metadata.json

```json
{
  "publication": {
    "title": "",
    "authors": [""],
    "journal": "",
    "year": 2024,
    "volume": "",
    "issue": "",
    "pages": "",
    "doi": "",
    "abstract": ""
  },
  "data": {
    "title": "",
    "description": "",
    "license": "CC0-1.0",
    "format": ["CSV", "R"],
    "size_mb": 0,
    "records": 0
  },
  "code": {
    "language": ["R"],
    "license": "MIT",
    "repository": "https://github.com/..."
  },
  "keywords": [],
  "related_datasets": []
}
```

## Checklist de Publicação

Antes de publicar, verifique:

### Dados
- [ ] Dados brutos incluídos em `data/raw/`
- [ ] Dados processados em `data/processed/`
- [ ] Metadados completos (metadata.json)
- [ ] Dicionário de dados criado
- [ ] Licença claramente especificada
- [ ] Dados sensíveis protegidos ou generalizados

### Código
- [ ] Scripts organizados e numerados
- [ ] Comentários adequados no código
- [ ] Dependências documentadas
- [ ] Ambiente reprodutível (renv.lock, requirements.txt, etc.)
- [ ] Caminhos relativos (não absolutos)
- [ ] Código testado em ambiente limpo

### Documentação
- [ ] README.md completo
- [ ] Instruções de reprodução claras
- [ ] Métodos estendidos documentados
- [ ] Citação correta da publicação
- [ ] Autores com ORCID

### Reprodutibilidade
- [ ] Versões de software documentadas
- [ ] Seed/random state especificado quando aplicável
- [ ] Tempo de execução estimado mencionado
- [ ] Requisitos de hardware (se relevantes)

### Integração
- [ ] DOI da publicação incluído
- [ ] Link para repositório de dados (Zenodo)
- [ ] Referência cruzada entre artigo e dados
- [ ] Citação dos dados no artigo

## Exemplo Completo

Ver: `/publications/EXEMPLO_2024_smith_ecology/` para um exemplo funcional completo.

## Ferramentas Úteis

### R
```r
# Criar ambiente reprodutível
renv::init()
renv::snapshot()

# Gerar relatório de sessão
sessionInfo()
```

### Python
```bash
# Criar requirements.txt
pip freeze > requirements.txt

# Criar environment.yml (conda)
conda env export > environment.yml
```

## Versionamento

- Use semantic versioning para updates significativos
- Documente mudanças no README.md
- Crie releases no GitHub para versões importantes

## Contato

Para questões sobre este template:
- Issues: [GitHub Issues]
- Email: [email institucional]
