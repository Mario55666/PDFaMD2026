#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversor interactivo PDF → Markdown
Basado en PyMuPDF4LLM (tecnología de pdf3md)

Ejecutar celda por celda en Jupyter/IPython.
"""

import os
from pathlib import Path
import pymupdf4llm
import fitz


def convertir_pdf(ruta_pdf, incluir_info=True):
    """
    Convierte un archivo PDF a Markdown.

    Args:
        ruta_pdf: Ruta al archivo PDF (string o Path)
        incluir_info: Si True, agrega metadatos YAML al inicio

    Returns:
        tuple: (texto_markdown, info_dict)
    """
    ruta_pdf = Path(ruta_pdf)

    if not ruta_pdf.exists():
        raise FileNotFoundError(f"No se encontró: {ruta_pdf}")

    # Leer info del PDF
    doc = fitz.open(str(ruta_pdf))
    info = {
        "archivo": ruta_pdf.name,
        "paginas": len(doc),
        "titulo": doc.metadata.get("title", "N/A"),
        "autor": doc.metadata.get("author", "N/A"),
        "tamano_kb": round(ruta_pdf.stat().st_size / 1024, 2)
    }
    doc.close()

    # Convertir a Markdown (usando pymupdf4llm igual que pdf3md)
    print(f"🔄 Convirtiendo: {ruta_pdf.name} ({info['paginas']} páginas)...")
    md_text = pymupdf4llm.to_markdown(str(ruta_pdf))

    # Agregar metadatos YAML frontmatter
    if incluir_info:
        header = f"""---
title: "{info['titulo']}" 
author: "{info['autor']}" 
pages: {info['paginas']}
source_file: "{info['archivo']}" 
---

"""
        md_text = header + md_text

    print(f"✅ Conversión exitosa: {len(md_text):,} caracteres")
    return md_text, info


def guardar_md(md_text, ruta_salida):
    """Guarda el texto Markdown en archivo."""
    ruta_salida = Path(ruta_salida)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(md_text)

    print(f"💾 Guardado: {ruta_salida}")
    return ruta_salida


def convertir_lote(rutas_pdf, carpeta_salida="./markdown_output"):
    """
    Convierte múltiples PDFs a Markdown.

    Args:
        rutas_pdf: Lista de rutas a archivos PDF
        carpeta_salida: Carpeta donde guardar los .md

    Returns:
        dict: {nombre_archivo: exito_boolean}
    """
    carpeta_salida = Path(carpeta_salida)
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    resultados = {}

    print("=" * 50)
    print("  CONVERSIÓN PDF → MARKDOWN (PyMuPDF4LLM)")
    print("=" * 50)

    for ruta in rutas_pdf:
        try:
            md_text, info = convertir_pdf(ruta)
            ruta_salida = carpeta_salida / (Path(ruta).stem + ".md")
            guardar_md(md_text, ruta_salida)
            resultados[Path(ruta).name] = True
        except Exception as e:
            print(f"❌ Error con {ruta}: {e}")
            resultados[Path(ruta).name] = False

    exitos = sum(resultados.values())
    print(f"\n📊 Total: {exitos}/{len(rutas_pdf)} archivos convertidos")
    print(f"📁 Salida: {carpeta_salida.absolute()}")

    return resultados


# ============ USO EJEMPLO ============
# 
# 1. Un solo archivo:
#    md_text, info = convertir_pdf("/ruta/al/archivo.pdf")
#    guardar_md(md_text, "/ruta/salida/archivo.md")
#
# 2. Múltiples archivos:
#    pdfs = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
#    convertir_lote(pdfs, "./mis_markdowns")
#
# 3. Todos los PDF de una carpeta:
#    from glob import glob
#    pdfs = glob("/ruta/carpeta/*.pdf")
#    convertir_lote(pdfs)
