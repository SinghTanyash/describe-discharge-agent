ocr_medications = [
    "TAB. ENTR 10 3 DAYS",
    "TAB. RACIPER 40MG 1-0-0 7 DAYS"
]

normalized = [
    {
        "name": "ENTEROCIN",
        "frequency": "",
        "duration": "",
        "quantity": ""
    },
    {
        "name": "RACIPER 40MG",
        "frequency": "1-0-0",
        "duration": "7 DAYS",
        "quantity": ""
    }
]

ocr_text = " ".join(
    ocr_medications
).upper()

verified = []

for med in normalized:

    name = med["name"].upper()

    tokens = [
        token
        for token in name.split()
        if len(token) >= 4
    ]

    matched = False

    for token in tokens:

        if token in ocr_text:

            matched = True
            break

    if matched:

        verified.append(med)

    else:

        print(
            f"[REJECTED HALLUCINATION] {name}"
        )

print("\nVERIFIED\n")

for med in verified:

    print(med)