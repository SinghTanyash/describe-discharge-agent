from tools.correction_learner import CorrectionLearner
from tools.correction_memory import CorrectionMemory


original = """
EMESET: for 3 DAYS

CLINICIAN REVIEW REQUIRED.
"""


edited = """
EMESET: Duration 3 DAYS

CLINICIAN REVIEW REQUIRED: Yes
"""


learner = CorrectionLearner()

learner.learn(
    original,
    edited
)

memory = CorrectionMemory()

print("\nUPDATED MEMORY\n")

for mistake, correction in memory.get_all().items():

    print(
        f"{mistake} -> {correction}"
    )