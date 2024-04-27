import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for path in filepaths:
    with open(path, "r") as file:
        content = file.read()
    pdf.add_page()
    filename = Path(path).stem
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.title()}", ln=1)
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output(f"PDFs/animals.pdf")

