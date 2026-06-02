from extractors.diagnosis_extractor import (
    DiagnosisExtractor
)

from extractors.pending_result_extractor import (
    PendingResultExtractor
)

from workflows.summary_generator import (
    SummaryGenerator
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

diagnoses = DiagnosisExtractor().extract(text)

pending = PendingResultExtractor().extract(text)

summary = SummaryGenerator().generate(
    diagnoses,
    pending
)

print(summary.model_dump_json(indent=2))