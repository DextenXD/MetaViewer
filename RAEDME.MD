# MetaViewer 🔍

A CLI forensics tool that extracts metadata from files. Built for CTF challenges and OSINT investigations.

---

## Installation

```bash
git clone https://github.com/yourname/metaviewer
cd metaviewer
pip install -r requirements.txt
```

**requirements.txt**
```
Pillow
exifread
PyPDF2
mutagen
python-docx
```

---

## Usage

```bash
python main.py <file> --format <text|json>
```

**Examples**
```bash
python main.py document.pdf --format text
python main.py photo.jpg --format json
python main.py report.docx --format text
```

Output is saved as a report file in the current directory.

---

## Supported File Types

| Type | Extensions | Library |
|------|------------|---------|
| PDF | `.pdf` | PyPDF2 |
| Image | `.jpg` `.jpeg` `.png` `.webp` `.gif` | Pillow + exifread |
| Document | `.docx` | python-docx |

---

## Project Structure

```
metaviewer/
├── main.py               # Entry point, argument parsing
├── reporter.py           # Output formatting (text/json)
├── requirements.txt
└── extractors/
    ├── pdf.py            # PDF metadata extraction
    ├── image.py          # Image + EXIF extraction
    └── document.py       # DOCX metadata extraction
```

---

## Output Example

```
Author: John Doe
Created: 2000-01-01 12:00:00
Modified: 2001-01-01 12:00:00
Title: MetaViewer Test Document
Keywords: forensics, metadata, ctf
Pages: 2
Encrypted: False
```

---

> Built for educational and CTF use only.