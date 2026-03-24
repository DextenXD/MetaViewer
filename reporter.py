from pathlib import Path
import os
from extractors.pdf import extract_pdf

def main(filepath, formatType):
  filepath = Path(filepath)
  if filepath.suffix == ".pdf":
    pdfReporter(filepath, formatType)



def pdfReporter(filepath, formatType):
    data = extract_pdf(filepath)
    if formatType == "text":
      if os.path.exists("PdfReport.txt"):
        os.remove("PdfReport.txt")
      with open("PdfReport.txt", "a") as f:
        for key, value in data.items():
          f.write(f"{key}: {value} \n")
      f.close()
        
