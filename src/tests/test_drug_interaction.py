from tools.drug_interaction_checker import (
    DrugInteractionChecker
)

medications = [

    {
        "name": "WARFARIN"
    },

    {
        "name": "ASPIRIN"
    },

    {
        "name": "RACIPER 40MG"
    }

]

warnings = (
    DrugInteractionChecker()
    .check(medications)
)

print("\nINTERACTIONS FOUND\n")

for warning in warnings:
    print("-", warning)