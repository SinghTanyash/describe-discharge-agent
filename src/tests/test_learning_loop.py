from tools.simulated_doctor import SimulatedDoctor
from tools.reward_calculator import RewardCalculator
from tools.learning_engine import LearningEngine
from tools.correction_learner import CorrectionLearner


doctor = SimulatedDoctor()
calculator = RewardCalculator()
engine = LearningEngine()
learner = CorrectionLearner()


draft = """
**DISCHARGE SUMMARY**

EMESET: for 3 DAYS

Review immediately in case of fever, loose stools, vomiting, or fatigue.

**CLINICIAN REVIEW REQUIRED.**
"""


for iteration in range(1, 4):

    print(f"\n{'='*50}")
    print(f"ITERATION {iteration}")
    print(f"{'='*50}")

    improved_draft = engine.improve(draft)

    edited_draft = doctor.review(
        improved_draft
    )
    learner.learn(
        improved_draft,
        edited_draft
    )
    reward = calculator.calculate(
        improved_draft,
        edited_draft
    )
    print("\nREWARD SCORE:")
    print(reward)

    print("\nDRAFT:")
    print(improved_draft)

    print("\nDOCTOR VERSION:")
    print(edited_draft)