import re


class MedicationExtractor:

    def extract(self, text):

        medications = []

        match = re.search(
            r"ADVICE ON DISCHARGE:(.*?)FOLLOW-UP INSTRUCTIONS:",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if not match:
            return medications

        section = match.group(1)

        lines = section.split("\n")

        for line in lines:

            line = line.strip()

            line = re.sub(
                r"\s+",
                " ",
                line
            )

            if (
                "TAB" in line.upper()
                or "CAP" in line.upper()
                or "INJ" in line.upper()
            ):

                line = line.replace("100", "")
                line = line.replace("IS DAYS", "15 DAYS")
                line = line.replace("ITABSOS", "TABLETS")
                line = line.replace("Zz", "")
                line = line.replace("‘", "")
                line = line.replace("|", "")

                line = re.sub(
                    r"\s+",
                    " ",
                    line
                ).strip()

                medicine_match = re.search(
                    r"(?:TAB|CAP|INJ)\.?\s+([A-Z0-9\s\-]+)",
                    line,
                    re.IGNORECASE
                )

                if medicine_match:

                    medicine = (
                        medicine_match.group(1)
                        .strip()
                    )

                    medications.append(
                        medicine
                    )

        medications = list(
            set(medications)
        )

        return medications