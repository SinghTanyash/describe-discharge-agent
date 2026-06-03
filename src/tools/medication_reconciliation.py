class MedicationReconciliation:

    def reconcile(
        self,
        admission_meds,
        discharge_meds
    ):

        results = []

        admission_names = {
            med.lower().strip()
            for med in admission_meds
        }

        discharge_names = set()

        for med in discharge_meds:

            if isinstance(med, dict):
                name = (
                    med.get("name", "")
                    .lower()
                    .strip()
                )
            else:
                name = (
                    str(med)
                    .lower()
                    .strip()
                )

            discharge_names.add(name)

        for med in discharge_names:

            if med not in admission_names:

                results.append(
                    f"NEW: {med}"
                )

        for med in admission_names:

            if med not in discharge_names:

                results.append(
                    f"STOPPED: {med}"
                )

        for med in admission_names:

            if med in discharge_names:

                results.append(
                    f"CONTINUED: {med}"
                )

        return results