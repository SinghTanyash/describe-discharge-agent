from extractors.pdf_extractor import PDFExtractor
from extractors.allergy_extractor import (
    AllergyExtractor
)

pdf_path = "data/patient_2/Patient 2.pdf"
text = PDFExtractor().extract_text(
    pdf_path
)

allergies = (
    AllergyExtractor().extract(text)
)

print("\nALLERGIES FOUND\n")

for allergy in allergies:
    print("-", allergy)