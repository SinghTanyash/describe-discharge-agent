from tools.medication_reconciliation import (
    MedicationReconciliation
)

admission_meds = [
    "THYROXINE",
    "PARACETAMOL",
    "VITAMIN D"
]

discharge_meds = [
    {
        "name": "THYROXINE"
    },
    {
        "name": "RACIPER 40MG"
    }
]

results = (
    MedicationReconciliation()
    .reconcile(
        admission_meds,
        discharge_meds
    )
)

print("\nRECONCILIATION RESULTS\n")

for item in results:
    print("-", item)