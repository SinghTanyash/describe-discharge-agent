class ConflictDetector:

    def detect(
        self,
        diagnoses,
        hospital_course
    ):

        conflicts = []

        hospital_course = hospital_course.lower()

        if (
            "colitis" in hospital_course
            and not any(
                "colitis" in d.lower()
                for d in diagnoses
            )
        ):

            conflicts.append(
                "Possible diagnosis mismatch: Hospital course mentions colitis but discharge diagnosis does not."
            )

        return conflicts