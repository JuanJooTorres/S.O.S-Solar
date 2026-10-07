# 🗂️ Estructura sugerida del repositorio — S.O.S Solar

## 🌳 Mapa de carpetas

```text
S.O.S-Solar/
│
├── README.md                      # Página principal (divulgativa)
├── TECHNICAL_DOCS.md              # Anexo técnico (especializado)
├── ESTRUCTURA_REPOSITORIO.md      # Este documento (puede moverse a /docs)
├── LICENSE                        # Licencia (MIT)
├── CONTRIBUTING.md                # (Opcional) Guía para colaborar
├── .gitignore
│
├── docs/                          # Documentación ampliada
│   ├── guia-de-uso.md             # Cómo usar la estación (para la comunidad)
│   ├── glosario.md                # Glosario extendido
│   ├── manual-de-seguridad.md     # Normas de uso y seguridad
│   ├── informe-final.pdf          # Informe institucional
│   └── presentacion.pdf           # Presentación del proyecto
│
├── schematics/                    # Esquemáticos
│   ├── system/
│   │   ├── sistema_general.pdf
│   │   └── sistema_general.<fuente>
│   └── inverter/
│       ├── inversor_spwm.pdf
│       └── inversor_spwm.<fuente>
│
├── pcb/                           # Diseño de circuito impreso
│   └── inverter/
│       ├── project/               # Proyecto EDA editable
│       ├── gerbers/               # Archivos de fabricación
│       ├── BOM.csv                # Lista de materiales
│       └── renders/               # Vistas 3D / capas
│
├── hardware/                      # Mecánica y montaje
│   ├── diagrama-cableado.pdf
│   ├── estructura-soporte/        # Planos del soporte del panel / gabinete
│   └── lista-componentes.csv
│
├── data/                          # Datos y análisis
│   ├── measurements/
│   │   ├── curva_carga.csv
│   │   ├── curva_descarga.csv
│   │   └── tension_panel.csv
│   ├── analysis/
│   │   └── analisis_eficiencia.ipynb
│   └── scripts/
│       └── calculo_autonomia.py
│
├── datasheets/                    # Hojas de datos de componentes
│   ├── EGS002.pdf
│   ├── mosfets.pdf
│   ├── bateria-vrla-agm.pdf
│   └── controlador.pdf
│
└── media/                         # Recursos visuales
    ├── banner/
    │   └── banner-sos-solar.png
    ├── images/
    │   ├── prototipo-general.jpg
    │   ├── panel-instalado.jpg
    │   └── dispositivos-cargando.jpg
    ├── oscilogramas/
    │   ├── onda-sin-carga.png
    │   └── onda-con-carga.png
    ├── diagramas/
    │   ├── flujo-energia.png
    │   └── bloques-conceptuales.png
    ├── gifs/
    │   └── demo-funcionamiento.gif
    └── videos/
        └── demo.mp4
```

---

## 📌 Qué va en cada carpeta

| Carpeta | Contenido | Público principal |
|---|---|---|
| `/docs` | Guías de uso, glosario, informe y presentación | 🌱 General |
| `/schematics` | Esquemáticos del sistema y del inversor | ⚙️ Técnico |
| `/pcb` | Proyecto EDA, Gerbers, BOM y renders del PCB | ⚙️ Técnico |
| `/hardware` | Cableado, soporte y montaje mecánico | ⚙️ Técnico |
| `/data` | Mediciones, scripts y análisis | ⚙️ Técnico |
| `/datasheets` | Hojas de datos de los componentes | ⚙️ Técnico |
| `/media` | Fotos, oscilogramas, diagramas, GIFs y videos | 🌱 y ⚙️ |

---

## 🖼️ Assets recomendados

| Asset | Para qué sirve | Ruta | Prioridad |
|---|---|---|:-:|
| Banner del proyecto | Encabezado visual del README | `media/banner/` | ⭐⭐⭐ |
| Foto del prototipo completo | Primera impresión | `media/images/prototipo-general.jpg` | ⭐⭐⭐ |
| GIF/video de demostración | Mostrar el celular cargando | `media/gifs/` | ⭐⭐⭐ |
| Capturas de osciloscopio | Evidencia de onda senoidal | `media/oscilogramas/` | ⭐⭐⭐ |
| Diagrama de flujo de energía | Explicación visual | `media/diagramas/` | ⭐⭐ |
| Render 3D del PCB | Estética técnica | `pcb/inverter/renders/` | ⭐⭐ |
| Foto del equipo | Identidad humana del proyecto | `media/images/equipo.jpg` | ⭐⭐ |

### Cómo insertar los assets en el README

```markdown
![Prototipo S.O.S Solar](media/images/prototipo-general.jpg)
![Demo](media/gifs/demo-funcionamiento.gif)
<img src="media/oscilogramas/onda-con-carga.png" width="600" alt="Onda senoidal pura">
```

---

## ✅ Buenas prácticas

- **Nombres de archivo:** minúsculas, sin espacios ni tildes (`onda-con-carga.png`).
- **Imágenes ligeras:** menos de 1 MB cuando sea posible; los GIF pesados pueden reemplazarse por video.
- **Texto alternativo:** describir siempre la imagen en el `alt`.
- **Archivos grandes (video, Gerbers pesados):** considerar [Git LFS](https://git-lfs.com/) o publicarlos en *Releases*.
- **Fuentes y exportaciones:** guardar tanto el archivo editable como el PDF exportado.
- **Escalas en mediciones:** toda captura de osciloscopio debe mostrar V/div, s/div y el canal.
- **Etiquetas del repositorio (Topics):** `solar-energy`, `renewable-energy`, `inverter`, `pure-sine-wave`, `spwm`, `egs002`, `education`, `colombia`.
- **Releases:** publicar versiones del diseño (`v1.0-prototipo`) con Gerbers y BOM.

---

## 🧱 Crear la estructura rápidamente

Puedes generar todo el árbol de carpetas con el script `crear_estructura.sh` (incluido como descarga).
