from pydantic import BaseModel
from typing import List
from models.medication import Medication


class AgentState(BaseModel):

    diagnoses: List[str] = []

    procedures: List[str] = []

    demographics: dict = {}

    dates: dict = {}

    pending_results: List[str] = []

    medications: List[Medication] = []

    medication_reconciliation: List[str] = []

    followups: List[str] = []

    allergies: List[str] = []

    execution_trace: List[str] = []

    hospital_course: str = ""

    discharge_condition: str = ""

    completed_tools: List[str] = []

    conflicts: list = []

    summary: str = ""

    errors: List[str] = []

    warnings: List[str] = []

    review_items: List[str] = []

    drug_interaction_warnings: List[str] = []

    current_task: str = ""

    requires_review: bool = False

    max_steps: int = 20

    current_step: int = 0