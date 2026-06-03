from difflib import SequenceMatcher


class RewardCalculator:

    def calculate(
        self,
        draft,
        edited
    ):

        similarity = SequenceMatcher(
            None,
            draft,
            edited
        ).ratio()

        reward = round(
            similarity,
            4
        )

        return reward