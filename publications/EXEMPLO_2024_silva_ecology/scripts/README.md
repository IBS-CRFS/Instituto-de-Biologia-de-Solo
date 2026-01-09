# Scripts de Análise

Scripts numerados para **processamento e análise** dos dados do projeto.

## Organização

Scripts devem ser numerados na ordem de execução:

```
scripts/
├── 01_data_cleaning.R        # Limpeza de dados
├── 02_diversity_analysis.R   # Análise de diversidade
├── 03_statistical_models.R   # Modelos estatísticos
├── 04_figures_generation.R   # Geração de figuras
└── README.md                 # Este arquivo
```

## Convenções

### Nomenclatura
```
NN_descricao_curta.extensao

Onde:
- NN = Número de 01 a 99
- descricao_curta = Nome descritivo (snake_case)
- extensao = R, py, sh, etc.
```

### Cabeçalho Padrão

Todos os scripts devem iniciar com:

```r
# ==============================================================================
# Título: [Nome descritivo do script]
# Projeto: Silva et al. 2024 - Ecology
# Autor: [Seu nome]
# Data: [YYYY-MM-DD]
# Descrição: [O que este script faz]
# Entrada: [Arquivos de entrada]
# Saída: [Arquivos de saída]
# ==============================================================================
```

## Fluxo de Trabalho

### 01_data_cleaning.R
**Objetivo**: Limpar e padronizar dados brutos

- **Lê**: `data/raw/*.csv`
- **Gera**: `data/processed/*.csv`
- **Faz**:
  - Remove outliers
  - Padroniza nomes de espécies
  - Trata valores ausentes
  - Valida dados

### 02_diversity_analysis.R
**Objetivo**: Calcular índices de diversidade

- **Lê**: `data/processed/community_matrix.csv`
- **Gera**: `data/processed/diversity_metrics.csv`
- **Faz**:
  - Índices de Shannon, Simpson, riqueza
  - Curvas de rarefação
  - Curvas de acumulação

### 03_statistical_models.R
**Objetivo**: Ajustar modelos estatísticos

- **Lê**: `data/processed/*.csv`
- **Gera**: `results/tables/model_results.csv`
- **Faz**:
  - GLMs, GLMMs
  - Testes de hipóteses
  - Seleção de modelos

### 04_figures_generation.R
**Objetivo**: Gerar todas as figuras

- **Lê**: `results/tables/*.csv`
- **Gera**: `results/figures/*.pdf`
- **Faz**:
  - Figuras do manuscrito (300 DPI)
  - Figuras suplementares
  - Exportação em PDF e PNG

## Boas Práticas

### Reprodutibilidade

✅ **Faça**:
- Use caminhos relativos
- Documente dependências
- Use `set.seed()` para aleatoriedade
- Comente código complexo
- Salve sessionInfo()

❌ **Evite**:
- Caminhos absolutos
- `setwd()` hardcoded
- Instalar pacotes no script
- Código sem comentários

### Exemplo (R)

```r
# Carregar pacotes
library(tidyverse)
library(vegan)

# Definir seed para reprodutibilidade
set.seed(123)

# Ler dados (caminho relativo)
data <- read_csv("../data/processed/community_matrix.csv")

# Análise
results <- diversity(data, index = "shannon")

# Salvar resultados
write_csv(results, "../results/tables/diversity.csv")

# Salvar informações da sessão
writeLines(capture.output(sessionInfo()), 
           "../environment/sessionInfo.txt")
```

## Dependências

### R
Listar pacotes usados:
```r
# Pacotes necessários:
# - tidyverse (2.0.0)
# - vegan (2.6-4)
# - ggplot2 (3.4.0)

# Instalar (se necessário):
# install.packages(c("tidyverse", "vegan", "ggplot2"))
```

### Python
Listar em `requirements.txt`:
```
pandas==2.0.0
numpy==1.24.0
matplotlib==3.7.0
```

## Execução

### Executar Todos os Scripts

**R**:
```r
source("01_data_cleaning.R")
source("02_diversity_analysis.R")
source("03_statistical_models.R")
source("04_figures_generation.R")
```

**Bash**:
```bash
Rscript 01_data_cleaning.R
Rscript 02_diversity_analysis.R
Rscript 03_statistical_models.R
Rscript 04_figures_generation.R
```

### Scripts Individuais

Execute apenas o script necessário, mas certifique-se que as dependências (scripts anteriores) foram executadas.

## Debugging

Se encontrar erros:
1. Verifique se dados de entrada existem
2. Verifique se pacotes estão instalados
3. Leia mensagens de erro
4. Verifique versões de pacotes
5. Consulte `environment/sessionInfo.txt` do projeto original

## Versionamento

Scripts são versionados via Git. Para mudanças maiores:
- Documente em comentários
- Atualize header com data
- Descreva mudanças no commit

Ver também:
- `/data/README.md` - Estrutura de dados
- `/environment/README.md` - Ambiente reprodutível
- `/docs/templates/PROJECT_README_TEMPLATE.md` - Template de projeto
