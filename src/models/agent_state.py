from pydantic import BaseModel
from typing import List


class AgentState(BaseModel):

    diagnoses: List[str] = []

    pending_results: List[str] = []

    medications: List[str] = []

    followups: List[str] = []

    execution_trace: List[str] = []

    hospital_course: str = ""

    completed_tools: List[str] = []

    current_task: str = ""

    requires_review: bool = False

    max_steps: int = 10

    current_step: int = 0