from extractors.pdf_extractor import PDFExtractor

from extractors.demographics_extractor import (
    DemographicsExtractor
)

pdf_path = "data/patient_2/Patient 2.pdf"

text = PDFExtractor().extract_text(
    pdf_path
)

result = (
    DemographicsExtractor().extract(
        text
    )
)

print(result)