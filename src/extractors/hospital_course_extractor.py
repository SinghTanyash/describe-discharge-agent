import re


class HospitalCourseExtractor:

    def extract(self, text):

        match = re.search(
            r"COURSE IN THE HOSPITAL:(.*?)CONDITION AT DISCHARGE:",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if not match:
            return ""

        course = match.group(1)

        course = re.sub(
            r"\s+",
            " ",
            course
        ).strip()

        return course