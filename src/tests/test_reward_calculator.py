from tools.simulated_doctor import SimulatedDoctor
from tools.reward_calculator import RewardCalculator


draft = """
**DISCHARGE SUMMARY**

EMESET: for 3 DAYS

Review immediately in case of fever, loose stools, vomiting, or fatigue.

**CLINICIAN REVIEW REQUIRED.**
"""


doctor = SimulatedDoctor()
edited = doctor.review(draft)

calculator = RewardCalculator()

reward = calculator.calculate(
    draft,
    edited
)

print("\nREWARD SCORE\n")
print(reward)