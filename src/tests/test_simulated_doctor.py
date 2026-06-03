from tools.simulated_doctor import SimulatedDoctor


draft = """
**DISCHARGE SUMMARY**

EMESET: for 3 DAYS

Review immediately in case of fever, loose stools, vomiting, or fatigue.

**CLINICIAN REVIEW REQUIRED.**
"""


doctor = SimulatedDoctor()

edited = doctor.review(draft)

print("\nORIGINAL DRAFT\n")
print(draft)

print("\nEDITED VERSION\n")
print(edited)