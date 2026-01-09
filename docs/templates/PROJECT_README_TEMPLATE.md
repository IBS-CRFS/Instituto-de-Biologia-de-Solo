# [Título do Projeto]: [Primeiro Autor] et al. [Ano] - [Journal]

> **Template de README para Projetos Científicos**
> 
> Substitua todo o texto entre [colchetes] com suas informações.
> Remova esta seção ao usar o template.

## Citação da Publicação

[Autor1], [Autor2], & [Autor3]. ([Ano]). [Título completo do artigo]. *[Nome do Journal]*, [Volume]([Issue]), [Páginas]. https://doi.org/[DOI]

## Informações do Projeto

- **Título**: [Título completo do projeto/artigo]
- **Autores**: [Lista de autores com afiliações]
- **Autor correspondente**: [Nome] ([email])
- **Período de coleta/pesquisa**: [Data início] - [Data fim]
- **Status**: [Publicado/Em revisão/Em preparação]
- **DOI do artigo**: https://doi.org/[DOI]
- **DOI dos dados**: https://doi.org/[DOI-ZENODO]

## Estrutura do Projeto

```
YYYY_autor_journal/
├── README.md                    # Este arquivo
├── data/
│   ├── raw/                     # Dados brutos originais (IMUTÁVEIS)
│   │   ├── [arquivo1].csv
│   │   └── [arquivo2].xlsx
│   ├── processed/               # Dados limpos e processados
│   │   ├── [matriz].csv
│   │   └── [variaveis].csv
│   └── metadata/                # Metadados do projeto
│       ├── metadata.json
│       └── data_dictionary.csv
├── scripts/                     # Scripts de análise (numerados)
│   ├── 01_data_cleaning.R
│   ├── 02_[analise].R
│   ├── 03_[modelos].R
│   └── 04_figures_generation.R
├── mapas/                       # Mapas e dados espaciais
│   ├── [mapa1].pdf
│   ├── [shapefile].shp
│   └── README.md
├── imagens-pranchas/            # Pranchas de figuras e fotos
│   ├── prancha_[tema].pdf
│   ├── fotos_campo/
│   └── fotos_laboratorio/
├── manuscritos/                 # Versões do manuscrito
│   ├── v1_submitted.docx
│   ├── v2_revised.docx
│   ├── final_accepted.pdf
│   └── supplementary_material.pdf
├── taxonomia-delta/             # Sistema DELTA (se aplicável)
│   ├── chars
│   ├── items
│   ├── specs
│   └── intkey.ink
├── results/                     # Resultados das análises
│   ├── figures/                # Figuras do manuscrito
│   │   ├── figure1_[desc].pdf
│   │   ├── figure2_[desc].pdf
│   │   └── figure3_[desc].pdf
│   ├── tables/                 # Tabelas
│   │   ├── table1_[desc].csv
│   │   └── table2_[desc].csv
│   └── supplementary/          # Material suplementar
│       └── tableS1_[desc].csv
├── docs/                        # Documentação adicional
│   ├── methods_extended.md
│   ├── analysis_notes.md
│   └── field_protocol.md
└── environment/                 # Ambiente reprodutível
    ├── renv.lock               # R packages (se usar R)
    ├── requirements.txt        # Python packages (se usar Python)
    ├── sessionInfo.txt         # Informações da sessão
    └── system_info.txt         # Sistema operacional, versões
```

## Resumo do Projeto

[Escreva aqui um parágrafo resumindo o projeto, objetivos principais e principais achados]

### Objetivos

1. [Objetivo 1]
2. [Objetivo 2]
3. [Objetivo 3]

### Principais Resultados

- [Resultado 1]
- [Resultado 2]
- [Resultado 3]

## Como Reproduzir as Análises

### Requisitos

**Software**:
- [Software 1] versão [X.Y.Z] ou superior
- [Software 2] versão [X.Y.Z] ou superior

**Pacotes R** (se aplicável):
- [pacote1] ([versão])
- [pacote2] ([versão])
- Ver `environment/renv.lock` para lista completa

**Pacotes Python** (se aplicável):
- [pacote1] ([versão])
- [pacote2] ([versão])
- Ver `environment/requirements.txt` para lista completa

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo.git
   cd Instituto-de-Biologia-de-Solo/publications/YYYY_autor_journal
   ```

2. **Restaure o ambiente** (R)
   ```r
   install.packages("renv")
   renv::restore()
   ```

   **OU** (Python)
   ```bash
   pip install -r environment/requirements.txt
   ```

3. **Execute os scripts em ordem**
   ```r
   source("scripts/01_data_cleaning.R")
   source("scripts/02_[analise].R")
   source("scripts/03_[modelos].R")
   source("scripts/04_figures_generation.R")
   ```

4. **Verifique os resultados**
   - Figuras estarão em `results/figures/`
   - Tabelas em `results/tables/`

## Dados

### Dados Brutos

Localizados em `data/raw/`:

| Arquivo | Descrição | Formato |
|---------|-----------|---------|
| [arquivo1].csv | [Descrição] | CSV, UTF-8 |
| [arquivo2].xlsx | [Descrição] | Excel |

**Origem**: [Descreva onde/como os dados foram coletados]

### Dados Processados

Localizados em `data/processed/`:

| Arquivo | Descrição | Gerado por |
|---------|-----------|------------|
| [matriz].csv | [Descrição] | scripts/01_*.R |
| [variaveis].csv | [Descrição] | scripts/01_*.R |

### Metadados

- **metadata.json**: Metadados completos do projeto (ver template JSON)
- **data_dictionary.csv**: Dicionário de dados descrevendo todas as variáveis

## Mapas e Dados Espaciais

Localizados em `mapas/`:

- [Descrição dos mapas incluídos]
- Software usado: [QGIS, ArcGIS, R, etc.]
- Sistema de coordenadas: [WGS84, SIRGAS2000, etc.]

## Imagens e Pranchas

### Pranchas de Figuras
- **prancha_[tema].pdf**: [Descrição]

### Fotografias
- `fotos_campo/`: Fotos dos sítios de coleta, habitat, processo de coleta
- `fotos_laboratorio/`: Fotos dos espécimes, estruturas diagnósticas

**Formato**: JPEG, 300 DPI  
**Nomenclatura**: `YYYY-MM-DD_local_tipo_seq.jpg`

## Manuscritos

Localizados em `manuscritos/`:

| Versão | Data | Status | Arquivo |
|--------|------|--------|---------|
| v1 | [Data] | Submetido | v1_submitted.docx |
| v2 | [Data] | Revisado | v2_revised.docx |
| Final | [Data] | Aceito | final_accepted.pdf |

**Material Suplementar**: supplementary_material.pdf

## Taxonomia DELTA

[Se aplicável]

Sistema DELTA para descrições taxonômicas padronizadas:

- **chars**: [N] caracteres morfológicos codificados
- **items**: [N] táxons descritos
- **intkey.ink**: Chave interativa de identificação

**Como usar**:
```bash
delta intkey.ink     # Gerar descrições
intkey intkey.ink    # Chave interativa
```

**Referência**: https://www.delta-intkey.com/

## Scripts

| Script | Descrição | Entrada | Saída |
|--------|-----------|---------|-------|
| 01_data_cleaning.R | [Desc] | data/raw/* | data/processed/* |
| 02_[analise].R | [Desc] | data/processed/* | results/* |
| 03_[modelos].R | [Desc] | data/processed/* | results/* |
| 04_figures_generation.R | [Desc] | results/* | results/figures/* |

## Resultados

### Figuras do Manuscrito

| Figura | Arquivo | Descrição |
|--------|---------|-----------|
| Figura 1 | figure1_[desc].pdf | [Descrição] |
| Figura 2 | figure2_[desc].pdf | [Descrição] |
| Figura 3 | figure3_[desc].pdf | [Descrição] |

### Tabelas

| Tabela | Arquivo | Descrição |
|--------|---------|-----------|
| Tabela 1 | table1_[desc].csv | [Descrição] |
| Tabela 2 | table2_[desc].csv | [Descrição] |

## Licenciamento

- **Dados**: [CC0 1.0 Universal (domínio público) / CC BY 4.0]
- **Código**: [MIT License / GPL-3.0 / outro]
- **Manuscrito**: Copyright dos autores
- **Figuras**: [CC BY 4.0 / outra licença]

Ver arquivos de licença:
- `/LICENSE-CC0.md`
- `/LICENSE-CC-BY-4.0.md`

## Financiamento

- [Agência 1] - Processo [número]
- [Agência 2] - Processo [número]
- [Bolsas]: [Tipo] - [Agência] - [Beneficiário]

## Agradecimentos

[Agradecimentos a colaboradores, instituições, proprietários de áreas, etc.]

## Contato

**Autor Correspondente**: [Nome]  
**Email**: [email]  
**ORCID**: [0000-0000-0000-0000]  
**Instituição**: [Nome da instituição]

## Data de Disponibilização

- **Dados brutos**: [Data]
- **Manuscrito submetido**: [Data]
- **Manuscrito aceito**: [Data]
- **Publicação online**: [Data]
- **Dados processados**: [Data]

## Referências

Se o projeto usa dados ou métodos de outros trabalhos, cite aqui:

1. [Referência 1]
2. [Referência 2]
3. [Referência 3]

## Changelog do Projeto

### [Versão] - [Data]
- [Mudança 1]
- [Mudança 2]

## Notas Adicionais

[Qualquer informação adicional relevante que não se encaixe nas seções acima]

---

**Última atualização**: [Data]  
**Versão**: [X.Y.Z]

---

## Checklist de Qualidade

Antes de publicar, verifique:

- [ ] Todos os dados brutos estão em `/data/raw/`
- [ ] Scripts executam sem erros
- [ ] Metadados completos incluídos
- [ ] README está completo e atualizado
- [ ] Licenças estão especificadas
- [ ] Figuras em alta qualidade (300 DPI mínimo)
- [ ] Ambiente reprodutível documentado
- [ ] Contatos e afiliações corretos
- [ ] DOI atribuído (Zenodo, Dryad, etc.)
- [ ] Código de revisores/comentários removido
- [ ] Dados sensíveis removidos ou anonimizados
