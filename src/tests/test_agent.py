from models.agent_state import AgentState
from agents.discharge_agent import DischargeAgent
from pprint import pprint

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

print("\nFINAL STATE\n")

pprint(final_state.model_dump())