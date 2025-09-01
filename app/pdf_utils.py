from pypdf import PdfReader
from io import BytesIO
import fitz 
import pytesseract
from PIL import Image

def extract_text_from_pdf(file):
    """Extracts text from a PDF file, including OCR for images.

    Args:
        file: A file-like object containing the PDF data.

    Returns:
        A string containing the extracted text.
    """
    text = ""

    # 1. Extract normal text using pypdf
    reader = PdfReader(file)
    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + "\n"

    # 2. Re-open the file for image extraction using PyMuPDF
    file.seek(0)  # Reset pointer
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(BytesIO(image_bytes))

            # OCR using pytesseract
            ocr_text = pytesseract.image_to_string(image)
            if ocr_text.strip():
                text += "\n[Image Text]\n" + ocr_text + "\n"

    return text.strip()
