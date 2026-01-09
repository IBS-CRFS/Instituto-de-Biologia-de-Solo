# Exemplo de Projeto: Silva et al. 2024 - Ecology

Este é um **exemplo de estrutura** para organização de projeto de artigo científico.

## Citação da Publicação

Silva, J., Santos, M., & Oliveira, P. (2024). Diversity patterns of soil fauna in Atlantic Forest fragments. *Ecology*, 105(3), e4123. https://doi.org/10.1002/ecy.4123

## Estrutura do Projeto

```
EXEMPLO_2024_silva_ecology/
├── README.md                   # Este arquivo
├── data/
│   ├── raw/                    # Dados brutos originais
│   │   ├── field_data.csv
│   │   ├── soil_samples.csv
│   │   └── specimen_counts.csv
│   └── processed/              # Dados processados
│       ├── community_matrix.csv
│       ├── environmental_vars.csv
│       └── diversity_metrics.csv
├── scripts/                    # Scripts de análise
│   ├── 01_data_cleaning.R
│   ├── 02_diversity_analysis.R
│   ├── 03_statistical_models.R
│   └── 04_figures_generation.R
├── results/                    # Resultados
│   ├── figures/
│   │   ├── figure1_map.pdf
│   │   ├── figure2_diversity.pdf
│   │   └── figure3_ordination.pdf
│   ├── tables/
│   │   ├── table1_sites.csv
│   │   └── table2_models.csv
│   └── supplementary/
│       └── tableS1_species_list.csv
├── docs/                       # Documentação
│   ├── methods_extended.md
│   └── analysis_notes.md
└── environment/                # Ambiente reprodutível
    ├── renv.lock
    └── sessionInfo.txt
```

## Resumo do Projeto

Este estudo investigou padrões de diversidade de fauna de solo em fragmentos de Mata Atlântica no estado de São Paulo, Brasil. Foram amostrados 20 fragmentos florestais ao longo de um gradiente de tamanho e isolamento.

### Objetivos

1. Caracterizar a composição de espécies de fauna de solo
2. Avaliar efeitos de tamanho e isolamento de fragmentos
3. Identificar grupos indicadores de qualidade ambiental

### Principais Resultados

- 150 espécies identificadas
- Riqueza correlacionada com tamanho do fragmento
- Grupos específicos sensíveis ao isolamento

## Como Reproduzir as Análises

### Requisitos

- R versão 4.3.0 ou superior
- RStudio (opcional mas recomendado)
- Pacotes R listados em `environment/renv.lock`

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo.git
   cd Instituto-de-Biologia-de-Solo/publications/EXEMPLO_2024_silva_ecology
   ```

2. **Restaure o ambiente R**
   ```r
   install.packages("renv")
   renv::restore()
   ```

3. **Execute os scripts em ordem**
   ```r
   source("scripts/01_data_cleaning.R")
   source("scripts/02_diversity_analysis.R")
   source("scripts/03_statistical_models.R")
   source("scripts/04_figures_generation.R")
   ```

4. **Verifique os resultados**
   - Figuras estarão em `results/figures/`
   - Tabelas em `results/tables/`

## Dados

### Dados Brutos

Localizados em `data/raw/`:

- **field_data.csv**: Dados de campo (datas, coordenadas, condições)
- **soil_samples.csv**: Análises de solo (pH, matéria orgânica, textura)
- **specimen_counts.csv**: Contagens de espécimes por amostra

### Dados Processados

Localizados em `data/processed/`:

- **community_matrix.csv**: Matriz de abundância espécie × sítio
- **environmental_vars.csv**: Variáveis ambientais padronizadas
- **diversity_metrics.csv**: Índices de diversidade calculados

## Scripts

1. **01_data_cleaning.R**
   - Importa dados brutos
   - Remove outliers
   - Padroniza nomes de espécies
   - Gera dados processados

2. **02_diversity_analysis.R**
   - Calcula índices de diversidade (Shannon, Simpson, riqueza)
   - Análises de rarefação
   - Curvas de acumulação de espécies

3. **03_statistical_models.R**
   - Modelos lineares generalizados
   - Modelos de efeitos mistos
   - Testes de hipóteses

4. **04_figures_generation.R**
   - Gera todas as figuras do manuscrito
   - Figuras suplementares
   - Salva em formato publicável (PDF, 300 DPI)

## Licenças

- **Dados**: CC0 1.0 Universal (domínio público)
- **Código**: MIT License
- **Manuscrito**: Copyright dos autores

## Financiamento

- FAPESP - Processo 2022/12345-6
- CNPq - Processo 123456/2022-1

## Contato

**Autor Correspondente**: João Silva  
**Email**: joao.silva@example.com  
**ORCID**: 0000-0001-2345-6789

## Data de Disponibilização

**Dados brutos**: 15 de março de 2024  
**Manuscrito aceito**: 1 de abril de 2024  
**Publicação online**: 15 de maio de 2024

---

**Nota**: Esta é uma estrutura de EXEMPLO. Substitua por seus dados e informações reais ao criar um novo projeto.
