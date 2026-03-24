from pathlib import Path
import os
from extractors.pdf import extract_pdf
from extractors.image import extract_image
from extractors.document import extract_doc


def main(filepath, formatType):
    filepath = Path(filepath)
    if filepath.suffix.lower() == ".pdf":
        pdfReporter(filepath, formatType)
    elif filepath.suffix.lower() in [".png", ".jpeg", ".jpg", ".webp", ".gif"]:
        imageReporter(filepath, formatType)
    elif filepath.suffix.lower() == ".docx":
        docuReporter(filepath, formatType)


def pdfReporter(filepath, formatType):
    data = extract_pdf(filepath)
    if data is None:
        print("Could not extract data :(")
        return
    if formatType.lower() == "text":
        if os.path.exists("PdfReport.txt"):
            os.remove("PdfReport.txt")
        with open("PdfReport.txt", "a") as f:
            for key, value in data.items():
                f.write(f"{key}: {value} \n")
        f.close()
    elif formatType.lower() == "json":
        if os.path.exists("PdfReport.json"):
            os.remove("PdfReport.json")
        with open("PdfReport.json", "a") as f:
            f.write(str(data))
    else:
        print("please select json or text :D")


def imageReporter(filepath, formatType):
    data = extract_image(filepath)
    if data is None:
        print("Could not extract data :(")
        return
    if formatType.lower() == "text":
        if os.path.exists("ImgReport.txt"):
            os.remove("ImgReport.txt")
        with open("ImgReport.txt", "a") as f:
            for key, value in data.items():
                f.write(f"{str(key)}: {str(value)} \n")
    elif formatType.lower() == "json":
        if os.path.exists("ImgReport.json"):
            os.remove("ImgReport.json")
        with open("ImgReport.json", "a") as f:
            f.write(data)
    else:
        print("Please select json or text :D")

def docuReporter(filepath, formatType):
    data = extract_doc(filepath)
    if data is None:
        print("Could not extract data :(")
        return
    if formatType.lower() == "text":
        if os.path.exists("docReport.txt"):
            os.remove("docReport.txt")
        with open("docReport.txt", "a") as f:
            for key, value in data.items():
                f.write(f"{str(key)}: {str(value)} \n")
    elif formatType.lower() == "json":
        if os.path.exists("docReport.json"):
            os.remove("docReport.json")
        with open("docReport.json", "a") as f:
            f.write(data)
    else:
        print("Please select json or text :D")
        