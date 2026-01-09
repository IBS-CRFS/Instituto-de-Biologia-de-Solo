# Guia de Início Rápido

Bem-vindo ao repositório do **Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos**! Este guia ajudará você a começar rapidamente.

## 📋 Visão Geral

Este repositório contém:
- Conjuntos de dados de biodiversidade de solo
- Metadados padronizados (Darwin Core)
- Scripts e análises reprodutíveis
- Materiais suplementares de publicações científicas
- Documentação completa sobre políticas e processos

## 🚀 Início Rápido em 5 Minutos

### 1. Explorar os Dados

Navegue pelos diretórios principais:

- **`/data/`**: Conjuntos de dados brutos e processados
- **`/publications/`**: Dados organizados por publicação científica
- **`/metadata/schemas/`**: Templates e esquemas de metadados

### 2. Entender a Estrutura

Consulte o [README principal](README.md) para:
- Estrutura completa do repositório
- Padrões de metadados utilizados
- Informações sobre licenciamento
- Como citar os dados

### 3. Usar os Dados

```bash
# Clone o repositório
git clone https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo.git

# Navegue para os dados
cd Instituto-de-Biologia-de-Solo/data/
```

### 4. Citar Apropriadamente

Sempre cite os dados quando usar:

```
Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos. (2026). 
[Título do Dataset]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

Ver [CITATION.cff](CITATION.cff) para citação formal.

### 5. Contribuir

Quer adicionar dados ou melhorias? Consulte [CONTRIBUTING.md](CONTRIBUTING.md)!

## 📚 Para Diferentes Usuários

### Pesquisadores Usando os Dados

**Você quer**: Baixar e usar dados para sua pesquisa

**Comece aqui**:
1. Explore `/data/` ou `/publications/` para encontrar dados relevantes
2. Leia os metadados (arquivos `metadata.json`)
3. Verifique a licença (geralmente CC0 ou CC BY 4.0)
4. Baixe os dados
5. **Importante**: Cite apropriadamente (ver [README.md](README.md#como-citar))

**Documentos úteis**:
- [README.md](README.md) - Visão geral
- [DATA_POLICY.md](DATA_POLICY.md) - Política de dados
- [CITATION.cff](CITATION.cff) - Como citar

### Pesquisadores Contribuindo com Dados

**Você quer**: Adicionar seus dados ao repositório

**Comece aqui**:
1. Leia [CONTRIBUTING.md](CONTRIBUTING.md) - Guia completo de contribuição
2. Use os templates em `/docs/templates/`:
   - `metadata_template.json` - Para metadados gerais
   - `publication_structure_template.md` - Para estrutura de publicação
3. Prepare seus dados seguindo padrões Darwin Core (se aplicável)
4. Submeta via Pull Request

**Documentos úteis**:
- [CONTRIBUTING.md](CONTRIBUTING.md) - Como contribuir
- [DATA_POLICY.md](DATA_POLICY.md) - Políticas e padrões
- `/metadata/schemas/darwin_core_template.csv` - Template Darwin Core

### Desenvolvedores e Cientistas de Dados

**Você quer**: Trabalhar com código, scripts, APIs

**Comece aqui**:
1. Clone o repositório
2. Explore scripts em `/publications/[publicacao]/scripts/`
3. Verifique ambiente computacional (renv.lock, requirements.txt)
4. Execute análises reprodutíveis

**Documentos úteis**:
- [CONTRIBUTING.md](CONTRIBUTING.md) - Padrões de código
- `/publications/README.md` - Estrutura de código e análises
- Arquivos de ambiente em cada publicação

### Editores e Revisores de Periódicos

**Você quer**: Verificar dados e código de manuscritos

**Comece aqui**:
1. Localize a publicação em `/publications/[YYYY_autor_journal]/`
2. Leia o README da publicação
3. Verifique disponibilidade de:
   - Dados brutos e processados
   - Scripts reprodutíveis
   - Metadados completos
   - Documentação clara
4. Teste reprodutibilidade seguindo instruções no README

**O que verificar**:
- ✅ Dados completos e documentados
- ✅ Scripts executáveis e comentados
- ✅ Ambiente reprodutível (renv.lock, etc.)
- ✅ Licenças claras
- ✅ Citação apropriada

### Educadores e Estudantes

**Você quer**: Usar dados para ensino ou aprendizado

**Comece aqui**:
1. Explore dados de exemplo em `/data/`
2. Use templates para aprender boas práticas
3. Estude scripts em `/publications/` como exemplos

**Recursos educacionais**:
- Templates bem documentados em `/docs/templates/`
- Exemplos de análises reprodutíveis
- Documentação sobre padrões (Darwin Core, FAIR)

## 🔑 Conceitos Importantes

### Princípios FAIR

Nossos dados seguem princípios FAIR:
- **F**indable (Encontrável): DOIs, metadados ricos
- **A**ccessible (Acessível): Aberto, gratuito
- **I**nteroperable (Interoperável): Padrões internacionais
- **R**eusable (Reutilizável): Licenças abertas, bem documentado

### Darwin Core

Padrão internacional para dados de biodiversidade:
- Termos padronizados (scientificName, decimalLatitude, etc.)
- Interoperabilidade com GBIF, SiBBr, etc.
- Template disponível: `/metadata/schemas/darwin_core_template.csv`

### Zenodo e DOI

- **Zenodo**: Repositório permanente que arquiva cada release
- **DOI**: Identificador permanente para citação
- Integração automática: cada release → novo DOI
- Guia completo: [docs/ZENODO_INTEGRATION.md](docs/ZENODO_INTEGRATION.md)

## 📖 Documentação Completa

| Documento | Descrição |
|-----------|-----------|
| [README.md](README.md) | Visão geral completa do repositório |
| [DATA_POLICY.md](DATA_POLICY.md) | Política de dados abertos e FAIR |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir (dados, código, documentação) |
| [CITATION.cff](CITATION.cff) | Arquivo de citação formal |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [LICENSE-CC0.md](LICENSE-CC0.md) | Licença para dados factuais |
| [LICENSE-CC-BY-4.0.md](LICENSE-CC-BY-4.0.md) | Licença para dados curados |
| [docs/ZENODO_INTEGRATION.md](docs/ZENODO_INTEGRATION.md) | Guia de integração Zenodo |

## ❓ Perguntas Frequentes (FAQ)

### Posso usar os dados comercialmente?

**Sim**, dados sob CC0 ou CC BY 4.0 permitem uso comercial. CC BY requer atribuição.

### Como sei qual licença se aplica?

Verifique o arquivo `metadata.json` de cada dataset ou o README da publicação.

### Preciso pedir permissão para usar os dados?

**Não**, desde que respeite a licença (CC0 não requer nem atribuição, mas é boa prática; CC BY requer atribuição).

### Como reporto um erro nos dados?

Abra uma [Issue no GitHub](../../issues) ou envie email para [email institucional].

### Posso modificar os dados?

**Sim**, ambas licenças (CC0 e CC BY) permitem modificações. Se usar CC BY, indique que modificou.

### Como contribuo com meus dados?

Siga o guia em [CONTRIBUTING.md](CONTRIBUTING.md). Basicamente:
1. Prepare dados e metadados
2. Fork o repositório
3. Adicione seus dados seguindo estrutura padrão
4. Submeta Pull Request

### Os dados têm DOI?

Sim, cada release do repositório recebe um DOI via Zenodo. Ver badges no README principal.

### Como cito um dataset específico?

Cada dataset tem instruções de citação nos metadados. Use o CITATION.cff como base.

### Dados de espécies ameaçadas estão disponíveis?

Dados sensíveis são generalizados (coordenadas arredondadas). Isso é indicado nos metadados (campo `dataGeneralizations`).

### Como sei que versão dos dados usar?

- Para máxima reprodutibilidade: Use versão específica (tag/release)
- Para dados mais atualizados: Use versão mais recente
- Sempre cite a versão usada!

## 🛠️ Ferramentas Úteis

### Validação Darwin Core

**R:**
```r
install.packages("bdDwC")
library(bdDwC)
```

**Python:**
```python
pip install pygbif
```

### Leitura de Dados

**R:**
```r
# CSV
data <- read.csv("data/processed/occurrences.csv")

# Com metadados
library(jsonlite)
metadata <- fromJSON("metadata.json")
```

**Python:**
```python
import pandas as pd
import json

# CSV
data = pd.read_csv("data/processed/occurrences.csv")

# Metadados
with open("metadata.json") as f:
    metadata = json.load(f)
```

## 🌐 Links Externos Úteis

- **Darwin Core**: https://dwc.tdwg.org/
- **GBIF**: https://www.gbif.org/
- **Zenodo**: https://zenodo.org/
- **FAIR Principles**: https://www.go-fair.org/fair-principles/
- **SiBBr**: https://www.sibbr.gov.br/

## 📧 Contato e Suporte

- **Issues**: [GitHub Issues](../../issues) - Para perguntas, bugs, sugestões
- **Email**: [email institucional]
- **Website**: [URL do instituto]

## 🎯 Próximos Passos

Agora que você conhece o básico:

1. ✅ Explore o repositório
2. ✅ Leia a documentação relevante para seu caso
3. ✅ Use ou contribua com dados
4. ✅ Cite apropriadamente
5. ✅ Compartilhe com colegas!

---

**Última atualização**: Janeiro 2026

Dúvidas não respondidas aqui? Abra uma [Issue](../../issues)!
