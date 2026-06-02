import re


class DiagnosisExtractor:

    def extract(self, text):

        diagnoses = []

        pattern = r"DIAGNOSIS:(.*?)(?:HISTORY:|PAST HISTORY:)"

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        if match:

            diagnosis_block = match.group(1)

            lines = diagnosis_block.split("\n")

            for line in lines:

                line = line.strip()

                if line and any(ch.isalpha() for ch in line):
                    diagnoses.append(line)

        return diagnoses