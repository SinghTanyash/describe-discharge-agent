from tools.diagnosis_extractor import DiagnosisExtractor

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

extractor = DiagnosisExtractor()

diagnoses = extractor.extract(text)

print("\nDiagnoses Found:\n")

for diagnosis in diagnoses:
    print("-", diagnosis)