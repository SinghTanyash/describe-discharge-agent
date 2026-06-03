from tools.correction_memory import CorrectionMemory


memory = CorrectionMemory()

memory.remember(
    "for 3 DAYS",
    "Duration 3 DAYS"
)

memory.remember(
    "CLINICIAN REVIEW REQUIRED.",
    "CLINICIAN REVIEW REQUIRED: Yes"
)

print("\nMEMORY CONTENTS\n")

for mistake, correction in memory.get_all().items():

    print(
        f"{mistake} -> {correction}"
    )