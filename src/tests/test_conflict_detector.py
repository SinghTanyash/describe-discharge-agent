from tools.conflict_detector import (
    ConflictDetector
)

diagnoses = [
    "ACUTE GASTROENTERITIS WITH DEHYDRATION",
    "URINARY TRACT INFECTION"
]

hospital_course = """
USG abdomen showed findings
which could represent colitis.
"""

conflicts = (
    ConflictDetector().detect(
        diagnoses,
        hospital_course
    )
)

print("\nCONFLICTS\n")

for conflict in conflicts:
    print("-", conflict)