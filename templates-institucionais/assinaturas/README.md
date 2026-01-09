# Assinaturas de Email

Templates de **assinaturas padronizadas** para emails institucionais do IBS.

## Estrutura

```
assinaturas/
├── curador/          # Assinatura do curador
├── equipe/           # Assinatura da equipe técnica
└── institucional/    # Assinatura genérica do IBS
```

## Tipos de Assinaturas

### 1. Curador
**Arquivo**: `curador/assinatura_email.html`

Para: Curador da coleção

Inclui:
- Nome completo + título (PhD, Dr.)
- Cargo oficial
- Logo do IBS
- Contatos completos
- ORCID link

### 2. Equipe
**Arquivo**: `equipe/assinatura_email.html`

Para: Técnicos e assistentes de pesquisa

Inclui:
- Nome completo
- Cargo/função
- Logo do IBS
- Contatos do instituto

### 3. Institucional
**Arquivo**: `institucional/assinatura_email.html`

Para: Comunicações gerais oficiais

Inclui:
- Instituto de Biologia do Solo
- Logo
- Contatos institucionais
- Links úteis

## Formato

Todas as assinaturas são em **HTML** para melhor compatibilidade e formatação.

## Instalação

### Gmail
1. Configurações > Geral > Assinatura
2. Copie código HTML do arquivo
3. Cole na caixa de assinatura
4. Defina como padrão

### Outlook
1. Arquivo > Opções > Email > Assinaturas
2. Novo > Cole código HTML
3. Defina como padrão para novas mensagens

### Thunderbird
1. Ferramentas > Configurações de Conta
2. Escolha conta > Marque "Usar HTML"
3. Cole código HTML

## Personalização

Substitua os placeholders:
- `[SEU_NOME]`
- `[SEU_CARGO]`
- `[SEU_EMAIL]`
- `[SEU_TELEFONE]`
- `[SEU_ORCID]` (se aplicável)

## Logo

O logo na assinatura deve ser:
- Formato PNG (leve)
- Largura: 150px máximo
- Hospedado online ou anexado

## Cores

Use as cores oficiais do IBS:
- Verde: #228B22
- Terra: #8B5A2B
- Texto: #333333

## Boas Práticas

✅ **Faça**:
- Mantenha assinatura concisa
- Use logo oficial
- Inclua apenas contatos essenciais
- Teste em diferentes clientes de email

❌ **Não faça**:
- Assinaturas muito longas
- Muitas cores ou fontes
- Imagens pesadas
- Informações desnecessárias

Ver documentação completa em `/templates-institucionais/README.md`
