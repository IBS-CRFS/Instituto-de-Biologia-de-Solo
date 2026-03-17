# Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos

[![DOI](https://zenodo.org/badge/DOI/10.15468/pbxmgz.svg)](https://doi.org/10.15468/pbxmgz)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19055009.svg)](https://doi.org/10.5281/zenodo.19055009)

## Sobre o Instituto

O **Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos** é dedicado ao estudo e conservação da biodiversidade edáfica, com foco na taxonomia, ecologia e conservação de organismos que habitam o solo. Nossa missão é produzir conhecimento científico de excelência, manter coleções biológicas de referência e promover práticas de ciência aberta e reprodutível.

Este repositório reúne conjuntos de dados, metadados, scripts e materiais suplementares utilizados em artigos científicos, relatórios técnicos e outros produtos acadêmicos. O objetivo é garantir **transparência**, **reprodutibilidade** e **acesso aberto** aos dados, em conformidade com os princípios FAIR (Findable, Accessible, Interoperable, Reusable) e as melhores práticas de ciência aberta.

📚 **[Guia de Início Rápido](docs/QUICK_START.md)** | 📖 [Documentação Completa](#documentação) | 🤝 [Como Contribuir](CONTRIBUTING.md)

## Estrutura do Repositório

```
.
├── colecao-referencia/            # 🔬 Coleção de Referência da Fauna de Solos
│   ├── darwin-core/               # Dados da coleção no padrão Darwin Core
│   │   ├── occurrences.csv        # Registros de espécimes
│   │   ├── taxonomy.csv           # Informações taxonômicas
│   │   └── measurements.csv       # Medidas morfológicas
│   ├── imagens/                   # Imagens dos espécimes
│   ├── documentacao/              # Protocolos e catálogo
│   └── emprestimos/               # 📬 Gestão de empréstimos
│       ├── cartas-enviadas/       # Correspondências enviadas
│       ├── cartas-recebidas/      # Correspondências recebidas
│       └── registros/             # Registro de empréstimos
├── templates-institucionais/      # 🎨 Templates Oficiais do IBS
│   ├── logotipos/                 # Logotipos institucionais
│   │   ├── principal/            # Logo principal (SVG, PNG, PDF)
│   │   └── variantes/            # Versões alternativas
│   ├── cartas/                    # Modelos de cartas oficiais
│   │   ├── timbradas/            # Papel timbrado
│   │   └── solicitacoes/         # Templates de solicitação
│   └── assinaturas/               # Assinaturas de email
├── publications/                  # 📄 Projetos por Artigo Científico
│   └── YYYY_autor_journal/        # Cada artigo em pasta separada
│       ├── data/                  # Dados específicos (raw/processed/metadata)
│       ├── scripts/               # Análises reprodutíveis
│       ├── mapas/                 # 🗺️ Mapas e dados espaciais
│       ├── imagens-pranchas/      # 📷 Pranchas e fotografias
│       ├── manuscritos/           # 📝 Versões do manuscrito
│       ├── taxonomia-delta/       # 🔬 Sistema DELTA para taxonomia
│       ├── results/               # Figuras e tabelas
│       ├── docs/                  # Documentação do projeto
│       └── environment/           # Reprodutibilidade
├── data/                          # Dados gerais do instituto
│   ├── raw/                       # Dados brutos originais (imutáveis)
│   └── processed/                 # Dados processados e análises
├── metadata/                      # Metadados e esquemas
│   └── schemas/                   # Esquemas de metadados (Darwin Core, etc.)
├── docs/                          # Documentação
│   └── templates/                 # Modelos e templates
├── CITATION.cff                   # Arquivo de citação
├── DATA_POLICY.md                 # Política de dados abertos
├── CONTRIBUTING.md                # Guia de contribuição
├── CHANGELOG.md                   # Histórico de versões
└── README.md                      # Este arquivo
```

### 🔬 Coleção de Referência

A pasta `/colecao-referencia` contém a **base de dados completa** da coleção de espécimes, organizada no **padrão Darwin Core** para máxima interoperabilidade com GBIF, SiBBr e outros sistemas internacionais. Inclui também o sistema de gestão de **empréstimos** com controle de correspondências e registros. Ver [colecao-referencia/README.md](colecao-referencia/README.md) para detalhes.

### 🎨 Templates Institucionais

A pasta `/templates-institucionais` contém todos os recursos visuais e documentais oficiais do IBS: **logotipos** em múltiplos formatos, **modelos de cartas** oficiais, e **assinaturas de email** padronizadas. Ver [templates-institucionais/README.md](templates-institucionais/README.md) para guia de uso.

### 📄 Projetos por Artigo

Cada artigo científico tem sua **própria pasta** em `/publications` com estrutura padronizada contendo dados, scripts, **mapas**, **imagens e pranchas**, **manuscritos**, **taxonomia DELTA**, resultados e documentação completa. Ver exemplo em [publications/EXEMPLO_2024_silva_ecology](publications/EXEMPLO_2024_silva_ecology) e template completo em [docs/templates/publication_structure_template.md](docs/templates/publication_structure_template.md).

## Dados e Metadados

### Padrões de Metadados

Os dados biológicos seguem o padrão **Darwin Core** (DwC), um padrão internacional para dados de biodiversidade mantido pela Biodiversity Information Standards (TDWG). Para mais informações sobre os termos Darwin Core utilizados, consulte a [documentação oficial](https://dwc.tdwg.org/terms/).

Principais termos Darwin Core utilizados:
- **Occurrence**: Registros de ocorrência de organismos
- **Taxon**: Informações taxonômicas
- **Location**: Dados de localização geográfica
- **Event**: Informações sobre eventos de coleta
- **MeasurementOrFact**: Medições e características

### Organização dos Dados

Cada conjunto de dados inclui:
- **Dados brutos**: Preservados em formato original (CSV, Excel, etc.)
- **Dados processados**: Versões limpas e padronizadas
- **Metadados**: Descrições completas seguindo padrões internacionais
- **Scripts**: Código para processamento e análises (R, Python, etc.)
- **Dicionário de dados**: Descrição de todas as variáveis

### Acesso Rápido

- 🔬 **Coleção de Referência**: Ver [colecao-referencia/README.md](colecao-referencia/README.md)
- 📬 **Gestão de Empréstimos**: Ver [colecao-referencia/emprestimos/README.md](colecao-referencia/emprestimos/README.md)
- 🎨 **Templates Institucionais**: Ver [templates-institucionais/README.md](templates-institucionais/README.md)
- 📄 **Exemplo de Projeto Completo**: Ver [publications/EXEMPLO_2024_silva_ecology/](publications/EXEMPLO_2024_silva_ecology/)
- 📋 **Template Darwin Core**: Ver [metadata/schemas/darwin_core_template.csv](metadata/schemas/darwin_core_template.csv)
- 📝 **Template de Projeto**: Ver [docs/templates/publication_structure_template.md](docs/templates/publication_structure_template.md)

## Licenciamento

Este repositório utiliza múltiplas licenças para diferentes tipos de conteúdo:

### Dados e Metadados
- **[CC0 1.0 Universal](LICENSE-CC0.md)**: Dedicação ao domínio público para dados factuais e metadados, promovendo máxima reutilização
- **[CC BY 4.0](LICENSE-CC-BY-4.0.md)**: Para conjuntos de dados com valor criativo agregado

### Código e Scripts
- Consulte os arquivos individuais para licenciamento específico

A escolha da licença para cada conjunto de dados é indicada nos respectivos arquivos de metadados.

## Como Citar

### Citação Geral do Repositório

Para citar este repositório como um todo, use o formato:

```
Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos. (YYYY). 
[Título do dataset]. Zenodo. https://doi.org/10.15468/pbxmgz
```

### Citação de Conjuntos de Dados Específicos

Cada conjunto de dados possui instruções específicas de citação em seu arquivo de metadados. Utilize o arquivo `CITATION.cff` para importar citações em gerenciadores de referências.

### Formato BibTeX

```bibtex
@dataset{instituto_biologia_solo_YYYY,
  author       = {{Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos}},
  title        = {[Título do Dataset]},
  year         = {YYYY},
  publisher    = {Zenodo},
  doi          = {10.15468/pbxmgz},
  url          = {https://doi.org/10.15468/pbxmgz}
}
```

## Versionamento e DOI

### Integração com Zenodo

Este repositório está integrado com o [Zenodo](https://zenodo.org/) para arquivamento permanente e atribuição de DOI (Digital Object Identifier). Cada release do repositório recebe automaticamente um DOI único e permanente.

### Política de Versionamento

Seguimos o **Semantic Versioning** (SemVer 2.0.0):
- **MAJOR**: Mudanças incompatíveis ou reestruturações significativas
- **MINOR**: Adição de novos dados ou funcionalidades de forma retrocompatível
- **PATCH**: Correções de erros e pequenas atualizações

Consulte o arquivo [CHANGELOG.md](CHANGELOG.md) para histórico completo de versões.

### Como Criar um Release com DOI

1. Atualize o `CHANGELOG.md` com as mudanças da versão
2. Crie uma tag de versão: `git tag -a v1.0.0 -m "Descrição da versão"`
3. Faça push da tag: `git push origin v1.0.0`
4. Crie um release no GitHub
5. O Zenodo criará automaticamente um DOI para o release

## Reprodutibilidade

### Ambiente Computacional

Cada análise inclui informações sobre o ambiente computacional utilizado:
- Versões de software (R, Python, etc.)
- Pacotes e dependências
- Sistema operacional
- Arquivos de configuração (renv.lock, requirements.txt, environment.yml, etc.)

### Workflows

Scripts de análise são organizados de forma sequencial e documentados, permitindo reprodução completa dos resultados publicados.

## Política de Dados Abertos

Este repositório adere aos princípios de dados abertos e ciência aberta. Consulte [DATA_POLICY.md](DATA_POLICY.md) para nossa política completa de:
- Compartilhamento de dados
- Privacidade e dados sensíveis
- Período de embargo (quando aplicável)
- Requisitos de citação
- Direitos e responsabilidades

## Como Contribuir

Contribuições são bem-vindas! Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes sobre:
- Como reportar problemas
- Como sugerir melhorias
- Como submeter dados
- Padrões de qualidade
- Processo de revisão

## Documentação

| Documento | Descrição |
|-----------|-----------|
| [QUICK_START.md](docs/QUICK_START.md) | Guia de início rápido (comece aqui!) |
| [DATA_POLICY.md](DATA_POLICY.md) | Política completa de dados abertos |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir com dados e código |
| [CITATION.cff](CITATION.cff) | Arquivo de citação formal |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [ZENODO_INTEGRATION.md](docs/ZENODO_INTEGRATION.md) | Guia de integração com Zenodo |
| [data/README.md](data/README.md) | Guia do diretório de dados |
| [publications/README.md](publications/README.md) | Guia do diretório de publicações |

## Contato

Para questões sobre os dados, colaborações ou mais informações:
- **Website**: [URL do instituto]
- **Email**: [email institucional]
- **Issues**: Use a aba [Issues](../../issues) deste repositório

## Agradecimentos

Agradecemos às agências de fomento, colaboradores e à comunidade científica que contribuem para a ciência aberta e reprodutível.

---

**Última atualização**: Janeiro 2026
