# Templates Institucionais

Esta pasta contém os modelos visuais e documentais oficiais do **Instituto de Biologia do Solo (IBS)** e da **Coleção de Referência da Fauna de Solos**.

## Estrutura

```
templates-institucionais/
├── logotipos/                 # Logotipos oficiais do IBS
│   ├── principal/            # Logo principal em várias resoluções
│   ├── variantes/            # Variantes do logo (monocromático, etc.)
│   └── uso/                  # Guia de uso da marca
├── cartas/                   # Modelos de cartas oficiais
│   ├── timbradas/           # Papéis timbrados
│   ├── solicitacoes/        # Templates de solicitação
│   ├── respostas/           # Templates de resposta
│   └── administrativas/     # Cartas administrativas
└── assinaturas/             # Assinaturas para email
    ├── curador/            # Assinatura do curador
    ├── equipe/             # Assinaturas da equipe
    └── institucional/      # Assinatura padrão IBS
```

## Logotipos (`/logotipos`)

### Logo Principal

Pasta `principal/` contém o logotipo oficial do IBS em múltiplos formatos:

| Arquivo | Formato | Uso | Resolução |
|---------|---------|-----|-----------|
| `ibs_logo.svg` | SVG (vetorial) | Impressão, design | Escalável |
| `ibs_logo_hires.png` | PNG | Impressão | 300 DPI |
| `ibs_logo_web.png` | PNG | Web, apresentações | 150 DPI |
| `ibs_logo_thumb.png` | PNG | Ícones, miniatura | 72 DPI |
| `ibs_logo.eps` | EPS | Gráfica profissional | Vetorial |
| `ibs_logo.pdf` | PDF | Documentos | Vetorial |

**Dimensões padrão**: Largura 2000px (alta resolução)

### Variantes

Pasta `variantes/` contém versões alternativas:

1. **Monocromático**
   - `ibs_logo_mono_black.png`: Preto sobre transparente
   - `ibs_logo_mono_white.png`: Branco sobre transparente
   - Uso: Impressões em preto e branco, carimbos

2. **Versões Simplificadas**
   - `ibs_logo_simple.png`: Versão simplificada para uso pequeno
   - `ibs_logo_icon.png`: Apenas ícone, sem texto (64x64, 128x128, 256x256)

3. **Cores Alternativas**
   - Para fundos coloridos ou aplicações especiais
   - Seguir manual de identidade visual

### Guia de Uso (`uso/`)

**Arquivo**: `manual_identidade_visual.pdf`

Contém diretrizes para:
- Espaçamento mínimo ao redor do logo
- Cores oficiais (RGB, CMYK, Pantone, HEX)
- Tamanhos mínimos de aplicação
- Fundos permitidos e não permitidos
- Usos incorretos (o que NÃO fazer)
- Exemplos de aplicação

#### Cores Oficiais do IBS

```
Cor Primária (Verde IBS):
- RGB: 34, 139, 34
- HEX: #228B22
- CMYK: 76, 0, 76, 45
- Pantone: 355 C

Cor Secundária (Terra):
- RGB: 139, 90, 43
- HEX: #8B5A2B
- CMYK: 0, 35, 69, 45
- Pantone: 4635 C

Cor de Texto:
- RGB: 51, 51, 51
- HEX: #333333
```

### Download e Uso

Para obter os logotipos:
1. Acesse a pasta apropriada
2. Escolha o formato adequado ao seu uso
3. Leia o manual de identidade visual
4. Use respeitando as diretrizes

**Permissões**:
- ✅ Uso em publicações científicas citando IBS
- ✅ Apresentações acadêmicas
- ✅ Material institucional aprovado
- ✅ Website oficial e materiais de divulgação autorizados
- ❌ Uso comercial não autorizado
- ❌ Modificação do logo sem autorização
- ❌ Uso que implique endosso não dado

## Cartas (`/cartas`)

### Papel Timbrado

Pasta `timbradas/` contém templates de papel timbrado:

| Arquivo | Formato | Uso |
|---------|---------|-----|
| `papel_timbrado_ibs.docx` | Word | Edição fácil |
| `papel_timbrado_ibs.odt` | LibreOffice | Software livre |
| `papel_timbrado_ibs.pdf` | PDF | Visualização/impressão |

**Elementos incluídos**:
- Logotipo IBS (topo esquerdo)
- Nome completo da instituição
- Endereço completo
- Telefone, email, website
- Rodapé com informações adicionais

### Templates de Solicitação

Pasta `solicitacoes/` contém modelos para solicitar:

1. **Solicitação de Empréstimo** (`solicitacao_emprestimo.docx`)
   - Para pesquisadores solicitarem material
   - Campos: dados do solicitante, material, justificativa
   
2. **Solicitação de Visita** (`solicitacao_visita.docx`)
   - Para agendar visita à coleção
   - Campos: datas, propósito, necessidades

3. **Solicitação de Doação** (`solicitacao_doacao.docx`)
   - Para oferecer material à coleção
   - Campos: descrição do material, procedência

### Templates de Resposta

Pasta `respostas/` contém modelos para:

1. **Aprovação de Empréstimo** (`aprovacao_emprestimo.docx`)
   ```
   Inclui:
   - Número de referência
   - Lista de material aprovado
   - Condições do empréstimo
   - Prazo de devolução
   - Instruções de envio
   - Termo de responsabilidade
   ```

2. **Negação de Empréstimo** (`negacao_emprestimo.docx`)
   ```
   Inclui:
   - Justificativa clara
   - Alternativas possíveis
   - Sugestões
   ```

3. **Confirmação de Recebimento** (`confirmacao_recebimento.docx`)
   ```
   Confirma recebimento de:
   - Material devolvido
   - Documentação
   - Doações
   ```

4. **Cobrança de Devolução** (`cobranca_devolucao.docx`)
   ```
   Lembrete amigável de:
   - Prazo vencido ou próximo
   - Instruções de devolução
   - Contato para renovação
   ```

### Cartas Administrativas

Pasta `administrativas/` contém:

- `agradecimento.docx`: Carta de agradecimento genérica
- `convite_evento.docx`: Convite para eventos institucionais
- `certificado_deposito.docx`: Certificado de depósito de material
- `relatorio_curadoria.docx`: Template de relatório de curadoria

### Variáveis nos Templates

Todos os templates usam campos que devem ser preenchidos:

```
[DATA]
[NOME_DESTINATARIO]
[INSTITUICAO_DESTINATARIO]
[ENDERECO_DESTINATARIO]
[NUMERO_REFERENCIA]
[NOME_CURADOR]
[ASSINATURA_CURADOR]
```

## Assinaturas de Email (`/assinaturas`)

### Assinatura do Curador

Arquivo: `curador/assinatura_email.html`

```html
<!-- Exemplo de estrutura -->
<div style="font-family: Arial, sans-serif; font-size: 12px;">
  <strong>[Nome do Curador], PhD</strong><br>
  Curador da Coleção de Referência da Fauna de Solos<br>
  Instituto de Biologia do Solo (IBS)<br>
  <br>
  <img src="[URL_LOGO]" alt="IBS" width="150"><br>
  <br>
  📧 [email]<br>
  📞 [telefone]<br>
  🌐 <a href="[website]">[website]</a><br>
  🔬 ORCID: <a href="[orcid_url]">[orcid]</a>
</div>
```

### Assinatura da Equipe

Arquivo: `equipe/assinatura_email.html`

Template padrão para técnicos e assistentes de pesquisa.

### Assinatura Institucional

Arquivo: `institucional/assinatura_email.html`

Assinatura genérica para comunicações oficiais gerais.

### Como Instalar Assinatura

**Gmail**:
1. Configurações > Geral > Assinatura
2. Cole o código HTML
3. Ajuste URL do logo se hospedado externamente

**Outlook**:
1. Arquivo > Opções > Email > Assinaturas
2. Novo > Cole HTML
3. Defina como padrão

**Thunderbird**:
1. Ferramentas > Configurações de Conta
2. Escolha conta > Marque "Usar HTML"
3. Cole código

## Uso dos Templates

### Carta Oficial

1. Abra template apropriado de `/cartas`
2. Preencha campos entre colchetes
3. Revise ortografia e formatação
4. Salve com nome descritivo
5. Converta para PDF para envio formal
6. Arquive cópia em `/colecao-referencia/emprestimos/cartas-enviadas`

### Logotipo

1. Consulte manual de identidade visual
2. Escolha formato e resolução apropriados
3. Respeite espaços mínimos e cores
4. Cite IBS quando usar em publicações

## Controle de Versões

| Item | Versão Atual | Última Atualização |
|------|--------------|-------------------|
| Logo principal | v2.0 | Janeiro 2026 |
| Manual de identidade | v1.5 | Janeiro 2026 |
| Templates de cartas | v3.0 | Janeiro 2026 |
| Assinaturas email | v2.1 | Janeiro 2026 |

## Solicitações e Sugestões

Para solicitar novos templates ou sugerir melhorias:
- **Email**: design@ibs.br
- **Issues**: [GitHub Issues](../../issues)

## Direitos e Licenciamento

- **Logotipos**: © Instituto de Biologia do Solo. Todos os direitos reservados.
- **Templates de cartas**: CC BY 4.0 - Uso permitido com atribuição
- **Uso institucional**: Permitido para fins acadêmicos e científicos

---

**Responsável pela Identidade Visual**: [Nome]  
**Email**: design@ibs.br  
**Última atualização**: Janeiro 2026
