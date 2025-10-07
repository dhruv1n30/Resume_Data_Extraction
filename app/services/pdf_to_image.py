import fitz  # PyMuPDF

from PIL import Image


def get_pdf_images(pdf_content: bytes) -> list[Image.Image]:
    """
    Convert PDF bytes to a list of PIL Images (one per page) using PyMuPDF.
    No Poppler dependency required.
    """
    try:
        # Open PDF from bytes
        pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
        images = []

        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pix = page.get_pixmap()  # Render page to image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)

        return images

    except Exception as e:
        raise ValueError(f"Failed to convert PDF to images: {str(e)}") from e
