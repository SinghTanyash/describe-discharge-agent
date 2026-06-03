import json
import os


class CorrectionMemory:

    def __init__(self):

        self.memory_file = "memory/corrections.json"

        os.makedirs(
            "memory",
            exist_ok=True
        )

        if not os.path.exists(
            self.memory_file
        ):

            with open(
                self.memory_file,
                "w"
            ) as f:

                json.dump(
                    {},
                    f
                )

    def load(self):

        with open(
            self.memory_file,
            "r"
        ) as f:

            return json.load(f)

    def save(self, memory):

        with open(
            self.memory_file,
            "w"
        ) as f:

            json.dump(
                memory,
                f,
                indent=4
            )

    def remember(
        self,
        mistake,
        correction
    ):

        memory = self.load()

        memory[mistake] = correction

        self.save(memory)

    def get_correction(
        self,
        mistake
    ):

        memory = self.load()

        return memory.get(
            mistake
        )

    def get_all(self):

        return self.load()