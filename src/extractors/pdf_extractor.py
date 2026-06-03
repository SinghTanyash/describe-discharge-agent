import fitz
import pytesseract
from PIL import Image
import os


class PDFExtractor:
    def extract(self, pdf_path):
        return self.extract_text(pdf_path)

    def extract_text(self, pdf_path):

        doc = fitz.open(pdf_path)

        full_text = ""

        for page_num in range(len(doc)):

            page = doc[page_num]

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

            image_path = f"temp_page_{page_num}.png"

            pix.save(image_path)

            image = Image.open(image_path)

            page_text = pytesseract.image_to_string(image)

            full_text += f"\n--- PAGE {page_num+1} ---\n"
            full_text += page_text

            os.remove(image_path)

        return full_text