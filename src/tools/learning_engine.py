from tools.correction_memory import CorrectionMemory


class LearningEngine:

    def __init__(self):

        self.memory = CorrectionMemory()

    def improve(
        self,
        draft
    ):

        improved_draft = draft

        corrections = self.memory.get_all()

        for mistake, correction in corrections.items():

            improved_draft = improved_draft.replace(
                mistake,
                correction
            )

        return improved_draft