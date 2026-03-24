from PyPDF2 import PdfReader

def extract_pdf(filepath):
  reader = PdfReader(filepath)
  print(reader.metadata)
