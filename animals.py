import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", size=16, style="B")
for path in filepaths:
    pdf.add_page()
    filename = Path(path).stem
    pdf.cell(w=50, h=8, txt=f"{filename.title()}")


pdf.output(f"PDFs/animals.pdf")

