import re


class AllergyExtractor:

    def extract(
        self,
        text
    ):

        allergies = []

        lower_text = text.lower()

        no_allergy_patterns = [

            "no known drug allergy",

            "no known drug allergies",

            "not known",

            "nkda",

            "nka",

            "no drug allergy"
        ]

        for pattern in no_allergy_patterns:

            if pattern in lower_text:

                return [
                    "No Known Drug Allergy"
                ]

        patterns = [

            r"allergic to\s+([^\n\.]+)",

            r"drug allergy\s*[:\-]\s*([^\n]+)",

            r"allergies\s*[:\-]\s*([^\n]+)",

            r"allergy\s*[:\-]\s*([^\n]+)"
        ]

        for pattern in patterns:

            matches = re.findall(
                pattern,
                text,
                re.IGNORECASE
            )

            for match in matches:

                match = match.strip()

                if len(match) < 3:
                    continue

                allergies.append(
                    match
                )

        if allergies:

            return list(
                set(allergies)
            )

        return []