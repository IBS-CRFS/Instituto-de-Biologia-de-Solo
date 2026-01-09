# Guia de Integração com Zenodo

Este documento descreve como integrar este repositório GitHub com o Zenodo para arquivamento permanente e atribuição automática de DOI.

## O que é Zenodo?

[Zenodo](https://zenodo.org/) é um repositório de dados de pesquisa de acesso aberto, gratuito e de longo prazo, operado pelo CERN. Características principais:

- **Preservação permanente**: Dados arquivados são preservados indefinidamente
- **DOI gratuito**: Cada depósito recebe um DOI (Digital Object Identifier) único e permanente
- **Versionamento**: Cada versão recebe seu próprio DOI, com um DOI "conceito" que sempre aponta para a última versão
- **Descoberta**: Dados são indexados e facilmente descobertos
- **Citável**: DOIs tornam os dados formalmente citáveis
- **Integração com GitHub**: Sincronização automática de releases

## Benefícios da Integração GitHub-Zenodo

1. **Automação**: Cada release no GitHub automaticamente cria um depósito no Zenodo
2. **DOI permanente**: Cada versão recebe um DOI único
3. **Backup**: Cópia permanente independente do GitHub
4. **Citação**: Facilita citação formal dos dados
5. **Impacto**: Permite rastrear uso e impacto através de citações

## Configuração Inicial

### Passo 1: Criar Conta no Zenodo

1. Acesse [https://zenodo.org/](https://zenodo.org/)
2. Clique em "Sign up" (ou "Log in" se já tiver conta)
3. Escolha "Sign up with GitHub" para simplificar
4. Autorize Zenodo a acessar sua conta GitHub

### Passo 2: Conectar GitHub ao Zenodo

1. Faça login no Zenodo
2. Vá para [https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)
3. Clique em "Sync now" para sincronizar seus repositórios
4. Encontre `Instituto-de-Biologia-de-Solo` na lista
5. Ative o switch para "ON" ao lado do repositório

### Passo 3: Configurar Metadados no Zenodo (Opcional)

1. Clique em "Settings" ao lado do repositório
2. Configure metadados padrão:
   - **Communities**: Adicione a comunidades relevantes (ex: biodiversity, ecology)
   - **License**: Confirme licença padrão (CC BY 4.0 ou CC0)
   - **Keywords**: Adicione palavras-chave padrão
   - **Description**: Descrição padrão do repositório

## Criando um Release com DOI

### Método 1: Via Interface do GitHub

1. Vá para o repositório no GitHub
2. Clique em "Releases" (na barra lateral direita)
3. Clique em "Create a new release"
4. Preencha:
   - **Tag version**: Use semantic versioning (ex: v1.0.0)
   - **Release title**: Título descritivo (ex: "Initial Public Release")
   - **Description**: Descrição das mudanças (copie do CHANGELOG.md)
5. Clique em "Publish release"
6. Aguarde alguns minutos
7. Verifique o Zenodo - um novo depósito será criado automaticamente

### Método 2: Via Linha de Comando

```bash
# 1. Certifique-se de que tudo está commitado
git status

# 2. Atualize CHANGELOG.md com as mudanças desta versão
nano CHANGELOG.md

# 3. Commit o changelog
git add CHANGELOG.md
git commit -m "chore: update changelog for v1.0.0"

# 4. Crie uma tag anotada
git tag -a v1.0.0 -m "Release v1.0.0 - Initial public release

- Estrutura completa do repositório institucional
- Documentação completa de políticas e processos
- Templates para contribuição de dados
- Integração com padrões Darwin Core"

# 5. Push da tag para GitHub
git push origin v1.0.0

# 6. Crie o release no GitHub via gh CLI (opcional)
gh release create v1.0.0 \
  --title "v1.0.0 - Initial Public Release" \
  --notes-file release_notes.md

# 7. Verifique no Zenodo após alguns minutos
```

### Verificando o DOI

1. Acesse [https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)
2. Encontre seu repositório e clique no badge ou link do DOI
3. Verifique se os metadados estão corretos
4. Copie o DOI (formato: 10.5281/zenodo.XXXXXXX)

## Atualizando README com Badge do DOI

Após o primeiro release:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

Substitua `XXXXXXX` pelo número real do seu DOI.

## Estrutura de DOIs Versionados

Zenodo cria dois tipos de DOI:

1. **DOI Conceito**: Sempre aponta para a versão mais recente
   - Formato: `10.5281/zenodo.1234567`
   - Use este para citar o trabalho em geral

2. **DOI Versão**: Específico para cada versão
   - Formato: `10.5281/zenodo.1234568` (número diferente)
   - Use este para reprodutibilidade exata

### Exemplo de Citação

**Versão específica (recomendado para reprodutibilidade):**
```
Instituto de Biologia do Solo. (2026). Repositório de Dados - Versão 1.0.0 
(v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.1234568
```

**Sempre a mais recente (recomendado para referência geral):**
```
Instituto de Biologia do Solo. (2026). Repositório de Dados. Zenodo. 
https://doi.org/10.5281/zenodo.1234567
```

## Editando Metadados no Zenodo

Após criação do depósito, você pode editar metadados:

1. Acesse o depósito no Zenodo
2. Clique em "Edit" (canto superior direito)
3. Atualize:
   - **Title**: Título mais descritivo se necessário
   - **Authors**: Adicione colaboradores com ORCID
   - **Description**: Expanda a descrição
   - **Keywords**: Adicione palavras-chave relevantes
   - **Communities**: Vincule a comunidades científicas
   - **Related identifiers**: Adicione DOIs de publicações relacionadas
   - **License**: Confirme licença apropriada
4. Salve as mudanças

## Boas Práticas

### Antes de Criar um Release

- [ ] Atualize `CHANGELOG.md` com todas as mudanças
- [ ] Teste scripts e código
- [ ] Verifique que dados estão completos e corretos
- [ ] Revise metadados (`metadata.json`, `CITATION.cff`)
- [ ] Atualize documentação se necessário
- [ ] Faça commit de todas as mudanças

### Nomenclatura de Releases

Use **Semantic Versioning** (SemVer):

- **v1.0.0**: Primeira release pública
- **v1.1.0**: Adição de novos dados ou funcionalidades
- **v1.1.1**: Correção de bugs ou erros menores
- **v2.0.0**: Mudanças incompatíveis (reestruturação)

### Descrição de Releases

Inclua no release notes:

```markdown
# Release v1.1.0 - [Título Descritivo]

## Novos Dados
- Lista de novos conjuntos de dados adicionados

## Melhorias
- Melhorias em scripts ou documentação

## Correções
- Bugs ou erros corrigidos

## Mudanças Importantes
- Mudanças que afetam uso ou compatibilidade

## Citação
Para citar esta versão específica: [incluir citação]
```

## Integrando DOI em Publicações

Quando publicar artigos usando dados deste repositório:

### No Manuscrito

**Data Availability Statement:**
```
Os dados que suportam os achados deste estudo estão disponíveis abertamente 
no Zenodo em https://doi.org/10.5281/zenodo.XXXXXXX (versão 1.0.0).
```

**Nas Referências:**
```
Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos. 
(2026). [Título do Dataset] (v1.0.0) [Data set]. Zenodo. 
https://doi.org/10.5281/zenodo.XXXXXXX
```

### Em Materiais Suplementares

- Incluir DOI completo e versão específica
- Incluir instruções sobre como acessar os dados
- Citar licença dos dados

## Vinculando Zenodo a Publicações

No Zenodo, você pode vincular depósitos a publicações:

1. Edite o depósito no Zenodo
2. Em "Related identifiers", adicione:
   - **Relation**: "is supplemented by" ou "is cited by"
   - **Identifier**: DOI do artigo publicado
3. Isso cria link bidirecional entre dados e publicação

## Atualizações e Novas Versões

### Quando Criar Nova Versão

- Adição significativa de novos dados
- Correções importantes em dados existentes
- Atualizações de scripts ou análises
- Melhorias substanciais na documentação

### Processo

1. Faça todas as mudanças no repositório
2. Atualize `CHANGELOG.md`
3. Incremente versão seguindo SemVer
4. Crie novo release no GitHub
5. Zenodo automaticamente cria nova versão com novo DOI
6. Atualize README com novo DOI se necessário

## Comunidades no Zenodo

Considere submeter seus depósitos a comunidades relevantes:

- **Biodiversity Informatics**: Para dados de biodiversidade
- **Ecology**: Para dados ecológicos
- **Research Data**: Para dados de pesquisa em geral
- Comunidades nacionais brasileiras (se existirem)

Isso aumenta a visibilidade e descoberta dos dados.

## Monitoramento de Uso

Zenodo fornece estatísticas:

- **Views**: Número de visualizações
- **Downloads**: Número de downloads
- **Citations**: Citações via Crossref (quando disponível)

Acesse via: Dashboard > Depósito > Statistics

## Solução de Problemas

### Release não aparece no Zenodo

- Verifique se integração está ativa em Settings/GitHub
- Tente "Sync now" nas configurações do Zenodo
- Aguarde até 30 minutos
- Verifique logs em Settings/GitHub no Zenodo

### DOI não aparece

- DOI é criado só após publicação do depósito
- Pode levar alguns minutos
- Recarregue a página do depósito

### Metadados incorretos

- Edite o depósito no Zenodo
- Atualize `CITATION.cff` no GitHub para futuros releases

## Recursos Adicionais

- **Zenodo Help**: https://help.zenodo.org/
- **GitHub-Zenodo Guide**: https://guides.github.com/activities/citable-code/
- **DOI Handbook**: https://www.doi.org/hb.html
- **CITATION.cff Docs**: https://citation-file-format.github.io/

## Contato

Para problemas com integração Zenodo:
- **Zenodo Support**: https://zenodo.org/support
- **Issues deste repositório**: [GitHub Issues]

---

**Última atualização**: Janeiro 2026
