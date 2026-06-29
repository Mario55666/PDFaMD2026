# PDF a Markdown Converter

**d3amgindesign | 2026**

Conversor de archivos PDF a formato Markdown que funciona 100% en el navegador. Arrastra tus PDFs, conviertelos y descarga los archivos `.md` — todo sin conexion a internet y sin subir archivos a ningun servidor.

---

## Caracteristicas principales

- **100% local**: El procesamiento ocurre integramente en tu navegador usando JavaScript. Tus archivos nunca salen de tu dispositivo.
- **Sin instalacion**: Un solo archivo HTML. Solo abrelo en tu navegador y funciona.
- **Multiples archivos**: Convierte varios PDFs simultaneamente en lote.
- **Deteccion inteligente**: Analiza los tamenos de fuente del PDF para identificar encabezados (`#`, `##`, `###`), listas, negritas y parrafos.
- **Vista previa**: Visualiza el Markdown generado antes de descargarlo.
- **Descarga directa**: Exporta cada resultado como archivo `.md` con un clic.
- **Copia rapida**: Copia el contenido Markdown al portapapeles.
- **Diseno retro-tech**: Interfaz estilo Synthwave/Cyberpunk con acentos neon.

## Requisitos

- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Conexion a internet (solo para cargar PDF.js desde CDN la primera vez)
- Archivos PDF con texto seleccionable

## Como usar

### Metodo 1: Abrir directamente

1. Descarga el archivo `pdf_a_markdown.html`
2. Abrelo con tu navegador (doble clic)
3. Arrastra archivos PDF al area indicada o haz clic para seleccionarlos
4. Presiona **Iniciar conversion**
5. Descarga o copia cada resultado

### Metodo 2: Desplegar en servidor web

1. Copia `pdf_a_markdown.html` a la carpeta publica de tu servidor
2. Accede a la URL correspondiente
3. Usa normalmente

### Metodo 3: Para desarrolladores (modificar)

1. Clona o descarga el archivo HTML
2. Edita los estilos CSS internos para personalizar colores, fuentes o disenno
3. Abre el archivo en un editor de codigo
4. Guarda y prueba en tu navegador

## Manual de uso detallado

### Paso 1: Selecciona tus PDFs

Arrastra uno o varios archivos PDF al area punteada de la interfaz, o haz clic para abrir el selector de archivos. El sistema soporta multiples archivos simultaneos.

### Paso 2: Inicia la conversion

Presiona el boton **Iniciar conversion**. El procesamiento ocurre 100% en tu navegador. Veras una barra de progreso y los resultados apareceran en tiempo real.

### Paso 3: Descarga los resultados

Cada archivo convertido muestra:
- Numero de paginas procesadas
- Cantidad de caracteres y lineas
- Titulo y autor (si estan en los metadatos del PDF)

Usa los botones de cada tarjeta para:
- **Copiar**: Copia el Markdown al portapapeles
- **Descargar**: Guarda el archivo como `.md`
- **Ver**: Expande la vista previa del contenido Markdown

### Paso 4: Seguridad garantizada

Tus archivos **nunca se suben** a ningun servidor. Todo el procesamiento es local usando PDF.js de Mozilla. Puedes usar la herramienta incluso sin conexion a internet despues de la primera carga.

## Como funciona

La herramienta utiliza un enfoque basado en **PDF.js** (Mozilla) para extraer el contenido textual de los PDFs. El algoritmo de conversion a Markdown analiza:

1. **Posicion espacial**: Las coordenadas (X, Y) de cada fragmento de texto para reconstruir el orden de lectura
2. **Tamanos de fuente**: Detecta jerarquias para identificar encabezados (`#`, `##`, `###`)
3. **Formatos especiales**: Reconoce listas con viñetas, listas numeradas y texto en negrita
4. **Post-procesamiento**: Une lineas sueltas que pertenecen al mismo parrafo y limpia el resultado

Este enfoque esta inspirado en **pdf3md**, que utiliza PyMuPDF4LLM para la conversion.

## Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| PDF.js v4.7.76 | Extraccion de texto y metadatos de PDFs |
| Vanilla JavaScript | Logica de conversion y manejo de archivos |
| CSS3 | Estilos retro-tech con efectos neon, CRT scanlines y grid |
| Google Fonts (Inter, JetBrains Mono) | Tipografia legible y moderna |

## Limitaciones conocidas

- PDFs basados en imagenes (escaneados) no son compatibles, ya que no contienen texto seleccionable
- Archivos PDF muy grandes (mas de 50 MB) pueden tardar en procesar
- La calidad de la conversion depende de la estructura interna del PDF
- Tablas complejas pueden perder su formato exacto

## Personalizacion

El archivo es autocontenido. Puedes modificar:

- **Colores**: Edita las variables CSS en `:root` para cambiar la paleta
- **Tipografia**: Sustituye las fuentes de Google Fonts en el `<link>` del head
- **Textos**: Busca y reemplaza las etiquetas de texto en el HTML
- **Efectos visuales**: Activa/desactiva scanlines CRT, grid de fondo o marquee

## Credito e inspiracion

Este proyecto esta inspirado en [**pdf3md**](https://github.com/murtaza-nasir/pdf3md) de Murtaza Nasir, una aplicacion web que convierte PDFs a Markdown usando PyMuPDF4LLM. La version presente replica el mismo objetivo funcionando integramente en el navegador sin requerir backend.

## Desarrollador

**d3amgindesign**

## Licencia

Uso libre para fines educativos y personales.

---

*Lima, Peru | 2026*
