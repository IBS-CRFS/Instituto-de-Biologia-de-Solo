# Ambiente Reprodutível

Documentação do **ambiente computacional** para reprodutibilidade das análises.

## Arquivos

### renv.lock (R)
Snapshot de todos os pacotes R usados no projeto.

**Restaurar ambiente**:
```r
install.packages("renv")
renv::restore()
```

### requirements.txt (Python)
Lista de pacotes Python com versões.

**Instalar**:
```bash
pip install -r requirements.txt
```

### sessionInfo.txt
Saída de `sessionInfo()` em R, incluindo:
- Versão do R
- Sistema operacional
- Pacotes carregados e versões
- Configurações locale

### system_info.txt
Informações do sistema:
- Sistema operacional
- Versão do SO
- Processador
- Memória RAM
- Outras ferramentas (Git, etc.)

## Gerenciamento de Ambiente

### R com renv

O `renv` cria um ambiente isolado para o projeto.

**Inicializar** (apenas primeira vez):
```r
renv::init()
```

**Snapshot** (após instalar/atualizar pacotes):
```r
renv::snapshot()
```

**Restaurar** (para reproduzir):
```r
renv::restore()
```

### Python com venv

**Criar ambiente virtual**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**Instalar dependências**:
```bash
pip install -r requirements.txt
```

**Exportar dependências**:
```bash
pip freeze > requirements.txt
```

## Documentando Seu Ambiente

### Para R

```r
# Salvar informações da sessão
writeLines(capture.output(sessionInfo()), "environment/sessionInfo.txt")

# Salvar informações do sistema
writeLines(c(
  paste("OS:", Sys.info()["sysname"], Sys.info()["release"]),
  paste("R version:", R.version.string),
  paste("Date:", Sys.Date())
), "environment/system_info.txt")
```

### Para Python

```python
import platform
import sys

with open("environment/system_info.txt", "w") as f:
    f.write(f"OS: {platform.system()} {platform.release()}\n")
    f.write(f"Python: {sys.version}\n")
    f.write(f"Platform: {platform.platform()}\n")
```

## Versões Críticas

Documente versões de software crítico:

| Software | Versão | Motivo |
|----------|--------|--------|
| R | 4.3.0 | Linguagem principal |
| RStudio | 2023.06.0 | IDE |
| QGIS | 3.28 | Análises espaciais |
| Python | 3.11.0 | Scripts auxiliares |

## Dependências do Sistema

Algumas ferramentas podem precisar de bibliotecas do sistema:

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get install libgdal-dev libproj-dev libgeos-dev
```

**Mac**:
```bash
brew install gdal proj geos
```

## Docker (Avançado)

Para máxima reprodutibilidade, considere usar Docker:

```dockerfile
FROM rocker/tidyverse:4.3.0
RUN install2.r --error \
    vegan \
    sf \
    tmap
COPY . /project
WORKDIR /project
```

## Problemas Comuns

### Pacote não instala
- Verifique versão do R/Python
- Verifique dependências do sistema
- Consulte documentação do pacote

### Resultados diferentes
- Verifique `set.seed()`
- Verifique versões de pacotes
- Verifique dados de entrada

### Erro ao restaurar renv
```r
# Limpar e tentar novamente
renv::clean()
renv::restore()
```

## Checklist de Reprodutibilidade

Antes de finalizar:

- [ ] `renv.lock` ou `requirements.txt` atualizado
- [ ] `sessionInfo.txt` salvo
- [ ] `system_info.txt` documentado
- [ ] Versões críticas documentadas
- [ ] Seeds definidos em scripts aleatórios
- [ ] Caminhos são relativos (não absolutos)
- [ ] Dependências do sistema documentadas
- [ ] Testado em máquina limpa (se possível)

## Recursos

- renv: https://rstudio.github.io/renv/
- Python venv: https://docs.python.org/3/library/venv.html
- Docker: https://www.docker.com/
- Conda: https://docs.conda.io/

Ver também:
- `/scripts/README.md` - Como executar scripts
- `/docs/templates/PROJECT_README_TEMPLATE.md` - Template de projeto
- Guia de contribuição: `/CONTRIBUTING.md`
