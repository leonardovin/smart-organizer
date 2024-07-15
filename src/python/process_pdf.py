# process_pdf.py

from .extract_text import extract_text_from_pdf
from .detect_title import detect_title
from .rename_file import rename_pdf_file

def process_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    title = detect_title(text)
    if title:
        # rename_pdf_file(pdf_path, title)
        print(title)
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_pdf(sys.argv[1])
    else:
        print("Usage: python process_pdf.py <path_to_pdf>")
