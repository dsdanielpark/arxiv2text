import os
import io
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def arxiv_to_md(pdf_url, output_folder):
    # Extract the last part of the PDF URL to use as the filename
    filename = pdf_url.split("/")[-1] + ".md"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, filename)

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

    # Find the start and end of the Abstract and Introduction sections
    start_abstract = extracted_text.find("Abstract")
    start_introduction = extracted_text.find("Introduction")
    end_abstract = start_introduction if start_introduction != -1 else None

    # Extract Abstract and Introduction sections
    abstract = extracted_text[start_abstract:end_abstract].strip()
    introduction = extracted_text[start_introduction:].strip() if start_introduction != -1 else ""

    # Save the Abstract and Introduction as Markdown
    markdown_text = f"# {abstract}\n\n# {introduction}"

    # Save the Markdown content to the specified file
    with open(output_path, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_text)

    print("Markdown content saved to", output_path)