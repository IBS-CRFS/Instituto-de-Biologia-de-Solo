# Imagens da Coleção

Esta pasta contém imagens de alta qualidade dos espécimes da coleção.

## Estrutura

Cada espécime tem sua própria pasta, nomeada com o número de catálogo:

```
imagens/
├── IBS-0001/
│   ├── habitus_dorsal.jpg
│   ├── habitus_ventral.jpg
│   ├── detalhe_prostomio.jpg
│   └── metadata.json
├── IBS-0002/
│   ├── habitus_dorsal.jpg
│   └── metadata.json
└── ...
```

## Padrões de Nomenclatura

### Tipos de Imagem

- `habitus_dorsal.jpg`: Vista dorsal completa do espécime
- `habitus_ventral.jpg`: Vista ventral completa
- `habitus_lateral.jpg`: Vista lateral
- `detalhe_[estrutura].jpg`: Detalhes de estruturas específicas
  - Exemplos: `detalhe_prostomio.jpg`, `detalhe_clitelo.jpg`, `detalhe_cerdas.jpg`

### Requisitos Técnicos

- **Formato**: JPEG para uso geral, TIFF para arquivo
- **Resolução**: Mínimo 300 DPI
- **Tamanho**: Máximo 10 MB por arquivo
- **Barra de escala**: Obrigatória em todas as imagens
- **Fundo**: Neutro (preferencialmente branco ou preto)

## Metadados das Imagens

Cada pasta de espécime contém um arquivo `metadata.json`:

```json
{
  "catalogNumber": "IBS-0001",
  "imageDate": "2024-01-20",
  "photographer": "Maria Santos",
  "equipment": {
    "camera": "Nikon D850",
    "lens": "Micro-Nikkor 105mm f/2.8",
    "microscope": "Leica M205 C"
  },
  "settings": {
    "aperture": "f/8",
    "iso": "100",
    "magnification": "2.5x"
  },
  "copyright": "Instituto de Biologia do Solo",
  "license": "CC BY 4.0",
  "notes": "Espécime fotografado vivo antes da fixação"
}
```

## Como Adicionar Novas Imagens

1. Criar pasta com número de catálogo: `mkdir IBS-XXXX`
2. Salvar imagens seguindo nomenclatura padrão
3. Criar arquivo `metadata.json` com informações técnicas
4. Adicionar referência no arquivo Darwin Core (`occurrences.csv`)
5. Atualizar contador de imagens na estatística da coleção

## Uso e Licenciamento

As imagens são licenciadas sob **CC BY 4.0**, requerendo:
- Atribuição ao Instituto de Biologia do Solo
- Link para a licença
- Indicação de modificações (se houver)

Exemplo de citação:
```
Instituto de Biologia do Solo. (2024). Pontoscolex corethrurus (IBS-0001) 
[Fotografia]. Disponível em: https://...
Licença: CC BY 4.0
```

## Processamento de Imagens

Scripts para processamento batch estão disponíveis em `/scripts/image_processing/`:
- Redimensionamento
- Adição de barra de escala
- Geração de thumbnails
- Extração de metadados EXIF

## Integração com Sistemas Externos

As imagens são referenciadas nos registros Darwin Core através do campo `associatedMedia` e podem ser integradas com:
- GBIF (através de URLs)
- Morphobank
- Wikimedia Commons
- Zenodo

---

**Última atualização**: Janeiro 2026
