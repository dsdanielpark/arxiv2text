import io
import requests
import tempfile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from bs4 import BeautifulSoup
import os


def arxiv_to_html(pdf_url: str, output_folder: str) -> None:
    """
    Convert a PDF from an arXiv URL to an HTML file and save it in the specified folder.

    Args:
        pdf_url (str): The URL of the PDF on arXiv.
        output_folder (str): The folder where the HTML file will be saved.

    Returns:
        None

    Example:
    >>> pdf_url = "https://arxiv.org/pdf/2310.06825"
    >>> output_folder = "output"
    >>> arxiv_to_html(pdf_url, output_folder)
    """
    response = requests.get(pdf_url)
    pdf_file = io.BytesIO(response.content)

    resource_manager = PDFResourceManager()

    laparams = LAParams()
    laparams.box_width = 1000

    codec = 'utf-8'
    output_file = tempfile.NamedTemporaryFile(delete=False)

    fontsize = 10
    laparams.char_margin = fontsize * 1.5
    laparams.all_texts = True

    html_converter = HTMLConverter(resource_manager, output_file, codec=codec, laparams=laparams, layoutmode="exact", scale=1)
    interpreter = PDFPageInterpreter(resource_manager, html_converter)

    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)

    html_converter.close()

    with open(output_file.name, 'r', encoding=codec) as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')
    style = soup.new_tag('style')
    style.string = f'.ltxt {{font-size: {fontsize}px;}}'
    soup.head.append(style)

    # Extract the last part of the PDF URL to use as the filename
    filename = pdf_url.split("/")[-1] + ".html"
    output_path = os.path.join(output_folder, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print("HTML content saved to", output_path)
