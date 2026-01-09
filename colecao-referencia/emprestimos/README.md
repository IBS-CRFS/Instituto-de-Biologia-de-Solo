# Empréstimos da Coleção

Esta pasta gerencia todos os empréstimos de material da Coleção de Referência da Fauna de Solos.

## Estrutura

```
emprestimos/
├── cartas-enviadas/           # Cartas e documentos enviados
├── cartas-recebidas/          # Cartas e documentos recebidos
└── registros/                 # Registro de empréstimos ativos e histórico
```

## Sistema de Empréstimos

### Processo de Empréstimo

1. **Solicitação**
   - Pesquisador envia carta formal ou email
   - Preenche formulário de empréstimo (ver `/templates-institucionais/cartas`)
   - Justifica necessidade científica

2. **Análise**
   - Curador avalia solicitação
   - Verifica disponibilidade do material
   - Confirma qualificação do solicitante

3. **Aprovação**
   - Carta de aprovação enviada
   - Termo de responsabilidade assinado
   - Condições específicas definidas

4. **Envio**
   - Material embalado adequadamente
   - Documentação completa anexada
   - Registro de envio arquivado

5. **Retorno**
   - Prazo monitorado
   - Confirmação de recebimento
   - Verificação de condições

## Cartas Enviadas (`/cartas-enviadas`)

Arquiva correspondências enviadas pelo IBS:

### Organização por Tipo

```
cartas-enviadas/
├── aprovacao/                 # Cartas aprovando empréstimos
├── negacao/                   # Cartas negando solicitações
├── cobranca/                  # Lembretes de devolução
├── confirmacao/               # Confirmações de recebimento
└── agradecimento/             # Agradecimentos por devoluções
```

### Nomenclatura de Arquivos

```
YYYY-MM-DD_tipo_instituicao_pesquisador.pdf

Exemplos:
2024-01-15_aprovacao_usp_silva.pdf
2024-02-20_cobranca_unicamp_santos.pdf
2024-03-10_confirmacao_ufrj_oliveira.pdf
```

### Conteúdo Mínimo

Toda carta enviada deve incluir:
- Número de referência do empréstimo
- Data de envio
- Instituição destinatária
- Pesquisador responsável
- Resumo do conteúdo
- Assinatura do curador

## Cartas Recebidas (`/cartas-recebidas`)

Arquiva correspondências recebidas:

### Organização

```
cartas-recebidas/
├── solicitacoes/              # Solicitações de empréstimo
├── renovacoes/                # Pedidos de renovação
├── devolucoes/                # Avisos de devolução
└── agradecimentos/            # Cartas de agradecimento
```

### Nomenclatura

```
YYYY-MM-DD_tipo_instituicao_pesquisador.pdf

Exemplos:
2024-01-10_solicitacao_usp_silva.pdf
2024-04-15_renovacao_unicamp_santos.pdf
2024-06-20_devolucao_ufrj_oliveira.pdf
```

### Processamento

1. Carta recebida é digitalizada (se física)
2. Arquivo salvo seguindo nomenclatura padrão
3. Entrada criada no registro de empréstimos
4. Resposta preparada e enviada

## Registros de Empréstimos (`/registros`)

### Arquivo Principal: `emprestimos.csv`

Planilha central com todos os empréstimos:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| loan_id | ID único do empréstimo | LOAN-2024-001 |
| catalog_numbers | Números de catálogo | IBS-0001, IBS-0002 |
| borrower_name | Nome do pesquisador | Dr. João Silva |
| borrower_institution | Instituição | Universidade de São Paulo |
| borrower_email | Email de contato | silva@usp.br |
| request_date | Data da solicitação | 2024-01-10 |
| approval_date | Data de aprovação | 2024-01-15 |
| sent_date | Data de envio | 2024-01-20 |
| due_date | Data prevista de retorno | 2024-07-20 |
| return_date | Data real de retorno | 2024-07-15 |
| status | Status atual | active/returned/overdue |
| purpose | Finalidade | Revisão taxonômica |
| shipping_method | Método de envio | Correios - Sedex |
| tracking_number | Número de rastreio | BR123456789 |
| insurance_value | Valor segurado | 5000.00 |
| conditions | Condições especiais | Fotos antes da devolução |
| notes | Observações | Material frágil |

### Arquivo de Histórico: `historico_emprestimos.csv`

Registro permanente de todos os empréstimos concluídos.

### Controle de Status

- **pending**: Solicitação recebida, aguardando análise
- **approved**: Aprovado, aguardando envio
- **active**: Material enviado, empréstimo ativo
- **extended**: Prazo prorrogado
- **overdue**: Atrasado
- **returned**: Devolvido e verificado
- **cancelled**: Cancelado
- **denied**: Negado

## Políticas de Empréstimo

### Prazo Padrão
- **6 meses** para pesquisa regular
- **12 meses** para revisões taxonômicas extensas
- Renovações possíveis mediante justificativa

### Condições Gerais

1. **Responsabilidade**
   - Pesquisador é totalmente responsável pelo material
   - Deve manter em condições adequadas
   - Comunicar imediatamente qualquer problema

2. **Uso Permitido**
   - Apenas para fins científicos especificados
   - Não pode emprestar a terceiros
   - Fotos e dados podem ser compartilhados com citação

3. **Citação Obrigatória**
   - Mencionar coleção em publicações
   - Enviar cópias de publicações resultantes
   - Incluir número de catálogo nos materiais

4. **Devolução**
   - Mesmo método de envio usado na ida
   - Embalagem adequada
   - Aviso prévio de 1 semana

### Restrições

Material NÃO é emprestado para:
- Tipos nomenclaturais (holótipos, parátipos) - apenas em casos excepcionais
- Espécimes únicos de espécies raras
- Material em processo de preparação
- Solicitantes sem qualificação demonstrada

### Custos

- **Envio**: Pago pelo solicitante (ida e volta)
- **Seguro**: Obrigatório, custo do solicitante
- **Embalagem**: Fornecida pelo IBS
- **Multas por atraso**: R$ 50/mês após prazo

## Modelo de Carta de Solicitação

Ver template em `/templates-institucionais/cartas/solicitacao_emprestimo.docx`

Deve incluir:
- Dados do solicitante (nome, ORCID, instituição)
- Material solicitado (números de catálogo)
- Finalidade científica detalhada
- Prazo estimado
- Publicações previstas
- Experiência prévia com material similar
- Condições de armazenamento disponíveis

## Modelo de Termo de Responsabilidade

Ver template em `/templates-institucionais/cartas/termo_responsabilidade.docx`

## Estatísticas de Empréstimos

Relatório gerado trimestralmente:

| Métrica | 2024 |
|---------|------|
| Solicitações recebidas | [número] |
| Empréstimos aprovados | [número] |
| Empréstimos negados | [número] |
| Empréstimos ativos | [número] |
| Devoluções no prazo | [%] |
| Devoluções atrasadas | [%] |
| Instituições atendidas | [número] |
| Países atendidos | [número] |
| Publicações resultantes | [número] |

## Digitalização e Backup

- Todas as cartas são digitalizadas
- Backup mensal em nuvem
- Cópias físicas mantidas em arquivo
- Digitalização de alta qualidade (300 DPI)

## Comunicação com Pesquisadores

### Email Padrão

- Confirmação de recebimento: 48h
- Resposta sobre aprovação: 7-14 dias
- Lembretes de devolução: 1 mês antes, 1 semana antes, no vencimento

### Contato

**Responsável por Empréstimos**: [Nome]  
**Email**: emprestimos@ibs.br  
**Telefone**: [telefone]  
**Horário**: Segunda a sexta, 9h-17h

## Integração com Sistema

Os registros de empréstimos são integrados com:
- Base de dados Darwin Core (campo `disposition`)
- Sistema de catalogação
- Calendário institucional
- Sistema de email para lembretes automáticos

## Relatórios

Scripts para gerar relatórios em `/scripts/emprestimos/`:
- `relatorio_mensal.R`: Estatísticas do mês
- `emprestimos_ativos.R`: Lista de empréstimos em andamento
- `emprestimos_atrasados.R`: Alerta de atrasos
- `publicacoes_resultantes.R`: Tracking de publicações

---

**Última atualização**: Janeiro 2026
