import os
import io
import requests
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

def arxiv_to_md(pdf_url: str, output_folder: str) -> str:
    """
    Extracts the Abstract and Introduction sections from a PDF from an arXiv URL
    and saves them as a Markdown file. The function returns the Markdown text as a string.

    Args:
        pdf_url (str): The URL of the PDF on arXiv.
        output_folder (str): The folder where the Markdown file will be saved.

    Returns:
        str: The Markdown text extracted from the PDF.

    Example:
    ```python
    pdf_url = "https://arxiv.org/pdf/2310.06825"
    output_folder = "output"
    markdown_text = arxiv_to_md(pdf_url, output_folder)
    ```
    """
    # Extract the last part of the PDF URL to use as the filename
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, pdf_url.split("/")[-1] + ".md")

    # Extract text from the PDF
    extracted_text = extract_text(
        io.BytesIO(requests.get(pdf_url).content), laparams=LAParams()
    )

    # Remove single newline characters
    extracted_text = extracted_text.replace("\n", " ")

    # Find the start and end of the Abstract and Introduction sections
    start_abstract = extracted_text.find("Abstract")
    start_introduction = extracted_text.find("Introduction")
    end_abstract = start_introduction if start_introduction != -1 else None

    # Extract Abstract and Introduction sections
    abstract = extracted_text[start_abstract:end_abstract].strip()
    introduction = (
        extracted_text[start_introduction:].strip() if start_introduction != -1 else ""
    )

    # Construct Markdown content
    markdown_text = f"# {abstract}\n\n# {introduction}"

    if len(markdown_text) < 20:
        markdown_text = extracted_text

    markdown_text = markdown_text.replace('\n', ' ').replace('  ', '\n\n')

    # Save the Markdown content to the specified file
    with open(filename, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_text)

    print(f"Markdown content saved to {filename}")

    return markdown_text