from tools.learning_engine import LearningEngine


draft = """
**DISCHARGE SUMMARY**

EMESET: for 3 DAYS

**CLINICIAN REVIEW REQUIRED.**
"""


engine = LearningEngine()

improved = engine.improve(
    draft
)

print("\nORIGINAL DRAFT\n")
print(draft)

print("\nIMPROVED DRAFT\n")
print(improved)