# Coleção de Referência da Fauna de Solos

Esta pasta contém a base de dados completa da **Coleção de Referência da Fauna de Solos**, organizada seguindo o padrão internacional **Darwin Core**.

## Estrutura da Coleção

```
colecao-referencia/
├── darwin-core/              # Dados da coleção no padrão Darwin Core
│   ├── occurrences.csv       # Registros de ocorrência dos espécimes
│   ├── taxonomy.csv          # Informações taxonômicas
│   ├── measurements.csv      # Medidas e características morfológicas
│   └── metadata.xml          # Metadados da coleção (EML)
├── imagens/                  # Imagens dos espécimes
│   └── [catalogNumber]/      # Organizado por número de catálogo
├── documentacao/             # Documentação da coleção
│   ├── catalogo.pdf          # Catálogo da coleção
│   ├── protocolos.md         # Protocolos de curadoria
│   └── historico.md          # Histórico da coleção
└── README.md                 # Este arquivo
```

## Dados Darwin Core

Os dados da coleção seguem o padrão **Darwin Core** mantido pela TDWG (Biodiversity Information Standards), garantindo interoperabilidade com sistemas como:

- **GBIF** (Global Biodiversity Information Facility)
- **SiBBr** (Sistema de Informação sobre a Biodiversidade Brasileira)
- **iDigBio** (Integrated Digitized Biocollections)
- **SpeciesLink**

### Arquivo: occurrences.csv

Contém registros de todos os espécimes da coleção. Campos principais:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| catalogNumber | Número de catálogo único | IBS-0001 |
| scientificName | Nome científico completo | Pontoscolex corethrurus (Müller, 1857) |
| family | Família taxonômica | Rhinodrilidae |
| order | Ordem taxonômica | Opisthopora |
| class | Classe taxonômica | Clitellata |
| phylum | Filo taxonômico | Annelida |
| kingdom | Reino taxonômico | Animalia |
| basisOfRecord | Tipo de registro | PreservedSpecimen |
| preparations | Tipo de preparação | Preserved in 70% ethanol |
| institutionCode | Código da instituição | IBS |
| collectionCode | Código da coleção | FAUNA-SOLO |
| decimalLatitude | Latitude (graus decimais) | -23.5505 |
| decimalLongitude | Longitude (graus decimais) | -46.6333 |
| geodeticDatum | Sistema de coordenadas | WGS84 |
| country | País | Brazil |
| stateProvince | Estado | São Paulo |
| municipality | Município | São Paulo |
| locality | Localidade específica | Parque Ibirapuera |
| eventDate | Data de coleta | 2024-01-15 |
| recordedBy | Coletor | João Silva |
| identifiedBy | Identificador taxonômico | Maria Santos |
| dateIdentified | Data de identificação | 2024-01-20 |
| associatedMedia | Links para imagens | https://... |
| occurrenceRemarks | Observações | Found under leaf litter |

### Arquivo: taxonomy.csv

Informações taxonômicas detalhadas, incluindo:
- Classificação completa
- Sinonímias
- Referências bibliográficas
- Status taxonômico atual

### Arquivo: measurements.csv

Medidas morfológicas e características dos espécimes:
- Comprimento, largura, peso
- Contagens (segmentos, cerdas, etc.)
- Características diagnósticas
- Seguindo padrão Darwin Core MeasurementOrFact

## Curadoria e Qualidade

### Processo de Curadoria

1. **Recebimento**: Espécime é catalogado com número único
2. **Identificação**: Identificação taxonômica por especialista
3. **Preparação**: Preservação adequada (etanol, montagem, etc.)
4. **Digitalização**: Registro fotográfico e dados morfológicos
5. **Catalogação**: Entrada no banco de dados Darwin Core
6. **Verificação**: Controle de qualidade dos dados
7. **Publicação**: Disponibilização no GBIF/SiBBr

### Níveis de Qualidade

- **Nível 1**: Dados básicos (localidade, data, preparação)
- **Nível 2**: Identificação ao nível de família/gênero
- **Nível 3**: Identificação ao nível de espécie
- **Nível 4**: Revisão por especialista + imagens de alta qualidade
- **Nível 5**: Dados moleculares disponíveis

## Acesso aos Dados

### Darwin Core Archive (DwC-A)

Os dados são disponibilizados como Darwin Core Archive, um formato padrão que inclui:
- Arquivos CSV com dados
- Arquivo XML com metadados (EML)
- Arquivo meta.xml descrevendo a estrutura

Para gerar o DwC-A:
```bash
# Usando IPT (Integrated Publishing Toolkit)
# ou ferramentas como Python/R
```

### APIs e Exportação

Os dados podem ser acessados via:
- **Exportação direta**: Arquivos CSV nesta pasta
- **GBIF**: Após publicação no IPT
- **SiBBr**: Através da rede SpeciesLink
- **API customizada**: (em desenvolvimento)

## Estatísticas da Coleção

<!-- Atualizar regularmente -->

| Métrica | Valor |
|---------|-------|
| Total de espécimes | [número] |
| Total de espécies | [número] |
| Famílias representadas | [número] |
| Período de coleta | [ano início] - [ano fim] |
| Localidades | [número] |
| Estados brasileiros | [número] |
| Espécimes com imagens | [número] |
| Espécimes georreferenciados | [número] |
| Última atualização | [data] |

## Citação da Coleção

Para citar a coleção como um todo:

```
Instituto de Biologia do Solo. (2026). Coleção de Referência da Fauna de Solos. 
[Dataset]. Disponível via GBIF.org: https://doi.org/[DOI]
```

Para citar registros específicos, use o DOI do registro ou:

```
Instituto de Biologia do Solo. (2026). [Nome da espécie] [Número de catálogo]. 
Coleção de Referência da Fauna de Solos. Occurrence dataset: https://doi.org/[DOI]
```

## Imagens

As imagens dos espécimes estão organizadas em `/imagens/[catalogNumber]/`:

- `habitus_dorsal.jpg`: Vista dorsal completa
- `habitus_ventral.jpg`: Vista ventral completa
- `habitus_lateral.jpg`: Vista lateral
- `detalhe_*.jpg`: Detalhes de estruturas diagnósticas
- `metadata.json`: Metadados da imagem (equipamento, magnificação, etc.)

### Padrões de Imagem

- Formato: JPEG (alta qualidade) ou TIFF (arquivo)
- Resolução mínima: 300 DPI
- Escala: Barra de escala incluída
- Nomenclatura: `[catalogNumber]_[tipo]_[sequencia].jpg`

## Empréstimos e Acesso Físico

Para solicitar empréstimo de material ou visita à coleção:

1. Enviar solicitação via email: [email da coleção]
2. Preencher formulário de empréstimo
3. Aguardar aprovação do curador
4. Assinar termo de responsabilidade

### Políticas de Empréstimo

- Empréstimos são feitos apenas para pesquisadores qualificados
- Prazo padrão: 6 meses (renovável)
- Material deve ser devolvido nas mesmas condições
- Citação da coleção é obrigatória em publicações

## Protocolos de Preservação

Ver arquivo `documentacao/protocolos.md` para:
- Métodos de coleta
- Técnicas de fixação e preservação
- Protocolos de etiquetagem
- Procedimentos de armazenamento
- Controle de pragas
- Monitoramento ambiental

## Integração com GBIF/SiBBr

### Publicação no GBIF

Os dados são publicados no GBIF através do IPT (Integrated Publishing Toolkit):

1. Dados exportados no formato Darwin Core Archive
2. Metadados em EML (Ecological Metadata Language)
3. Publicação via IPT institucional
4. Atribuição de DOI permanente
5. Indexação e disponibilização global

**DOI da coleção no GBIF**: [a ser atribuído]

### Publicação no SiBBr

Os dados também são compartilhados com o Sistema de Informação sobre a Biodiversidade Brasileira:

- Via rede SpeciesLink
- Sincronização automática com GBIF
- Disponibilização no Portal SiBBr

## Controle de Versão

Cada atualização da base de dados recebe uma nova versão:

- **Versão MAJOR**: Revisão taxonômica completa ou reestruturação
- **Versão MINOR**: Adição significativa de espécimes (>100)
- **Versão PATCH**: Correções e atualizações menores

Ver `CHANGELOG.md` para histórico completo de versões.

## Licenciamento

Os dados da coleção são disponibilizados sob **CC0 1.0 Universal** (domínio público), permitindo máxima reutilização. Ver arquivo `LICENSE-CC0.md` na raiz do repositório.

As imagens podem ter licenças diferentes (geralmente CC BY 4.0) - verificar metadados de cada imagem.

## Contato

**Curador da Coleção**: [Nome]  
**Email**: [email]  
**Telefone**: [telefone]  
**Endereço**: [endereço físico da coleção]

**Suporte Técnico**: [email de suporte]  
**Issues no GitHub**: [link para issues]

## Colaboradores

Agradecemos a todos que contribuíram para a coleção:
- Coletores de campo
- Taxonomistas e identificadores
- Técnicos de curadoria
- Desenvolvedores do sistema
- Agências financiadoras

## Recursos Externos

- [Darwin Core](https://dwc.tdwg.org/)
- [GBIF](https://www.gbif.org/)
- [SiBBr](https://www.sibbr.gov.br/)
- [IPT Manual](https://www.gbif.org/ipt)
- [EML Documentation](https://eml.ecoinformatics.org/)

---

**Última atualização**: Janeiro 2026
