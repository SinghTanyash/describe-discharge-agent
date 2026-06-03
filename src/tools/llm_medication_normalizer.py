import os
import json

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class LLMMedicationNormalizer:

    def normalize(
        self,
        medications
    ):

        prompt = f"""
You are a clinical medication extraction assistant.

The following medications were extracted from OCR.

Clean OCR formatting only.

IMPORTANT RULES:

1. Never invent a medication name.
2. Never expand abbreviations into a different drug.
3. Never guess missing letters.
4. If OCR text is unclear, preserve it exactly.
5. Keep medication names as close as possible to the OCR.
6. Do not replace a medication with another medication.
7. If uncertain, keep the original OCR wording.

Medications:
{medications}

Return ONLY a JSON array.

Example:

[
  {{
    "name": "RACIPER 40MG",
    "frequency": "1-0-0",
    "duration": "7 DAYS",
    "quantity": ""
  }}
]

Do not include explanations.
Do not use markdown.
Return valid JSON only.
"""

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(
            prompt
        )

        print("\n=== GEMINI RAW RESPONSE ===\n")
        print(response.text)
        print("\n===========================\n")

        try:

            normalized = json.loads(
                response.text
            )

        except Exception as e:

            print(
                f"[NORMALIZATION ERROR] {e}"
            )

            return []

        ocr_text = " ".join(
            medications
        ).upper()

        verified = []

        for med in normalized:

            name = (
                med.get(
                    "name",
                    ""
                )
                .upper()
                .strip()
            )

            if not name:
                continue

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

                verified.append(
                    med
                )

            else:

                print(
                    f"[REJECTED HALLUCINATION] {name}"
                )

        return verified