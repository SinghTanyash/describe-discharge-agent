import re


class PendingResultExtractor:

    def extract(self, text):

        pending_results = []

        patterns = [
            r".*report awaited.*",
            r".*pending.*",
            r".*awaited.*"
        ]

        for line in text.split("\n"):

            for pattern in patterns:

                if re.search(pattern, line, re.IGNORECASE):

                    pending_results.append(
                        line.strip()
                    )

        return list(set(pending_results))
    