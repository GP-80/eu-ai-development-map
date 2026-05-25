# AI Development in the EU

Choropleth map of AI development across EU countries, ranked and styled in QGIS from a publicly available AI index dataset.

![EU AI Development Map](Europe_AI_Development.png)

## Pipeline

1. **Data wrangling** (`AI.py`) — loads and inspects the raw AI index dataset using Pandas
2. **Geocoding** (`geocoding.py`) — maps country names to coordinates using geopy and Nominatim
3. **Cartography** (`AI_EU.qgz`) — QGIS project with graduated symbology, ranked labels, pie chart inset, and inset map for small countries

## Files

| File | Description |
|---|---|
| `ai_index.csv` | Raw AI index data (source: Tortoise Media) |
| `ai_eu.csv` | Filtered EU subset |
| `ai_eu_geocoded.csv` | EU data with latitude/longitude |
| `AI_EU.qgz` | QGIS project file |
| `*.gpkg` | GeoPackage layers used in the QGIS map |

## Tools

- Python, Pandas, geopy
- QGIS
- Data: [Tortoise Media Global AI Index](https://www.tortoisemedia.com/intelligence/global-ai)
