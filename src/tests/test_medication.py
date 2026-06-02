from extractors.medication_extractor import (
    MedicationExtractor
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

medications = (
    MedicationExtractor().extract(text)
)

print("\nMEDICATIONS FOUND\n")

for med in medications:
    print("-", med)