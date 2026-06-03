from extractors.pdf_extractor import PDFExtractor
from extractors.discharge_condition_extractor import (
    DischargeConditionExtractor
)

pdf_path = "data/patient_2/Patient 2.pdf"

text = PDFExtractor().extract_text(pdf_path)

condition = (
    DischargeConditionExtractor().extract(text)
)

print("\nDISCHARGE CONDITION\n")

print(condition)