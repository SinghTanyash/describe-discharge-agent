import re


class DemographicsExtractor:

    def extract(self, text):

        demographics = {
            "name": "Missing - clinician review required",
            "age": "Missing - clinician review required",
            "gender": "Missing - clinician review required"
        }

        # ----------------------------
        # NAME EXTRACTION
        # ----------------------------

        name_patterns = [

            r"Patient\s+Name\s*[:\-]?\s*([A-Za-z .]+)",
            r"Name\s+of\s+Patient\s*[:\-]?\s*([A-Za-z .]+)",
            r"Pt\s+Name\s*[:\-]?\s*([A-Za-z .]+)",
            r"Name\s*[:\-]?\s*([A-Za-z ]{2,50})"
        ]

        invalid_names = [
            "Frequency Duration",
            "Frequency  Duration",
            "Consultant Signature",
            "DISCHARGE STAFFS NAME",
            "FULL NAME",
            "Medication Name",
            "Diagnosis",
            "Address"
        ]

        for pattern in name_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                candidate = (
                    match.group(1)
                    .strip()
                    .replace("\n", " ")
                )
                candidate = candidate.split("\n")[0].strip()

                candidate = re.sub(
                    r"\s+",
                    " ",
                    candidate
                )

                if (
                    len(candidate) > 2
                    and len(candidate.split()) <= 4
                    and candidate not in invalid_names
                ):

                    demographics["name"] = candidate
                    break

        # ----------------------------
        # AGE EXTRACTION
        # ----------------------------

        age_patterns = [
            r"\b(\d{1,3})\s*years?\b",
            r"Age\s*[:\-]?\s*(\d{1,3})",
        ]

        for pattern in age_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                age = match.group(1)

                try:

                    age_int = int(age)

                    if 0 < age_int < 120:

                        demographics["age"] = age
                        break

                except ValueError:
                    pass

        # ----------------------------
        # GENDER EXTRACTION
        # ----------------------------

        gender_patterns = [

            r"\bMale\b",
            r"\bFemale\b",
            r"\bM\/F\b",
            r"\bSex\s*[:\-]?\s*(Male|Female)\b"
        ]

        for pattern in gender_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                if match.group(0).lower() == "male":
                    demographics["gender"] = "Male"

                elif match.group(0).lower() == "female":
                    demographics["gender"] = "Female"

                elif len(match.groups()) > 0:
                    demographics["gender"] = match.group(1)

                break

        return demographics