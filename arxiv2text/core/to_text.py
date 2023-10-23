import io
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def arxiv_to_text(pdf_url: str) -> str:
    """
    Extract text content from a PDF file located at the specified URL.

    Args:
        pdf_url (str): The URL of the PDF file to extract text from.

    Returns:
        str: The extracted text content from the PDF.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request to the URL.
    """
    response = requests.get(pdf_url)
    pdf_file = io.BytesIO(response.content)

    resource_manager = PDFResourceManager()
    text_stream = io.StringIO()
    laparams = LAParams()

    device = TextConverter(resource_manager, text_stream, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)
    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)

    extracted_text = text_stream.getvalue()
    text_stream.close()

    return extracted_text
