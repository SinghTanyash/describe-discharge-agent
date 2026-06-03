from extractors.discharge_summary_section_extractor import (
    DischargeSummarySectionExtractor
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

section = (
    DischargeSummarySectionExtractor().extract(
        text
    )
)

print(section)