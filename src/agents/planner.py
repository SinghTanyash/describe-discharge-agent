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
            "medication_extractor"
            not in state.completed_tools
        ):
            return "medication_extractor"

        if (
            "followup_extractor"
            not in state.completed_tools
        ):
            return "followup_extractor"

        if (
            "hospital_course_extractor"
            not in state.completed_tools
        ):
            return "hospital_course_extractor"

        if (
            "pending_result_extractor"
            not in state.completed_tools
        ):
            return "pending_result_extractor"

        return "finish"