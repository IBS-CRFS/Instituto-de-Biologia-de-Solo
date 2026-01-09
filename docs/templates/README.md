# Templates e Modelos

**Templates reutilizáveis** para projetos científicos e metadados.

## Arquivos

### metadata_template.json
Template JSON completo para metadados de projetos.

**Inclui seções para**:
- Informações básicas (título, descrição, palavras-chave)
- Cobertura temporal e espacial
- Cobertura taxonômica
- Autores e contatos
- Proveniência dos dados
- Níveis de qualidade
- Licenciamento

**Como usar**:
1. Copie o arquivo
2. Preencha todos os campos aplicáveis
3. Remova seções não utilizadas
4. Valide JSON em https://jsonlint.com/
5. Inclua no diretório `/data/metadata/` do seu projeto

### publication_structure_template.md
Guia de estrutura para organizar projetos de artigos científicos.

**Descreve**:
- Organização de pastas
- Nomenclatura de arquivos
- Estrutura de dados (raw/processed)
- Scripts e análises
- Mapas e figuras
- Manuscritos
- Taxonomia
- Ambiente reprodutível

**Como usar**:
1. Leia o template completo
2. Crie as pastas recomendadas
3. Siga as convenções de nomenclatura
4. Adapte conforme necessário ao seu projeto

## Criando Seu Projeto

Para criar um novo projeto científico:

```bash
# Navegue até publications/
cd publications/

# Crie pasta com formato: YYYY_autor_journal
mkdir 2024_silva_ecology

# Copie estrutura do exemplo
cp -r EXEMPLO_2024_silva_ecology/* 2024_silva_ecology/

# Ou crie manualmente seguindo o template
```

## Templates Adicionais

### Para Projetos Científicos
Ver exemplo completo em:
`/publications/EXEMPLO_2024_silva_ecology/`

Este exemplo contém:
- README detalhado
- Estrutura completa de pastas
- Exemplos de organização
- Guias de reprodutibilidade

### Para Metadados Darwin Core
Ver template em:
`/metadata/schemas/darwin_core_template.csv`

### Para Coleção de Referência
Ver documentação em:
`/colecao-referencia/README.md`

## Boas Práticas

✅ **Faça**:
- Use templates como ponto de partida
- Adapte às necessidades do seu projeto
- Documente modificações
- Mantenha estrutura consistente

❌ **Evite**:
- Criar estruturas completamente diferentes
- Omitir metadados essenciais
- Usar nomes de arquivos não descritivos
- Misturar dados raw e processed

## Recursos

- **Exemplo completo**: `/publications/EXEMPLO_2024_silva_ecology/`
- **Guia rápido**: `/docs/QUICK_START.md`
- **Como contribuir**: `/CONTRIBUTING.md`

## Suporte

Para ajuda com templates:
- **Email**: suporte@ibs.br
- **Issues**: GitHub Issues do repositório
- **Documentação**: `/docs/README.md`

**Última atualização**: Janeiro 2026
