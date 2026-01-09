# Assinatura do Curador

Template de **assinatura de email** para o Curador da Coleção.

## Arquivo

**assinatura_email.html** - Template HTML para uso em clientes de email

## Estrutura da Assinatura

```
[Nome Completo], PhD
Curador da Coleção de Referência da Fauna de Solos
Instituto de Biologia do Solo (IBS)

[Logo IBS]

📧 [email]
📞 [telefone]
🌐 [website]
🔬 ORCID: [orcid-link]
```

## Personalização

Substitua os seguintes campos no arquivo HTML:

| Campo | Substituir por |
|-------|----------------|
| `[Nome Completo]` | Nome do curador |
| `[email]` | Email institucional |
| `[telefone]` | Telefone direto |
| `[website]` | URL do instituto |
| `[orcid]` | Número ORCID |
| `[orcid_url]` | Link completo do ORCID |
| `[URL_LOGO]` | URL onde logo está hospedado |

## Elementos Obrigatórios

✅ Nome completo com título acadêmico
✅ Cargo oficial (Curador...)
✅ Nome do instituto
✅ Logo do IBS
✅ Email institucional
✅ ORCID (identificador de pesquisador)

## Elementos Opcionais

- Telefone direto
- Links para publicações
- Redes sociais profissionais (ResearchGate, Google Scholar)

## Logo

Recomendações para o logo na assinatura:
- Use versão web do logo: `ibs_logo_web.png`
- Largura máxima: 150px
- Hospede em servidor confiável ou use base64

## Cores e Fonte

- Fonte: Arial, sans-serif (compatibilidade)
- Tamanho: 12px para texto principal
- Cores:
  - Nome em negrito: #333333
  - Cargo: #666666
  - Links: #228B22 (verde IBS)

## Instalação

1. Abra o arquivo `assinatura_email.html` em editor de texto
2. Substitua todos os placeholders
3. Copie todo o código HTML
4. Cole nas configurações de assinatura do seu cliente de email
5. Teste enviando email para si mesmo

## Manutenção

Atualizar quando:
- Mudança de cargo
- Nova publicação importante
- Atualização de contatos
- Mudança na identidade visual do IBS

Ver guia de instalação completo em `/templates-institucionais/assinaturas/README.md`
