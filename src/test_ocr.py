import fitz
import pytesseract
from PIL import Image

pdf_path = "data/patient_2/Patient 2.pdf"

doc = fitz.open(pdf_path)

page = doc[0]  # first page

pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

img_path = "page1.png"
pix.save(img_path)

image = Image.open(img_path)

text = pytesseract.image_to_string(image)

print("=" * 50)
print("OCR OUTPUT")
print("=" * 50)
print(text[:5000])