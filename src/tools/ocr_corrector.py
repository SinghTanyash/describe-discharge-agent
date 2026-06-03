import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class OCRCorrector:

    def correct(
        self,
        text
    ):

        prompt = f"""
You are correcting OCR errors in a hospital discharge summary.

Rules:
- Fix OCR spelling mistakes.
- Preserve medical meaning.
- Do not invent information.
- Do not remove information.
- Keep formatting as similar as possible.
- Return corrected text only.

TEXT:

{text}
"""

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(
            prompt
        )

        return response.text