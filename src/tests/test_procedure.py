from extractors.pdf_extractor import PDFExtractor

from extractors.procedure_extractor import (
    ProcedureExtractor
)

pdf_path = "data/patient_2/Patient 2.pdf"

text = PDFExtractor().extract_text(
    pdf_path
)

procedures = (
    ProcedureExtractor().extract(
        text
    )
)

print("\nPROCEDURES FOUND\n")

for procedure in procedures:
    print("-", procedure)