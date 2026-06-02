from tools.pending_result_extractor import (
    PendingResultExtractor
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

extractor = PendingResultExtractor()

results = extractor.extract(text)

print("\nPending Results:\n")

for result in results:
    print("-", result)