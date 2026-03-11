"""
print_barcodes_to_pdf.py

Reads SVG and raster images from ./barcode_images, converts them to pure B/W bitmaps
at high DPI, lays them out on A4 pages at 2.375 in x 0.1875 in (width x height),
prints the filename under each barcode, and writes a multi-page PDF: barcodes_output.pdf.

The purpose is to print all barcodes in a correctly scaled printable manner so that they
can be cut out and placed on minecarft arcade cards with a gluestick, allowing the player
to try any of the card power-ups they would like.  As new codes are added to the barcode 
images folder this script should be able to support those without additional updates.

Developed under Python 3.13.12.

Place your SVG/raster files in ./barcode_images next to this script.

Precondition:
    In Windows recommend installing Miniconda and using the Anaconda Prompt to run python and pip: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

Python Dependencies:
    pip install svglib

Usage:
    python print_barcodes_to_pdf.py

"""

#!/usr/bin/env python3
import os
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.lib.utils import ImageReader
from PIL import Image

# ---------- Configuration ----------
IMAGES_FOLDER = os.path.join(os.path.dirname(__file__), "barcode_images")
OUTPUT_PDF = os.path.join(os.path.dirname(__file__), "barcodes_output.pdf")

# Physical sizes (Millimeters)
BARCODE_WIDTH_MM = 60.0
BARCODE_HEIGHT_MM = 5.0
TEXT_GAP_MM = 1.5
H_SPACING_MM = 3.0
V_SPACING_MM = 3.0
MARGIN_MM = 12.7

# PDF / layout settings
PT_PER_MM = 2.83465
RASTER_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}

# Thread pool size (None => default)
MAX_WORKERS = None

# ---------- Helpers ----------

def list_image_files():
    files = []
    if not os.path.isdir(IMAGES_FOLDER):
        raise FileNotFoundError(f"Images folder not found: {IMAGES_FOLDER}")
    for fn in sorted(os.listdir(IMAGES_FOLDER), key=lambda s: s.lower()):
        path = os.path.join(IMAGES_FOLDER, fn)
        if os.path.isfile(path) and os.path.splitext(fn)[1].lower() in ({".svg"} | RASTER_EXTS):
            files.append(path)
    return files

def prepare_svg(path):
    try:
        drawing = svg2rlg(path)
        w = getattr(drawing, "width", None)
        h = getattr(drawing, "height", None)
        if not w or not h:
            bbox = getattr(drawing, "bbox", (None, None, None, None))
            w = w or bbox[2] or 1.0
            h = h or bbox[3] or 1.0
            drawing.width, drawing.height = w, h
        return (path, drawing, "svg")
    except Exception as e:
        return (path, None, f"error: {e}")

def prepare_raster(path):
    try:
        pil = Image.open(path).convert("RGBA")
        return (path, pil, "raster")
    except Exception as e:
        return (path, None, f"error: {e}")

def process_single(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".svg":
        return prepare_svg(path)
    else:
        return prepare_raster(path)

# ---------- Drawing helpers ----------

def draw_ruler_top(c, start_x, baseline_y, length_mm=60):
    """
    Draw a horizontal millimeter ruler from 0 to length_mm at baseline_y.
    start_x and baseline_y must already be inside the printable area.
    """
    tick_long = 6
    tick_medium = 4
    tick_short = 2

    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(0.5)
    end_x = start_x + length_mm * PT_PER_MM
    c.line(start_x, baseline_y, end_x, baseline_y)

    for mm in range(0, length_mm + 1):
        x = start_x + mm * PT_PER_MM
        if mm % 10 == 0:
            tlen = tick_long
        elif mm % 5 == 0:
            tlen = tick_medium
        else:
            tlen = tick_short
        c.line(x, baseline_y, x, baseline_y - tlen)
        if mm % 10 == 0:
            label = str(mm)
            c.setFont("Helvetica", 6)
            c.drawCentredString(x, baseline_y - tlen - 6, label)

    # unit label "mm" to the right of the final mark
    unit_x = end_x + (4 * PT_PER_MM / 2.0)
    c.setFont("Helvetica", 7)
    c.drawString(unit_x, baseline_y - tick_long - 6, "mm")

def draw_vertical_ruler_right(c, x_pos, top_y, length_mm=10):
    """
    Draw a vertical ruler with 0 at top_y and length_mm at top_y - length_mm.
    Only numeric labels for 0 and length_mm are drawn. Ticks every 1 mm.
    x_pos is the x coordinate where the vertical baseline will be drawn.
    """
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(0.5)
    bottom_y = top_y - (length_mm * PT_PER_MM)
    # draw vertical baseline
    c.line(x_pos, top_y, x_pos, bottom_y)

    tick_short = 3
    tick_long = 6

    # draw ticks every 1 mm; ticks extend to the right
    for mm in range(0, length_mm + 1):
        y = top_y - mm * PT_PER_MM
        tlen = tick_long if mm % 5 == 0 else tick_short
        c.line(x_pos, y, x_pos + tlen, y)

    # labels only for 0 and length_mm
    c.setFont("Helvetica", 6)
    c.drawString(x_pos + tick_long + 2, top_y - 3, "0")
    c.drawString(x_pos + tick_long + 2, bottom_y - 3, str(length_mm))
    # unit label "mm" to the right of the bottom mark
    c.setFont("Helvetica", 7)
    c.drawString(x_pos + tick_long + 18, bottom_y - 6, "mm")

# ---------- Main PDF generation ----------

def generate_pdf():
    files = list_image_files()
    if not files:
        print("No images found.")
        return

    print(f"Preparing {len(files)} images using ThreadPoolExecutor...")
    prepared = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(process_single, f): f for f in files}
        for fut in as_completed(futures):
            res = fut.result()
            prepared.append(res)

    # preserve original order
    path_to_result = {p: (obj, t) for (p, obj, t) in prepared}
    ordered_results = [(p, path_to_result[p][0], path_to_result[p][1]) for p in files]

    # Convert MM to points
    bw_pt = BARCODE_WIDTH_MM * PT_PER_MM   # full placed width = 60 mm
    bh_pt = BARCODE_HEIGHT_MM * PT_PER_MM
    gap_pt = TEXT_GAP_MM * PT_PER_MM
    h_sp_pt = H_SPACING_MM * PT_PER_MM
    v_sp_pt = V_SPACING_MM * PT_PER_MM
    margin_pt = MARGIN_MM * PT_PER_MM

    c = canvas.Canvas(OUTPUT_PDF, pagesize=A4)
    page_w, page_h = A4
    printable_w = page_w - 2 * margin_pt
    columns = max(1, int(math.floor((printable_w + h_sp_pt) / (bw_pt + h_sp_pt))))

    # Compute a baseline for the top horizontal ruler that is INSIDE the printable area.
    top_printable_y = page_h - margin_pt
    baseline_offset_mm = 1.5
    baseline_y = top_printable_y - (baseline_offset_mm * PT_PER_MM)

    # Draw top horizontal ruler on first page at baseline_y
    start_x = margin_pt
    draw_ruler_top(c, start_x, baseline_y, length_mm=60)

    # Determine where to start placing barcodes: place them below the ruler and its labels.
    tick_long = 6  # points used in draw_ruler_top
    label_space_pt = 6  # space used below ticks for labels in draw_ruler_top
    extra_gap_pt = 4  # small gap between ruler labels and first barcode row
    y_pt = baseline_y - tick_long - label_space_pt - extra_gap_pt

    x_pt = margin_pt

    font_name = "Helvetica"
    font_size = 7
    c.setFont(font_name, font_size)

    # Compute vertical ruler position: to the right of the first row of barcodes
    first_row_width = columns * bw_pt + (columns - 1) * h_sp_pt
    small_gap_mm = 3.0  # small gap between barcode row and vertical ruler in mm
    small_gap_pt = small_gap_mm * PT_PER_MM
    vertical_ruler_x = margin_pt + first_row_width + small_gap_pt

    # top of barcode band is y_pt; vertical ruler 0 should align with top of barcodes
    vertical_ruler_top_y = y_pt

    # Draw the vertical 0-10 mm ruler to the right of the first row
    draw_vertical_ruler_right(c, vertical_ruler_x, vertical_ruler_top_y, length_mm=10)

    item_index = 0
    for path, obj, img_type in ordered_results:
        if obj is None:
            print(f"Skipping {path}: processing failed.")
            continue

        # compute lower-left y coordinate for drawing
        y_draw = y_pt - bh_pt

        if img_type == "svg":
            drawing = obj
            d_w = getattr(drawing, "width", 1.0) or 1.0
            d_h = getattr(drawing, "height", 1.0) or 1.0
            # scale to full placed area (60 mm) so built-in white margins are preserved
            sx = bw_pt / float(d_w)
            sy = bh_pt / float(d_h)
            s = min(sx, sy)
            drawing.scale(s, s)
            renderPDF.draw(drawing, c, x_pt, y_draw)
        else:
            pil = obj
            img_reader = ImageReader(pil)
            src_w, src_h = pil.size
            src_aspect = src_w / src_h
            target_aspect = bw_pt / bh_pt
            if src_aspect >= target_aspect:
                draw_w = bw_pt
                draw_h = bw_pt / src_aspect
            else:
                draw_h = bh_pt
                draw_w = bh_pt * src_aspect
            draw_x = x_pt + (bw_pt - draw_w) / 2.0
            c.drawImage(img_reader, draw_x, y_draw, width=draw_w, height=draw_h, mask='auto')

        # Outline the full 60mm area with very thin dashed stroke (0.1 pt) in light grey
        # Save current stroke color to restore later (ReportLab doesn't provide a direct save/restore,
        # so we explicitly set black again after drawing the grey dashed rect).
        grey_value = 0.7  # light grey (0 = black, 1 = white)
        c.setStrokeColorRGB(grey_value, grey_value, grey_value)
        c.setLineWidth(0.1)
        # dash pattern: 1pt on, 1pt off
        c.setDash([1, 1])
        c.rect(x_pt, y_draw, bw_pt, bh_pt, stroke=1, fill=0)
        # clear dash and restore stroke color to black for subsequent drawing
        c.setDash([])
        c.setStrokeColorRGB(0, 0, 0)

        # Label: place below the barcode with a small gap
        text_y = y_draw - gap_pt - font_size
        c.setFont(font_name, font_size)
        c.drawCentredString(x_pt + bw_pt / 2.0, text_y, os.path.basename(path))

        item_index += 1
        # advance grid
        if (item_index % columns) == 0:
            x_pt = margin_pt
            # move down by barcode height + label + spacing
            y_pt = y_draw - gap_pt - font_size - v_sp_pt
            # if not enough space for next row, new page
            if y_pt - bh_pt < margin_pt:
                c.showPage()
                # draw top ruler only on the first page per prior behavior
                x_pt = margin_pt
                y_pt = page_h - margin_pt - bh_pt - (margin_pt * 0.25)
                c.setFont(font_name, font_size)
        else:
            x_pt += bw_pt + h_sp_pt

    c.save()
    print(f"PDF successfully generated: {OUTPUT_PDF}")

if __name__ == "__main__":
    generate_pdf()
