import re


class DischargeSummarySectionExtractor:

    def extract(self, text):

        pattern = (
            r"DIAGNOSIS:(.*?)FOLLOW-UP INSTRUCTIONS:.*?(?:CBC|$)"
        )

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        if match:

            return match.group(0).strip()

        return text