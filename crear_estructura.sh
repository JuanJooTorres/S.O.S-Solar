#!/usr/bin/env bash
# S.O.S Solar - Crea la estructura de carpetas del repositorio.
# Uso: bash crear_estructura.sh [nombre-carpeta-raiz]

set -e
ROOT="${1:-S.O.S-Solar}"

mkdir -p "$ROOT"/{docs,schematics/{system,inverter},pcb/inverter/{project,gerbers,renders},hardware/estructura-soporte,data/{measurements,analysis,scripts},datasheets,media/{banner,images,oscilogramas,diagramas,gifs,videos}}

# Archivos base
touch "$ROOT"/{README.md,TECHNICAL_DOCS.md,LICENSE,.gitignore}
touch "$ROOT"/docs/{guia-de-uso.md,glosario.md,manual-de-seguridad.md}
touch "$ROOT"/pcb/inverter/BOM.csv
touch "$ROOT"/hardware/lista-componentes.csv

# Mantener carpetas vacias en Git
for d in $(find "$ROOT" -type d -empty); do
  touch "$d/.gitkeep"
done

echo "Estructura creada en: $ROOT"
