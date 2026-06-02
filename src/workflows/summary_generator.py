from models.discharge_summary import DischargeSummary


class SummaryGenerator:

    def generate(
        self,
        diagnoses,
        pending_results
    ):

        summary = DischargeSummary()

        summary.diagnoses = diagnoses

        summary.pending_results = pending_results

        summary.discharge_condition = (
            "Hemodynamically stable"
        )

        summary.requires_clinician_review = (
            len(pending_results) > 0
        )

        return summary