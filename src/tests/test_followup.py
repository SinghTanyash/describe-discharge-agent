from extractors.followup_extractor import (
    FollowupExtractor
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

followups = (
    FollowupExtractor().extract(text)
)

print("\nFOLLOW UPS FOUND\n")

for item in followups:
    print("-", item)