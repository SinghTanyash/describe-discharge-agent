class Planner:

    def choose_next_tool(self, state):

        print(
            f"[PLANNER] Completed tools: {state.completed_tools}"
        )

        if (
            "diagnosis_extractor"
            not in state.completed_tools
        ):
            return "diagnosis_extractor"

        if (
            "demographics_extractor"
            not in state.completed_tools
        ):
            return "demographics_extractor"

        if (
            "date_extractor"
            not in state.completed_tools
        ):
            return "date_extractor"

        if (
            "procedure_extractor"
            not in state.completed_tools
        ):
            return "procedure_extractor"

        if (
            "medication_extractor"
            not in state.completed_tools
        ):
            return "medication_extractor"

        if (
            "medication_reconciliation"
            not in state.completed_tools
        ):
            return "medication_reconciliation"

        if (
            "drug_interaction_checker"
            not in state.completed_tools
        ):
            return "drug_interaction_checker"

        if (
            "followup_extractor"
            not in state.completed_tools
        ):
            return "followup_extractor"

        if (
            "allergy_extractor"
            not in state.completed_tools
        ):
            return "allergy_extractor"

        if (
            "hospital_course_extractor"
            not in state.completed_tools
        ):
            return "hospital_course_extractor"

        if (
            "discharge_condition_extractor"
            not in state.completed_tools
        ):
            return "discharge_condition_extractor"

        if (
            "pending_result_extractor"
            not in state.completed_tools
        ):
            return "pending_result_extractor"

        if (
            "summary_generator"
            not in state.completed_tools
        ):
            return "summary_generator"

        if (
            "clinician_review_generator"
            not in state.completed_tools
        ):
            return "clinician_review_generator"

        return "finish"