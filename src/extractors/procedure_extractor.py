import re


class ProcedureExtractor:

    def extract(
        self,
        text
    ):

        procedures = []

        procedure_patterns = {
            r"USG\s+abdomen\s+and\s+pelvis":
                "USG abdomen and pelvis",

            r"urine\s+culture\s+and\s+sensitivity":
                "Urine culture and sensitivity",

            r"stool\s+routine":
                "Stool routine",

            r"TSH":
                "TSH",

            r"Free\s*T4":
                "Free T4",

            r"Serum\s+Creatinine":
                "Serum Creatinine",

            r"Urine\s+routine":
                "Urine routine"
        }

        for pattern, label in (
            procedure_patterns.items()
        ):

            if re.search(
                pattern,
                text,
                re.IGNORECASE
            ):

                procedures.append(
                    label
                )

        return list(
            set(procedures)
        )