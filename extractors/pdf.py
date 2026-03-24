from PyPDF2 import PdfReader


def extract_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        meta = reader.metadata
        return {
            # Main info
            "Author": meta.author or "Unknown",
            "Creator": meta.creator or "Unknown",
            "Producer": meta.producer or "Unknown",
            "Subject": meta.subject or "Unknown",
            "Title": meta.title or "Unknown",
            "Created": meta.creation_date or "Unknown",
            "Modified": meta.modification_date or "Unknown",
            # additional info
            "Keywords": meta.get("/keywords") or "Unknown",
            "Trapped": meta.get("/Trapped") or "Unknown",
            "Language": meta.get("/lang") or "Unknown",
            # Document info
            "Pages": len(reader.pages) or "Unknown",
            "Headers": reader.pdf_header or "Unknown",
            "Encrypted": reader.is_encrypted or "Unknown",
            "Page Layout": reader.page_layout or "Unknown",
            "Page Mode": reader.page_mode or "Unknown",
        }
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

    except Exception as e:
        print(f"How did you even manage to do this??? {e}")
        return None
