import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class LLMSummaryGenerator:

    def generate(
        self,
        diagnoses,
        medications,
        followups,
        hospital_course,
        pending_results,
        requires_review
    ):

        prompt = f"""
You are a clinical discharge summary assistant.

Generate a professional discharge summary.

IMPORTANT:
- Never invent patient information.
- Never create MRN, DOB, admission date, discharge date, age, gender, clinician names or identifiers.
- If information is unavailable, omit it entirely.
- Only use information explicitly provided.

DIAGNOSES:
{diagnoses}

DISCHARGE MEDICATIONS:
{medications}

FOLLOW UP INSTRUCTIONS:
{followups}

HOSPITAL COURSE:
{hospital_course}

PENDING RESULTS:
{pending_results}

CLINICIAN REVIEW REQUIRED:
{requires_review}

Rules:
1. Do not invent facts.
2. Clearly list diagnoses.
3. Clearly list discharge medications.
4. Clearly list follow-up instructions.
5. Clearly mention pending results.
6. Mention clinician review requirement if applicable.
7. Use professional medical language.
8. Do not create placeholder sections.
9. Do not create Patient Information sections.
10. Only include sections for which data is provided.
"""

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(
            prompt
        )

        return response.text