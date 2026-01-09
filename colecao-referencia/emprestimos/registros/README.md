# Registros de Empréstimos

Esta pasta contém os **registros centrais** de todos os empréstimos da coleção.

## Arquivos Principais

### emprestimos.csv
Planilha central com todos os empréstimos ativos e histórico recente.

**Campos**:
| Campo | Descrição |
|-------|-----------|
| loan_id | ID único (ex: LOAN-2024-001) |
| catalog_numbers | Números de catálogo emprestados |
| borrower_name | Nome do pesquisador |
| borrower_institution | Instituição |
| borrower_email | Email de contato |
| request_date | Data da solicitação |
| approval_date | Data de aprovação |
| sent_date | Data de envio |
| due_date | Data prevista de retorno |
| return_date | Data real de retorno |
| status | Status atual |
| purpose | Finalidade científica |
| tracking_number | Número de rastreio |
| notes | Observações |

### historico_emprestimos.csv
Arquivo permanente com todos os empréstimos concluídos.

## Status Possíveis

- `pending`: Aguardando análise
- `approved`: Aprovado, aguardando envio
- `active`: Empréstimo ativo
- `extended`: Prazo prorrogado
- `overdue`: Atrasado
- `returned`: Devolvido
- `cancelled`: Cancelado
- `denied`: Negado

## Atualização

- Atualizar status a cada mudança
- Revisar semanalmente empréstimos ativos
- Alertar sobre prazos próximos ao vencimento
- Arquivar empréstimos concluídos no histórico

## Relatórios

Gerar relatórios:
- **Mensal**: Estatísticas de empréstimos
- **Trimestral**: Análise de tendências
- **Anual**: Relatório institucional

Scripts disponíveis em: `/scripts/emprestimos/`

## Backup

- Backup diário automático
- Manter 3 versões anteriores
- Cópia em nuvem segura

Ver documentação completa em `/colecao-referencia/emprestimos/README.md`
