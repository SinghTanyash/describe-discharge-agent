import re


class FollowupExtractor:

    def extract(self, text):

        followups = []

        match = re.search(
            r"FOLLOW-UP INSTRUCTIONS:(.*?)(?:--- PAGE|\Z)",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if not match:
            return followups

        section = match.group(1)

        lines = section.split("\n")

        for line in lines:

            line = line.strip()

            if line and len(line) > 5:
                followups.append(line)

        return followups