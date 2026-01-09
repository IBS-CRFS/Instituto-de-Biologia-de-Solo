# Política de Dados Abertos

## Princípios Fundamentais

O **Instituto de Biologia do Solo e Coleção de Referência da Fauna de Solos** adota os princípios **FAIR** (Findable, Accessible, Interoperable, Reusable) para gestão de dados científicos:

### Encontrável (Findable)
- Todos os conjuntos de dados recebem identificadores persistentes (DOI via Zenodo)
- Metadados ricos e padronizados facilitam a descoberta
- Dados são indexados em repositórios reconhecidos

### Acessível (Accessible)
- Dados disponibilizados em formato aberto e gratuito
- Protocolos padrão de acesso (HTTP/HTTPS, APIs quando aplicável)
- Metadados permanecem acessíveis mesmo quando dados têm restrições

### Interoperável (Interoperable)
- Uso de padrões internacionais (Darwin Core para dados de biodiversidade)
- Formatos de arquivo amplamente utilizados (CSV, JSON, XML)
- Vocabulários controlados e ontologias reconhecidas

### Reutilizável (Reusable)
- Licenças claras e abertas (CC0, CC BY 4.0)
- Documentação completa e metadados detalhados
- Proveniência dos dados bem documentada

## Compartilhamento de Dados

### Compromisso com Dados Abertos

Todos os dados produzidos pelo Instituto são compartilhados abertamente, exceto quando há impedimentos legais, éticos ou de confidencialidade. Nosso compromisso inclui:

- **Disponibilização oportuna**: Dados publicados junto com artigos ou após período de embargo justificado
- **Formato acessível**: Preferencialmente formatos não-proprietários (CSV, TXT, JSON)
- **Documentação completa**: Metadados e dicionários de dados acompanham todos os conjuntos
- **Preservação permanente**: Arquivamento em repositórios confiáveis com garantia de acesso a longo prazo

### Tipos de Dados Compartilhados

1. **Dados de ocorrência**: Registros de presença/ausência de organismos
2. **Dados taxonômicos**: Descrições, identificações, classificações
3. **Dados morfológicos**: Medidas, características, observações
4. **Dados moleculares**: Sequências genéticas, alinhamentos
5. **Dados ambientais**: Características do solo, clima, habitat
6. **Dados de coleção**: Informações sobre espécimes preservados
7. **Imagens**: Fotografias, microscopia, ilustrações científicas
8. **Scripts e código**: Análises, processamento, visualizações

## Licenciamento

### Dados Factuais (CC0 1.0)

Dados factuais brutos, observações e medições são disponibilizados sob **CC0 1.0 Universal**, dedicando-os ao domínio público:
- Registros de ocorrência
- Medições morfológicas
- Dados ambientais básicos
- Listas taxonômicas

**Justificativa**: Maximizar a reutilização e interoperabilidade, removendo barreiras legais.

### Dados com Valor Agregado (CC BY 4.0)

Conjuntos de dados que envolvem curaçãosignificativa, design experimental ou contribuição intelectual substancial usam **CC BY 4.0**:
- Bancos de dados curados
- Compilações originais
- Dados com análises agregadas
- Materiais educacionais

**Requisitos**: Atribuição apropriada ao usar estes dados.

### Código e Scripts

Scripts e código são disponibilizados sob licenças de software livre (MIT, GPL, etc.), especificadas em cada arquivo.

## Período de Embargo

### Política Geral

Preferencialmente, dados são disponibilizados imediatamente. Embargos são permitidos apenas em situações justificadas:

- **Máximo de 12 meses** após coleta/geração
- **Justificativa documentada** (ex: publicação em andamento, patentes, restrições de financiadores)
- **Data de liberação definida** e comunicada publicamente

### Após o Embargo

Todos os dados sob embargo são automaticamente liberados ao término do período, com notificação aos usuários cadastrados.

## Dados Sensíveis e Restrições

### Proteção de Espécies Ameaçadas

Coordenadas geográficas precisas de espécies ameaçadas ou vulneráveis podem ser:
- **Generalizadas** (ex: arredondadas para 0.1° ou município)
- **Restritas** mediante solicitação justificada
- **Documentadas** com explicação da restrição

### Dados de Propriedade Privada

Dados coletados em áreas privadas respeitam acordos de confidencialidade:
- Localidades específicas podem ser omitidas ou generalizadas
- Metadados indicam claramente as restrições
- Acesso mediante solicitação e aprovação do proprietário

### Dados de Terceiros

Dados obtidos de terceiros sob termos específicos:
- Licenciamento original é respeitado e documentado
- Permissões de redistribuição são verificadas
- Atribuição apropriada é mantida

## Citação e Atribuição

### Requisitos de Citação

Ao utilizar dados deste repositório, solicitamos:

1. **Citação formal**: Incluir citação completa nas referências
2. **DOI**: Usar o DOI permanente do conjunto de dados
3. **Versão**: Indicar a versão específica utilizada
4. **Reconhecimento**: Mencionar contribuições significativas em agradecimentos

### Formato de Citação

```
[Autores/Instituto]. (Ano). [Título do Dataset]. [Versão]. Zenodo. 
https://doi.org/[DOI]
```

### Rastreamento de Uso

Solicitamos que pesquisadores que utilizem nossos dados:
- Notifiquem publicações resultantes (via email ou issue no GitHub)
- Contribuam melhorias ou correções identificadas
- Compartilhem derivações que possam beneficiar a comunidade

## Qualidade e Curadoria dos Dados

### Padrões de Qualidade

Todos os dados passam por controle de qualidade incluindo:
- **Validação taxonômica**: Verificação de nomenclatura
- **Validação geográfica**: Verificação de coordenadas
- **Checagem de completude**: Campos obrigatórios preenchidos
- **Detecção de outliers**: Identificação de valores anômalos
- **Controle de duplicatas**: Remoção de registros redundantes

### Níveis de Curadoria

Os dados são classificados por nível de curadoria:

1. **Nível 0 - Bruto**: Dados originais sem processamento
2. **Nível 1 - Limpo**: Validações básicas aplicadas
3. **Nível 2 - Curado**: Revisão taxonômica e geográfica completa
4. **Nível 3 - Integrado**: Harmonizado com outros conjuntos e padrões

O nível de curadoria é indicado nos metadados de cada conjunto.

## Correções e Atualizações

### Reportar Problemas

Erros ou problemas nos dados podem ser reportados via:
- **GitHub Issues**: Para discussão pública e rastreamento
- **Email**: Para questões sensíveis
- **Pull Requests**: Para correções diretas

### Processo de Correção

1. **Verificação**: Problema é verificado pela equipe
2. **Correção**: Dados são corrigidos na fonte
3. **Versionamento**: Nova versão é criada
4. **Documentação**: Mudança registrada no CHANGELOG
5. **Notificação**: Usuários conhecidos são notificados

### Versões Anteriores

Todas as versões anteriores permanecem acessíveis via:
- Tags do Git
- Releases do GitHub
- DOIs versionados no Zenodo

## Responsabilidades

### Do Instituto

- Manter dados acessíveis e disponíveis
- Fornecer documentação clara e completa
- Responder a questões e feedback
- Preservar dados a longo prazo
- Aplicar padrões de qualidade

### Dos Usuários

- Citar apropriadamente os dados
- Respeitar termos de licenciamento
- Reportar erros identificados
- Compartilhar melhorias quando apropriado
- Usar dados de forma ética e responsável

## Conformidade Legal e Ética

### Legislação Aplicável

Este repositório está em conformidade com:
- **Lei de Acesso à Informação** (Lei 12.527/2011)
- **Marco Civil da Internet** (Lei 12.965/2014)
- **Lei Geral de Proteção de Dados - LGPD** (Lei 13.709/2018)
- **Convenção sobre Diversidade Biológica**
- **Protocolo de Nagoya** (acesso a recursos genéticos)

### Ética em Pesquisa

Dados de pesquisas com seres humanos (quando aplicável):
- Aprovação por Comitê de Ética documentada
- Consentimento informado obtido
- Dados anonimizados apropriadamente

## Arquivamento e Preservação

### Repositórios Utilizados

- **Primário**: GitHub (versionamento e colaboração)
- **Arquivamento**: Zenodo (preservação permanente, DOI)
- **Especializado**: GBIF, GenBank, etc. (quando aplicável)

### Garantias de Preservação

- **Múltiplas cópias**: Redundância em diferentes repositórios
- **Formatos abertos**: Evitando obsolescência tecnológica
- **Metadados permanentes**: Descritores persistem independentemente dos dados
- **Migração**: Plano de migração para novos formatos quando necessário

## Revisão da Política

Esta política é revisada anualmente ou quando mudanças significativas nas práticas, tecnologias ou legislação o justificarem.

**Última revisão**: Janeiro 2026  
**Próxima revisão programada**: Janeiro 2027

## Contato

Para questões sobre esta política ou dados específicos:
- **Email**: [email institucional]
- **GitHub Issues**: [link para issues]
- **Website**: [URL do instituto]

---

Esta política está em conformidade com diretrizes internacionais de dados abertos, incluindo recomendações da OCDE, UNESCO, e Comissão Europeia para ciência aberta.
