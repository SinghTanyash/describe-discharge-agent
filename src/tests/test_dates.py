from extractors.pdf_extractor import PDFExtractor

from extractors.date_extractor import (
    DateExtractor
)

pdf_path = "data/patient_2/Patient 2.pdf"

text = PDFExtractor().extract_text(
    pdf_path
)

dates = (
    DateExtractor().extract(text)
)

print(dates)