import fitz

pdf_path = "data/patient_2/Patient 2.pdf"

doc = fitz.open(pdf_path)

print(f"Pages: {len(doc)}")

total_text = ""

for page_num, page in enumerate(doc):
    text = page.get_text()

    if text.strip():
        print(f"Page {page_num + 1}: {len(text)} characters")

    total_text += text

print("\nTotal extracted characters:", len(total_text))