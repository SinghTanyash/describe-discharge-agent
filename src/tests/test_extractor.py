from tools.pdf_extractor import PDFExtractor

extractor = PDFExtractor()

text = extractor.extract_text(
    "data/patient_2/Patient 2.pdf"
)

with open(
    "outputs/patient2_ocr.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

print("OCR saved successfully")
print(f"Characters extracted: {len(text)}")