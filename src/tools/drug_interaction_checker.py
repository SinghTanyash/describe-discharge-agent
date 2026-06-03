class DrugInteractionChecker:

    def check(
        self,
        medications
    ):

        warnings = []

        medication_names = []

        for med in medications:

            if isinstance(
                med,
                dict
            ):
                medication_names.append(
                    med.get(
                        "name",
                        ""
                    ).upper()
                )

        interaction_rules = [

            (
                "WARFARIN",
                "ASPIRIN",
                "Potential bleeding risk"
            ),

            (
                "WARFARIN",
                "CLOPIDOGREL",
                "Potential bleeding risk"
            ),

            (
                "IBUPROFEN",
                "ASPIRIN",
                "Potential gastrointestinal bleeding risk"
            ),

            (
                "METFORMIN",
                "CONTRAST",
                "Potential kidney injury risk"
            )

        ]

        for (
            drug1,
            drug2,
            warning
        ) in interaction_rules:

            if (
                drug1 in medication_names
                and
                drug2 in medication_names
            ):

                warnings.append(
                    f"{drug1} + {drug2}: {warning}"
                )

        return warnings