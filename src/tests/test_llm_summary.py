from models.agent_state import AgentState
from agents.discharge_agent import DischargeAgent

from tools.llm_summary_generator import (
    LLMSummaryGenerator
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

state = AgentState()

agent = DischargeAgent()

final_state = agent.run(
    text=text,
    state=state
)

summary = LLMSummaryGenerator().generate(
    diagnoses=final_state.diagnoses,
    medications=final_state.medications,
    followups=final_state.followups,
    hospital_course=final_state.hospital_course,
    pending_results=final_state.pending_results,
    requires_review=final_state.requires_review
)

print("\n")
print("=" * 60)
print("ENHANCED DISCHARGE SUMMARY")
print("=" * 60)
print(summary)