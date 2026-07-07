from pathlib import Path
from pypdf import PdfReader

SAMPLE = Path(__file__).resolve().parent / "Ayush.pdf"


def read_pdf(Path)-> str:
    reader = PdfReader(Path)
    print(reader)
    for page in reader.pages:
        print(page.extract_text())
read_pdf(SAMPLE)




















#     text = ""

#     for page_number, page in enumerate(reader.pages, start=1):
#         page_text = page.extract_text()
#         text += f"\n--- Page {page_number} ---\n"
#         text += page_text if page_text else "[No text found]"

#     return text


# if __name__ == "__main__":
#     print(read_pdf())