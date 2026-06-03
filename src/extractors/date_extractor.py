import re


class DateExtractor:

    def extract(
        self,
        text
    ):

        dates = {
            "admission_date":
                "Missing - clinician review required",

            "discharge_date":
                "Missing - clinician review required"
        }

        date_pattern = (
            r"(\d{1,2}[\/\-.]\d{1,2}[\/\-.]\d{2,4})"
        )

        admission_patterns = [

            rf"Date\s+Of\s+Admission.*?{date_pattern}",

            rf"Admission\s+Date.*?{date_pattern}",

            rf"DOA.*?{date_pattern}",

            rf"Admitted\s+On.*?{date_pattern}",

            rf"Date\s*&\s*Time\s*of\s*Nursing\s*Initial\s*Assessment.*?{date_pattern}"
        ]

        discharge_patterns = [

            rf"Date\s+Of\s+Discharge.*?{date_pattern}",

            rf"Discharge\s+Date.*?{date_pattern}",

            rf"DOD.*?{date_pattern}",

            rf"Discharged\s+On.*?{date_pattern}"
        ]

        for pattern in admission_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if match:

                dates["admission_date"] = (
                    match.group(1)
                )

                break

        for pattern in discharge_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if match:

                dates["discharge_date"] = (
                    match.group(1)
                )

                break

        if (
            dates["admission_date"]
            ==
            "Missing - clinician review required"
        ):

            all_dates = re.findall(
                date_pattern,
                text
            )

            if len(all_dates) >= 1:

                dates["admission_date"] = (
                    all_dates[0]
                )

        if (
            dates["discharge_date"]
            ==
            "Missing - clinician review required"
        ):

            all_dates = re.findall(
                date_pattern,
                text
            )

            if len(all_dates) >= 2:

                dates["discharge_date"] = (
                    all_dates[-1]
                )

        return dates