from tools.correction_memory import CorrectionMemory


class CorrectionLearner:

    def __init__(self):

        self.memory = CorrectionMemory()

    def learn(
        self,
        original_text,
        edited_text
    ):

        original_lines = [
            line.strip()
            for line in original_text.split("\n")
            if line.strip()
        ]

        edited_lines = [
            line.strip()
            for line in edited_text.split("\n")
            if line.strip()
        ]

        for old_line, new_line in zip(
            original_lines,
            edited_lines
        ):

            if old_line != new_line:

                self.memory.remember(
                    old_line,
                    new_line
                )

                print(
                    f"[LEARNED] {old_line} -> {new_line}"
                )