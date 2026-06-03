from tools.llm_medication_normalizer import (
    LLMMedicationNormalizer
)

medications = [
    "TAB. RACIPER 40MG 1-0-0 7 DAYS",
    "TAB. ENTR¢ 10 -] 3 DAYS",
    "TAB. MEFTAL SPAS TABLETS 4TABLETS"
]

result = (
    LLMMedicationNormalizer()
    .normalize(medications)
)

print(result)