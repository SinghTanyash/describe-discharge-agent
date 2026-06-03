import re


class DischargeConditionExtractor:

    def extract(self, text):

        pattern = (
            r"CONDITION AT DISCHARGE:\s*(.*?)\s*ADVICE ON DISCHARGE:"
        )

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        if match:

            return match.group(1).strip()

        return "Not documented"