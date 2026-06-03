import re

from models.medication import Medication


class DataCleaner:

    def clean_medications(
        self,
        medications
    ):

        cleaned = []

        for med in medications:

            med = med.replace("¢", "")
            med = med.replace("]", "")
            med = med.replace("—", "-")
            med = med.replace("=", "")

            med = re.sub(
                r"\s+",
                " ",
                med
            )

            cleaned.append(
                med.strip()
            )

        return list(set(cleaned))

    def clean_pending_results(
        self,
        pending_results
    ):

        cleaned = []

        for result in pending_results:

            result = result.lower()

            if "urine culture" in result:

                cleaned.append(
                    "Urine culture and sensitivity report awaited"
                )

        return list(set(cleaned))

    def clean_hospital_course(
        self,
        hospital_course
    ):

        hospital_course = hospital_course.replace(
            "bactreia",
            "bacteria"
        )

        hospital_course = hospital_course.replace(
            "1V ",
            "IV "
        )

        hospital_course = hospital_course.replace(
            "['V ",
            "IV "
        )

        hospital_course = hospital_course.replace(
            "Mlexure",
            "flexure"
        )

        hospital_course = hospital_course.replace(
            "adviced",
            "advised"
        )

        hospital_course = re.sub(
            r"\s+",
            " ",
            hospital_course
        )

        return hospital_course.strip()

    def structure_medications(
        self,
        medications
    ):

        structured = []

        for med in medications:

            frequency = ""
            duration = ""

            if "1-0-0" in med:
                frequency = "1-0-0"

            if "7 DAYS" in med:
                duration = "7 DAYS"

            elif "15 DAYS" in med:
                duration = "15 DAYS"

            elif "3 DAYS" in med:
                duration = "3 DAYS"

            name = med

            for token in [
                "1-0-0",
                "7 DAYS",
                "15 DAYS",
                "3 DAYS"
            ]:

                name = name.replace(
                    token,
                    ""
                )

            name = name.strip()

            quantity = ""

            quantity_match = re.search(
                r"(\d+)\s*TABLETS?",
                name,
                re.IGNORECASE
            )

            if quantity_match:

                quantity = quantity_match.group(1)

                name = re.sub(
                    r"\d+\s*TABLETS?",
                    "",
                    name,
                    flags=re.IGNORECASE
                ).strip()

            medication = Medication(
                name=self.normalize_medication_name(
                    name
                ),
                frequency=frequency,
                duration=duration,
                quantity=quantity
            )

            structured.append(
                medication
            )

        return structured

    def normalize_medication_name(
        self,
        name
    ):

        name = re.sub(
            r"\bTAB[.,]?\b",
            "",
            name,
            flags=re.IGNORECASE
        )

        name = re.sub(
            r"\bTABLETS?\b",
            "",
            name,
            flags=re.IGNORECASE
        )

        name = name.replace(
            "-",
            ""
        )

        name = re.sub(
            r"\s+",
            " ",
            name
        )

        return name.strip()