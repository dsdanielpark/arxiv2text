import os
import io
import requests
from typing import Optional
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def arxiv_to_text(pdf_url: str, output_folder: Optional[str] = None) -> str:
    """
    Extract text content from a PDF file located at the specified URL. Optionally saves the extracted text to a file.

    Args:
        pdf_url (str): The URL of the PDF file to extract text from.
        output_folder (Optional[str]): The folder where the extracted text file will be saved. If None, the text file is not saved.

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

    # Save the text to a file if output_folder is specified
    if output_folder:
        os.makedirs(output_folder, exist_ok=True)
        file_name = os.path.join(output_folder, pdf_url.split('/')[-1] + '.txt')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        print(f"Extracted text saved to {file_name}")

    return extracted_text
