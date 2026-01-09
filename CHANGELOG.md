# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Adicionado
- Pasta `/colecao-referencia` com estrutura completa para base de dados da coleção
  - Subpasta `darwin-core/` com arquivo de exemplo de ocorrências no padrão Darwin Core
  - Subpasta `imagens/` para armazenamento de fotos dos espécimes
  - Subpasta `documentacao/` para protocolos, catálogo e histórico
  - README detalhado com instruções de uso, curadoria e integração GBIF/SiBBr
- Exemplo completo de estrutura de projeto em `/publications/EXEMPLO_2024_silva_ecology`
  - Estrutura padronizada com data/scripts/results/docs/environment
  - README demonstrando como organizar projeto de artigo científico
  - Pastas vazias com .gitkeep para manter estrutura
- Links de acesso rápido no README principal para:
  - Coleção de Referência
  - Exemplo de projeto
  - Templates Darwin Core e de projeto

### Modificado
- README.md principal atualizado com:
  - Estrutura expandida incluindo pasta `colecao-referencia/`
  - Destaque para separação de projetos por artigo científico
  - Seção de acesso rápido para navegação facilitada
  - Emojis para melhor identificação visual das seções

### Planejado
- Integração com GBIF para sincronização automática de dados de ocorrência
- API REST para acesso programático aos dados
- Dashboard interativo para visualização de dados
- Sistema de validação automática de dados Darwin Core

## [1.0.0] - 2026-01-09

### Adicionado
- Estrutura inicial do repositório institucional
- README.md institucional completo com informações sobre:
  - Missão e objetivos do Instituto
  - Estrutura organizacional do repositório
  - Padrões de metadados (Darwin Core)
  - Instruções de citação e licenciamento
  - Integração com Zenodo para DOI
  - Guias de reprodutibilidade
- DATA_POLICY.md - Política completa de dados abertos incluindo:
  - Princípios FAIR
  - Diretrizes de licenciamento (CC0/CC BY 4.0)
  - Gestão de dados sensíveis
  - Processo de embargo
  - Padrões de qualidade
- CONTRIBUTING.md - Guia detalhado de contribuição com:
  - Código de conduta
  - Processo de submissão de dados
  - Padrões de código e documentação
  - Templates e checklists
  - Processo de revisão
- CITATION.cff - Arquivo de citação no formato Citation File Format
- LICENSE-CC0.md - Texto da licença Creative Commons Zero para dados factuais
- LICENSE-CC-BY-4.0.md - Texto da licença Creative Commons BY 4.0 para dados curados
- Estrutura de diretórios:
  - `/data/raw` - Para dados brutos originais
  - `/data/processed` - Para dados processados
  - `/publications` - Para materiais por publicação
  - `/metadata/schemas` - Para esquemas de metadados
  - `/docs/templates` - Para templates e modelos
- Badges no README indicando DOI e licenças
- Instruções para versionamento semântico
- Documentação sobre integração com Zenodo

### Diretrizes Estabelecidas
- Padrão Darwin Core para dados de biodiversidade
- Princípios FAIR para gestão de dados
- Ciência aberta e reprodutível como pilares fundamentais
- Múltiplas licenças apropriadas para diferentes tipos de conteúdo

## Tipos de Mudanças

Este changelog utiliza as seguintes categorias:

- **Adicionado** (`Added`): para novas funcionalidades
- **Modificado** (`Changed`): para mudanças em funcionalidades existentes
- **Descontinuado** (`Deprecated`): para funcionalidades que serão removidas
- **Removido** (`Removed`): para funcionalidades removidas
- **Corrigido** (`Fixed`): para correções de bugs
- **Segurança** (`Security`): para correções de vulnerabilidades

## Versionamento

### Formato de Versão: MAJOR.MINOR.PATCH

- **MAJOR**: Mudanças incompatíveis na API ou estrutura
  - Exemplo: Reestruturação completa de diretórios, mudança de padrões de metadados
- **MINOR**: Adição de funcionalidade de forma retrocompatível
  - Exemplo: Novos conjuntos de dados, novos scripts, documentação expandida
- **PATCH**: Correções de bugs e pequenas atualizações
  - Exemplo: Correção de erros em dados, typos na documentação, pequenas melhorias

### Quando Criar uma Nova Versão?

#### MAJOR (X.0.0)
- Mudança de padrão de metadados (ex: Darwin Core para outro padrão)
- Reestruturação significativa de diretórios que quebra links existentes
- Remoção de datasets ou funcionalidades importantes
- Mudanças que exigem ação dos usuários para continuar usando o repositório

#### MINOR (0.X.0)
- Adição de novos conjuntos de dados
- Novos scripts de análise
- Expansão significativa da documentação
- Novos templates ou ferramentas
- Atualização de dados existentes com novos registros

#### PATCH (0.0.X)
- Correção de erros em dados (typos, coordenadas incorretas, etc.)
- Correção de bugs em scripts
- Melhorias na documentação sem adição de conteúdo substancial
- Atualizações de metadados para melhor conformidade
- Correções de links quebrados

## Como Documentar Mudanças

Ao fazer mudanças, siga este formato:

```markdown
## [Versão] - YYYY-MM-DD

### Adicionado
- Descrição clara do que foi adicionado
- Use bullet points
- Seja específico mas conciso

### Modificado
- O que mudou
- Por que mudou (se relevante)

### Corrigido
- Que problema foi resolvido
- Como foi resolvido (se relevante)
```

### Exemplo de Entrada

```markdown
## [1.1.0] - 2026-03-15

### Adicionado
- Dataset de fauna de solo da Mata Atlântica (50 novos registros)
- Script R para validação automática de coordenadas geográficas
- Tutorial sobre como usar Darwin Core Archive
- Template para metadados de imagens

### Modificado
- Atualização do README com exemplos de análises
- Melhoria na estrutura de diretórios em /publications
- Documentação expandida sobre processo de curadoria

### Corrigido
- Correção de 12 coordenadas geográficas no dataset XYZ
- Bug no script de conversão CSV para Darwin Core
- Links quebrados na documentação de metadados
```

## Releases e DOI

Cada release marcada com tag no GitHub automaticamente:
1. Gera um DOI permanente no Zenodo
2. Arquiva uma cópia estática do repositório
3. Torna-se citável de forma única

### Como Criar um Release

```bash
# 1. Atualize este CHANGELOG.md
# 2. Commit as mudanças
git add CHANGELOG.md
git commit -m "chore: prepare release v1.1.0"

# 3. Crie uma tag anotada
git tag -a v1.1.0 -m "Release v1.1.0 - Adição de dataset Mata Atlântica"

# 4. Push da tag
git push origin v1.1.0

# 5. Crie o release no GitHub
# 6. Zenodo automaticamente criará um DOI
```

## Política de Suporte

- **Versão atual**: Totalmente suportada, recebe todas as atualizações
- **Versão anterior (MAJOR)**: Correções críticas de segurança por 6 meses
- **Versões antigas**: Mantidas no Zenodo mas sem suporte ativo

## Migrações

Quando houver mudanças incompatíveis (MAJOR version), forneceremos:
- Guia de migração detalhado
- Scripts de conversão quando possível
- Período de transição com suporte a ambas versões
- Notificação prévia de pelo menos 3 meses

## Histórico Antes de 1.0.0

Não há histórico anterior. Este é o primeiro release do repositório institucional.

---

**Nota**: Este arquivo deve ser atualizado em toda mudança significativa, antes de criar um release.

## Links

- [Repositório GitHub](https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo)
- [Releases](https://github.com/nathanufpb/Instituto-de-Biologia-de-Solo/releases)
- [Zenodo](https://zenodo.org/XXXXXXX)
- [Como manter um Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
- [Semantic Versioning](https://semver.org/lang/pt-BR/)
