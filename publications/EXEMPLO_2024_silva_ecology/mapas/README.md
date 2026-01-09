# Mapas e Dados Espaciais

Mapas, shapefiles e **dados geográficos** do projeto.

## Conteúdo

### Shapefiles
- `site_locations.shp` - Pontos de coleta (lat/long)
- `fragments_boundaries.shp` - Limites dos fragmentos florestais
- `study_area.shp` - Área de estudo geral

### Mapas Finais (para publicação)
- `mapa_area_estudo.pdf` - Mapa da área de estudo
- `mapa_pontos_coleta.pdf` - Mapa com localização das coletas
- `mapa_resultados.pdf` - Mapa com resultados espacializados

## Sistema de Coordenadas

- **Sistema**: WGS84 (EPSG:4326) ou SIRGAS2000 (EPSG:4674)
- **Formato**: Graus decimais
- **Precisão**: 6 casas decimais (aprox. 10 cm)

## Software Utilizado

- **QGIS** 3.28 ou superior
- **R** com pacotes: `sf`, `tmap`, `ggplot2`, `raster`
- **ArcGIS** (se aplicável)

## Arquivos de Projeto

- `project.qgz` - Projeto QGIS
- `scripts/create_maps.R` - Script R para gerar mapas

## Camadas Base

Camadas de base utilizadas:
- OpenStreetMap
- Google Satellite
- Topografia SRTM
- Limites administrativos IBGE

## Geração de Mapas

### Usando QGIS
1. Abra `project.qgz`
2. Atualize camadas se necessário
3. Exporte mapas como PDF (300 DPI)

### Usando R
```r
library(sf)
library(tmap)

# Carregar dados
sites <- st_read("mapas/site_locations.shp")

# Criar mapa
tm_shape(sites) +
  tm_dots(size = 0.5, col = "red") +
  tm_scale_bar() +
  tm_compass()

# Salvar
tmap_save("mapas/mapa_pontos_coleta.pdf", dpi = 300)
```

## Especificações para Publicação

- **Formato**: PDF vetorial
- **Resolução**: 300 DPI mínimo
- **Cores**: RGB para online, CMYK para impressão
- **Escala**: Incluir barra de escala
- **Norte**: Incluir rosa dos ventos
- **Legenda**: Clara e autoexplicativa

## Metadados Geográficos

Para cada shapefile, incluir:
- Sistema de coordenadas
- Data de coleta
- Fonte dos dados
- Precisão/acurácia
- Método de georeferenciamento

## Dados Espaciais

Organização:
```
mapas/
├── shapefiles/
│   ├── site_locations.*
│   ├── fragments_boundaries.*
│   └── study_area.*
├── rasters/
│   ├── elevation.tif
│   └── landcover.tif
├── pdfs/
│   ├── mapa_area_estudo.pdf
│   └── mapa_pontos_coleta.pdf
└── project.qgz
```

## Licença de Dados Geográficos

Dados de base geralmente têm licenças específicas:
- OpenStreetMap: ODbL
- IBGE: Dados públicos
- Google: Verificar termos de uso

Sempre cite a fonte dos dados de base utilizados.

## Coordenadas Sensíveis

Se espécies ameaçadas ou áreas protegidas:
- Reduzir precisão das coordenadas (ex: 0.1 grau)
- Generalizar localidades
- Consultar políticas de dados sensíveis
- Ver `/DATA_POLICY.md`

Ver também:
- Scripts de geração: `/scripts/`
- Dados de coordenadas: `/data/processed/`
- Figuras do manuscrito: `/results/figures/`
