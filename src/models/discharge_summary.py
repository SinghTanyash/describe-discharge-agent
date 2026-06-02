from pydantic import BaseModel
from typing import List


class DischargeSummary(BaseModel):

    diagnoses: List[str] = []

    pending_results: List[str] = []

    discharge_medications: List[str] = []

    follow_up_instructions: List[str] = []

    discharge_condition: str = ""

    requires_clinician_review: bool = False