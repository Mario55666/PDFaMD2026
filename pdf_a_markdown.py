#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF to Markdown Converter
Basado en la misma tecnología de pdf3md (https://github.com/murtaza-nasir/pdf3md)
Usa PyMuPDF4LLM para convertir PDFs a Markdown limpio y bien estructurado.

Uso:
    python pdf_a_markdown.py <archivo.pdf> [archivo2.pdf ...]

Ejemplos:
    # Un solo archivo
    python pdf_a_markdown.py documento.pdf

    # Múltiples archivos
    python pdf_a_markdown.py doc1.pdf doc2.pdf doc3.pdf

    # Todos los PDFs de una carpeta
    python pdf_a_markdown.py *.pdf

    # Especificar carpeta de salida
    python pdf_a_markdown.py --output ./markdowns documento.pdf
"""

import os
import sys
import argparse
from pathlib import Path
import pymupdf4llm
import fitz


def obtener_info_pdf(ruta_pdf):
    """Obtiene información básica del PDF."""
    doc = fitz.open(ruta_pdf)
    info = {
        "paginas": len(doc),
        "titulo": doc.metadata.get("title", "N/A"),
        "autor": doc.metadata.get("author", "N/A"),
        "archivo": Path(ruta_pdf).name,
        "tamano_mb": round(os.path.getsize(ruta_pdf) / (1024 * 1024), 2)
    }
    doc.close()
    return info


def convertir_pdf_a_markdown(ruta_pdf, paginas=None, imagenes=False):
    """
    Convierte un PDF a Markdown usando PyMuPDF4LLM.

    Args:
        ruta_pdf: Ruta al archivo PDF
        paginas: Tupla (inicio, fin) para páginas específicas, o None para todas
        imagenes: Si True, incluye imágenes en el markdown

    Returns:
        str: Texto en formato Markdown
    """
    kwargs = {}

    if paginas:
        kwargs["pages"] = list(range(paginas[0], paginas[1]))

    if imagenes:
        kwargs["embed_images"] = True

    # Conversión principal usando pymupdf4llm (mismo motor que pdf3md)
    md_text = pymupdf4llm.to_markdown(ruta_pdf, **kwargs)

    return md_text


def guardar_markdown(contenido_md, ruta_salida, info_pdf=None):
    """Guarda el contenido Markdown en un archivo."""
    # Agregar metadatos al inicio
    header = ""
    if info_pdf:
        header = f"""---
title: "{info_pdf['titulo']}" 
author: "{info_pdf['autor']}" 
pages: {info_pdf['paginas']}
source: "{info_pdf['archivo']}" 
---

"""

    contenido_completo = header + contenido_md

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(contenido_completo)

    return ruta_salida


def procesar_archivo(ruta_pdf, carpeta_salida, paginas=None, imagenes=False):
    """Procesa un único archivo PDF."""
    ruta_pdf = Path(ruta_pdf)

    if not ruta_pdf.exists():
        print(f"  [ERROR] No se encontró: {ruta_pdf}")
        return False

    if ruta_pdf.suffix.lower() != ".pdf":
        print(f"  [ERROR] No es un PDF: {ruta_pdf}")
        return False

    print(f"\n📄 Procesando: {ruta_pdf.name}")

    # Obtener información del PDF
    try:
        info = obtener_info_pdf(ruta_pdf)
        print(f"   Páginas: {info['paginas']} | Tamaño: {info['tamana_mb']} MB")
    except Exception as e:
        print(f"   [AVISO] No se pudo leer info: {e}")
        info = None

    # Convertir a Markdown
    try:
        print(f"   🔄 Convirtiendo a Markdown...")
        md_text = convertir_pdf_a_markdown(str(ruta_pdf), paginas, imagenes)

        # Guardar archivo
        nombre_salida = ruta_pdf.stem + ".md"
        ruta_salida = Path(carpeta_salida) / nombre_salida

        guardar_markdown(md_text, ruta_salida, info)

        print(f"   ✅ Guardado: {ruta_salida}")
        print(f"   📊 Caracteres: {len(md_text):,} | Líneas: {md_text.count(chr(10)):,}")
        return True

    except Exception as e:
        print(f"   [ERROR] Conversión fallida: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Convierte archivos PDF a Markdown usando PyMuPDF4LLM (tecnología de pdf3md)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python pdf_a_markdown.py documento.pdf
  python pdf_a_markdown.py doc1.pdf doc2.pdf doc3.pdf --output ./md
  python pdf_a_markdown.py *.pdf --output ./markdowns
        """
    )

    parser.add_argument("archivos", nargs="+", help="Archivos PDF a convertir")
    parser.add_argument("-o", "--output", default=".", help="Carpeta de salida (default: actual)")
    parser.add_argument("--paginas", nargs=2, type=int, metavar=("INICIO", "FIN"),
                        help="Rango de páginas a convertir (0-based)")
    parser.add_argument("--imagenes", action="store_true",
                        help="Incluir imágenes en el Markdown")

    args = parser.parse_args()

    # Crear carpeta de salida si no existe
    carpeta_salida = Path(args.output)
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("  PDF → Markdown Converter")
    print("  Basado en pdf3md (PyMuPDF4LLM)")
    print("=" * 60)

    # Procesar cada archivo
    exitos = 0
    fallidos = 0

    for archivo in args.archivos:
        if procesar_archivo(archivo, carpeta_salida, args.paginas, args.imagenes):
            exitos += 1
        else:
            fallidos += 1

    # Resumen
    print("\n" + "=" * 60)
    print(f"  RESUMEN: {exitos} convertidos | {fallidos} fallidos")
    print(f"  Carpeta de salida: {carpeta_salida.absolute()}")
    print("=" * 60)

    return 0 if fallidos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
