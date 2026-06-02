from agents.planner import Planner

from extractors.diagnosis_extractor import (
    DiagnosisExtractor
)

from extractors.medication_extractor import (
    MedicationExtractor
)

from extractors.pending_result_extractor import (
    PendingResultExtractor
)

from extractors.followup_extractor import (
    FollowupExtractor
)

from extractors.hospital_course_extractor import (
    HospitalCourseExtractor
)

class DischargeAgent:

    def run(self, text, state):

        planner = Planner()

        while state.current_step < state.max_steps:

            tool = planner.choose_next_tool(state)

            print(
                f"\n[STEP {state.current_step + 1}] Running: {tool}"
            )

            if tool == "finish":

                print(
                    "[AGENT] All tasks completed"
                )

                break

            if tool == "diagnosis_extractor":

                diagnoses = (
                    DiagnosisExtractor().extract(text)
                )

                state.diagnoses = diagnoses

                state.completed_tools.append(
                    "diagnosis_extractor"
                )

                state.execution_trace.append(
                    "Diagnosis extraction completed"
                )

                print(
                    f"[AGENT] Found {len(diagnoses)} diagnoses"
                )

            elif tool == "medication_extractor":

                medications = (
                    MedicationExtractor().extract(text)
                )

                state.medications = medications

                state.completed_tools.append(
                    "medication_extractor"
                )

                state.execution_trace.append(
                    "Medication extraction completed"
                )

                print(
                    f"[AGENT] Found {len(medications)} medications"
                )

            elif tool == "followup_extractor":

                followups = (
                FollowupExtractor().extract(text)
                )

                state.followups = followups

                state.completed_tools.append(
                    "followup_extractor"
                )

                state.execution_trace.append(
                    "Follow-up extraction completed"
                )

                print(
                    f"[AGENT] Found {len(followups)} followups"
                )

            elif tool == "hospital_course_extractor":

                hospital_course = (
                    HospitalCourseExtractor().extract(text)
                )

                hospital_course = hospital_course.replace(
                    "--- PAGE 2 ---",
                    ""
                ).strip()

                state.hospital_course = (
                    hospital_course
                )

                state.completed_tools.append(
                    "hospital_course_extractor"
                )

                state.execution_trace.append(
                    "Hospital course extraction completed"
                )

                print(
                    "[AGENT] Hospital course extracted"
                )

            elif tool == "pending_result_extractor":

                pending_results = (
                    PendingResultExtractor().extract(text)
                )

                pending_results = list(
                    set(pending_results)
                )

                state.pending_results = (
                    pending_results
                )

                if pending_results:
                    state.requires_review = True

                state.completed_tools.append(
                    "pending_result_extractor"
                )

                state.execution_trace.append(
                    "Pending result extraction completed"
                )

                print(
                    f"[AGENT] Found {len(pending_results)} pending results"
                )

            state.current_step += 1

        print(
            f"\n[AGENT] Finished after {state.current_step} steps"
        )

        return state