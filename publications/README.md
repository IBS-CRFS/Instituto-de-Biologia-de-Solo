# Diretório de Publicações

Este diretório organiza dados, scripts e materiais suplementares associados a publicações científicas do Instituto de Biologia do Solo.

## Estrutura

Cada publicação tem seu próprio subdiretório seguindo o padrão:

```
YYYY_primeiro-autor_journal-abreviado/
```

**Exemplos:**
- `2024_silva_ecology/`
- `2023_santos_soil-biol-biochem/`
- `2024_oliveira_nature-ecol-evol/`

## Conteúdo de Cada Publicação

### Estrutura Padrão

```
YYYY_autor_journal/
├── README.md                   # Informações da publicação
├── metadata.json               # Metadados estruturados
├── data/
│   ├── raw/                    # Dados brutos
│   └── processed/              # Dados processados
├── scripts/                    # Código para análises
│   ├── 01_preparation.R
│   ├── 02_analysis.R
│   └── 03_visualization.R
├── results/                    # Resultados
│   ├── figures/
│   ├── tables/
│   └── supplementary/
├── docs/
│   └── supplementary_methods.md
└── environment/                # Reprodutibilidade
    ├── renv.lock
    └── sessionInfo.txt
```

### Arquivo README.md da Publicação

Deve conter:

1. **Citação completa** da publicação
2. **DOI** do artigo
3. **Autores** com ORCID
4. **Resumo**
5. **Descrição dos dados** incluídos
6. **Instruções de reprodução** das análises
7. **Requisitos** de software e pacotes
8. **Licenças** de dados e código
9. **Contato** do autor correspondente

Ver template completo em: `/docs/templates/publication_structure_template.md`

## Princípios

### 1. Reprodutibilidade

Todo material deve permitir reprodução completa dos resultados:

- **Dados brutos preservados**: Sem modificações
- **Scripts completos**: Todas as análises documentadas
- **Ambiente documentado**: Versões de software e pacotes
- **Instruções claras**: Passo a passo para reproduzir

### 2. Transparência

- Métodos detalhados disponíveis
- Decisões analíticas documentadas
- Dados brutos acessíveis (quando possível)
- Código aberto e comentado

### 3. Reutilização

- Licenças permissivas (CC0/CC BY para dados)
- Formatos abertos e padrão
- Metadados completos
- Documentação clara

## Nomenclatura e Organização

### Arquivos de Dados

```
[descricao]_[tipo].[extensao]

Exemplos:
- occurrence_records.csv
- environmental_variables.csv
- species_traits.csv
- site_coordinates.csv
```

### Scripts

Numerar na ordem de execução:

```
01_[etapa].R/py
02_[etapa].R/py
03_[etapa].R/py

Exemplos:
- 01_data_cleaning.R
- 02_statistical_analysis.R
- 03_figure_generation.R
- 04_supplementary_analyses.py
```

### Figuras e Tabelas

Corresponder à numeração da publicação:

```
results/figures/
├── figure_1_species_richness.pdf
├── figure_2_ordination.pdf
└── figure_3_abundance_model.pdf

results/tables/
├── table_1_site_description.csv
├── table_2_model_results.csv
└── table_s1_complete_species_list.csv
```

## Checklist Pré-Publicação

### Dados

- [ ] Dados brutos incluídos
- [ ] Dados processados disponíveis
- [ ] Metadados completos (metadata.json)
- [ ] Dicionário de dados criado
- [ ] Dados seguem padrões (Darwin Core, etc.)
- [ ] Licença claramente especificada
- [ ] Dados sensíveis tratados apropriadamente

### Código

- [ ] Scripts organizados e numerados
- [ ] Código bem comentado
- [ ] Caminhos relativos (não absolutos)
- [ ] Dependências documentadas
- [ ] Ambiente reprodutível configurado
- [ ] Código testado em ambiente limpo
- [ ] Licença de código especificada

### Documentação

- [ ] README.md completo
- [ ] Instruções de reprodução claras
- [ ] Citação da publicação incluída
- [ ] DOI da publicação incluído (quando disponível)
- [ ] Autores com ORCID listados
- [ ] Informações de contato

### Reprodutibilidade

- [ ] Versões de software documentadas
- [ ] Pacotes e dependências listados
- [ ] Seeds/random states especificados
- [ ] Tempo de execução estimado
- [ ] Requisitos de hardware (se relevantes)
- [ ] Testado em ambiente independente

### Integração

- [ ] Link no manuscrito para este repositório
- [ ] DOI do Zenodo incluído (se aplicável)
- [ ] Data availability statement no manuscrito
- [ ] Citação dos dados no manuscrito
- [ ] README atualizado na raiz do repositório

## Exemplo de Estrutura Completa

```
2024_santos_ecology/
├── README.md
├── metadata.json
├── data/
│   ├── raw/
│   │   ├── field_collections.csv
│   │   ├── laboratory_measurements.csv
│   │   └── environmental_data.csv
│   └── processed/
│       ├── occurrence_dwc.csv
│       ├── traits_clean.csv
│       └── environmental_summary.csv
├── scripts/
│   ├── 00_setup.R
│   ├── 01_data_cleaning.R
│   ├── 02_trait_analysis.R
│   ├── 03_diversity_metrics.R
│   ├── 04_statistical_models.R
│   └── 05_figures_tables.R
├── results/
│   ├── figures/
│   │   ├── fig1_map.pdf
│   │   ├── fig2_diversity.pdf
│   │   └── fig3_models.pdf
│   ├── tables/
│   │   ├── table1_sites.csv
│   │   └── table2_models.csv
│   └── supplementary/
│       ├── figS1_rarefaction.pdf
│       ├── figS2_residuals.pdf
│       └── tableS1_species_list.csv
├── docs/
│   ├── data_dictionary.csv
│   ├── supplementary_methods.md
│   └── analysis_notes.md
└── environment/
    ├── renv.lock
    ├── sessionInfo.txt
    └── R_version.txt
```

## Ambiente Computacional

### R Projects

Usar `renv` para gestão de pacotes:

```r
# Inicializar
renv::init()

# Instalar pacotes
install.packages("vegan")
install.packages("ggplot2")

# Snapshot do ambiente
renv::snapshot()

# Para reproduzir
renv::restore()
```

Salvar informação da sessão:

```r
writeLines(capture.output(sessionInfo()), "environment/sessionInfo.txt")
```

### Python

Usar `requirements.txt` ou `environment.yml`:

**requirements.txt:**
```bash
# Gerar
pip freeze > requirements.txt

# Instalar
pip install -r requirements.txt
```

**environment.yml (conda):**
```bash
# Exportar
conda env export > environment.yml

# Criar ambiente
conda env create -f environment.yml
```

## Publicando Após Publicação do Artigo

### 1. Organizar Materiais

- Reunir todos os dados, scripts e resultados
- Seguir estrutura padrão
- Criar README completo

### 2. Adicionar ao Repositório

```bash
# Criar branch
git checkout -b publication/2024_silva_ecology

# Adicionar arquivos
git add publications/2024_silva_ecology/
git commit -m "Add: Silva et al. 2024 Ecology publication data and scripts"

# Push
git push origin publication/2024_silva_ecology
```

### 3. Criar Pull Request

- Revisar todos os arquivos
- Verificar checklist
- Solicitar revisão

### 4. Após Merge, Criar Release

```bash
# Tag
git tag -a pub-2024_silva_ecology-v1.0.0 -m "Data and code for Silva et al. 2024 Ecology"

# Push tag
git push origin pub-2024_silva_ecology-v1.0.0
```

### 5. Obter DOI do Zenodo

- Zenodo criará DOI automaticamente
- Atualizar README da publicação com DOI
- Se necessário, adicionar DOI ao manuscrito via errata

## Atualizações Pós-Publicação

Se correções forem necessárias:

1. Documentar mudanças no README da publicação
2. Criar nova versão (incrementar patch: 1.0.1)
3. Explicar correções no CHANGELOG
4. Notificar editores se afetar conclusões

## Data Availability Statement

Incluir no manuscrito:

```
Data Availability

All data and code supporting the findings of this study are available 
in the GitHub repository at https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo
under the directory publications/[YYYY_autor_journal]/. The repository is archived 
in Zenodo with DOI: [DOI]. Data are provided under [CC0/CC BY 4.0] license, 
and code under [MIT/GPL/etc] license.
```

## Licenciamento

### Dados

- **CC0 1.0**: Para dados factuais (recomendado)
- **CC BY 4.0**: Para dados curados com valor agregado

### Código

- **MIT**: Permissiva, simples
- **GPL-3.0**: Copyleft
- **Apache 2.0**: Permissiva com proteção de patentes

Especificar no cabeçalho dos scripts e no README.

## Recursos

- [Research Compendia](https://research-compendium.science/)
- [The Turing Way](https://the-turing-way.netlify.app/)
- [rOpenSci Reproducibility Guide](https://ropensci.github.io/reproducibility-guide/)
- [Software Carpentry](https://software-carpentry.org/)

## Apoio

Para ajuda com:
- **Estruturação**: Consulte templates em `/docs/templates/`
- **Reprodutibilidade**: Issues ou email
- **Licenciamento**: Ver `DATA_POLICY.md`

## Contato

- Issues: [GitHub Issues]
- Email: [email institucional]
