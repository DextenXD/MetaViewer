from pathlib import Path
import os
from extractors.pdf import extract_pdf

def main(filepath, formatType):
  filepath = Path(filepath)
  if filepath.suffix.lower() == ".pdf":
    pdfReporter(filepath, formatType)
  elif filepath.suffix.lower() in [".png", ".jpeg", ".jpg", ".webp", ".gif"]:
    imageReporter(filepath, formatType)



def pdfReporter(filepath, formatType):
    data = extract_pdf(filepath)
    if data is None:
      print("Could not extract data")
      return
    if formatType == "text":
      if os.path.exists("PdfReport.txt"):
        os.remove("PdfReport.txt")
      with open("PdfReport.txt", "a") as f:
        for key, value in data.items():
          f.write(f"{key}: {value} \n")
      f.close()
    elif formatType == "json":
      with open("PdfReport.txt", "a") as f:
        f.write(str(data))

def imageReporter(filepath, formatType):
  return
