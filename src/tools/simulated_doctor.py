import re


class SimulatedDoctor:

    def review(self, draft):

        edited = draft

        # Doctor policy 1:
        # Ensure clinician review wording is standardized

        edited = edited.replace(
            "**CLINICIAN REVIEW REQUIRED.**",
            "**CLINICIAN REVIEW REQUIRED:** Yes"
        )

        # Doctor policy 2:
        # Standardize medication duration wording

        edited = re.sub(
            r": for (\d+\s*DAYS)",
            r": Duration \1",
            edited,
            flags=re.IGNORECASE
        )

        # Doctor policy 3:
        # Standardize follow-up wording

        edited = edited.replace(
            "Review immediately in case of fever, loose stools, vomiting, or fatigue.",
            "Review immediately in case of fever, loose stools, vomiting, fatigue."
        )

        # Doctor policy 4:
        # Add CBC if review date present but CBC missing

        if (
            "Review on" in edited
            and "CBC" not in edited
        ):
            edited += "\n\nCBC to be done."

        return edited