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

from extractors.date_extractor import (
    DateExtractor
)

from tools.llm_summary_generator import (
    LLMSummaryGenerator
)

from extractors.followup_extractor import (
    FollowupExtractor
)

from tools.medication_reconciliation import (
    MedicationReconciliation
)

from extractors.hospital_course_extractor import (
    HospitalCourseExtractor
)

from extractors.procedure_extractor import (
    ProcedureExtractor
)

from tools.clinician_review_generator import (
    ClinicianReviewGenerator
)

from tools.ocr_corrector import (
    OCRCorrector
)

from extractors.discharge_condition_extractor import (
    DischargeConditionExtractor
)

from extractors.discharge_summary_section_extractor import (
    DischargeSummarySectionExtractor
)

from tools.drug_interaction_checker import (
    DrugInteractionChecker
)

from extractors.allergy_extractor import (
    AllergyExtractor
)

from extractors.demographics_extractor import (
    DemographicsExtractor
)

from tools.data_cleaner import DataCleaner

from tools.conflict_detector import (
    ConflictDetector
)

from tools.llm_medication_normalizer import (
    LLMMedicationNormalizer
)


class DischargeAgent:

    def run(self, text, state):

        text = (
            DischargeSummarySectionExtractor()
            .extract(text)
        )

        try:
            text = (
                OCRCorrector()
                .correct(text)
            )

            print(
                "[AGENT] OCR correction completed"
            )

        except Exception as e:

            print(
                f"[AGENT] OCR correction failed: {e}"
            )

        planner = Planner()

        while state.current_step < state.max_steps:

            tool = planner.choose_next_tool(
                state
            )

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
                    DiagnosisExtractor()
                    .extract(text)
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

            elif tool == "demographics_extractor":

                demographics = (
                    DemographicsExtractor()
                    .extract(text)
                )

                state.demographics = demographics

                if (
                    "Missing" in demographics["name"]
                    or
                    "Missing" in demographics["age"]
                    or
                    "Missing" in demographics["gender"]
                ):

                    state.requires_review = True

                state.completed_tools.append(
                    "demographics_extractor"
                )

                state.execution_trace.append(
                    "Demographics extraction completed"
                )

                print(
                    "[AGENT] Demographics extracted"
                )

            elif tool == "date_extractor":

                dates = (
                    DateExtractor().extract(text)
                )

                state.dates = dates

                if (
                    "Missing" in dates["admission_date"]
                    or
                    "Missing" in dates["discharge_date"]
                ):
                    state.requires_review = True

                state.completed_tools.append(
                    "date_extractor"
                )

                state.execution_trace.append(
                    "Date extraction completed"
                )

                print(
                    "[AGENT] Dates extracted"
                )

            elif tool == "medication_extractor":

                medications = (
                    MedicationExtractor()
                    .extract(text)
                )

                medications = (
                    DataCleaner()
                    .clean_medications(
                        medications
                    )
                )

                medications = (
                    DataCleaner()
                    .structure_medications(
                        medications
                    )
                )

                try:

                    medications = (
                        LLMMedicationNormalizer()
                        .normalize(medications)
                    )

                except Exception as e:

                    print(
                        f"[AGENT] LLM medication normalization failed: {e}"
                    )

                    pass

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

            elif tool == "medication_reconciliation":

                admission_meds = []

                reconciliation = (
                    MedicationReconciliation()
                    .reconcile(
                        admission_meds,
                        state.medications
                    )
                )

                state.medication_reconciliation = (
                    reconciliation
                )

                state.completed_tools.append(
                    "medication_reconciliation"
                )

                state.execution_trace.append(
                    "Medication reconciliation completed"
                )

                print(
                    f"[AGENT] Found {len(reconciliation)} reconciliation items"
                )

            elif tool == "drug_interaction_checker":

                interaction_warnings = (
                    DrugInteractionChecker()
                    .check(
                        state.medications
                    )
                )

                state.drug_interaction_warnings = (
                    interaction_warnings
                )

                if interaction_warnings:

                    state.requires_review = True

                    state.warnings.extend(
                        interaction_warnings
                    )

                state.completed_tools.append(
                    "drug_interaction_checker"
                )

                state.execution_trace.append(
                    "Drug interaction check completed"
                )

                print(
                    f"[AGENT] Found {len(interaction_warnings)} interaction warnings"
                )

            elif tool == "followup_extractor":

                followups = (
                    FollowupExtractor()
                    .extract(text)
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

            elif tool == "procedure_extractor":

                procedures = (
                    ProcedureExtractor().extract(text)
                )

                state.procedures = procedures

                state.completed_tools.append(
                    "procedure_extractor"
                )

                state.execution_trace.append(
                    "Procedure extraction completed"
                )

                print(
                    f"[AGENT] Found {len(procedures)} procedures"
                )

            elif tool == "allergy_extractor":

                allergies = (
                    AllergyExtractor()
                    .extract(text)
                )

                if not allergies:

                    allergies = [
                        "Missing - clinician review required"
                    ]

                    state.requires_review = True

                state.allergies = allergies

                state.completed_tools.append(
                    "allergy_extractor"
                )

                state.execution_trace.append(
                    "Allergy extraction completed"
                )

                print(
                    f"[AGENT] Found {len(allergies)} allergies"
                )

            elif tool == "hospital_course_extractor":

                hospital_course = (
                    HospitalCourseExtractor()
                    .extract(text)
                )

                hospital_course = (
                    hospital_course.replace(
                        "--- PAGE 2 ---",
                        ""
                    ).strip()
                )

                hospital_course = (
                    DataCleaner()
                    .clean_hospital_course(
                        hospital_course
                    )
                )

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

            elif tool == "discharge_condition_extractor":

                discharge_condition = (
                    DischargeConditionExtractor()
                    .extract(text)
                )

                state.discharge_condition = (
                    discharge_condition
                )

                state.completed_tools.append(
                    "discharge_condition_extractor"
                )

                state.execution_trace.append(
                    "Discharge condition extraction completed"
                )

                print(
                    f"[AGENT] Discharge condition: {discharge_condition}"
                )

            elif tool == "clinician_review_generator":

                review_items = (
                    ClinicianReviewGenerator()
                    .generate(state)
                )

                state.review_items = (
                    review_items
                )

                state.completed_tools.append(
                    "clinician_review_generator"
                )

                state.execution_trace.append(
                    "Clinician review generation completed"
                )

                print(
                    f"[AGENT] Found {len(review_items)} review items"
                )

            elif tool == "summary_generator":

                try:

                    summary = (
                        LLMSummaryGenerator()
                        .generate(
                            diagnoses=state.diagnoses,
                            medications=state.medications,
                            followups=state.followups,
                            hospital_course=state.hospital_course,
                            pending_results=state.pending_results,
                            requires_review=state.requires_review
                        )
                    )

                    state.summary = summary

                    print(
                        "[AGENT] Summary generated"
                    )

                except Exception as e:

                    print(
                        f"[AGENT] Summary generation failed: {e}"
                    )

                    state.summary = (
                        "Summary generation failed"
                    )

                state.completed_tools.append(
                    "summary_generator"
                )

                state.execution_trace.append(
                    "Summary generation completed"
                )

            elif tool == "pending_result_extractor":

                pending_results = (
                    PendingResultExtractor()
                    .extract(text)
                )

                pending_results = (
                    DataCleaner()
                    .clean_pending_results(
                        pending_results
                    )
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

                conflicts = (
                    ConflictDetector()
                    .detect(
                        state.diagnoses,
                        state.hospital_course
                    )
                )

                state.conflicts = conflicts

                if conflicts:

                    state.requires_review = True

                    state.execution_trace.append(
                        "Conflict detection completed"
                    )

                    print(
                        f"[AGENT] Found {len(conflicts)} conflicts"
                    )

            state.current_step += 1

        print(
            f"\n[AGENT] Finished after {state.current_step} steps"
        )

        return state