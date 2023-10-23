import os
import io
import requests
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

def arxiv_to_md(pdf_url: str, output_folder: str) -> None:
    """
    Extracts the Abstract and Introduction sections from a PDF from an arXiv URL
    and saves them as a Markdown file.

    Args:
        pdf_url (str): The URL of the PDF on arXiv.
        output_folder (str): The folder where the Markdown file will be saved.

    Returns:
        None

    Example:
    ```python
    pdf_url = "https://arxiv.org/pdf/2310.06825"
    output_folder = "output"
    arxiv_to_md(pdf_url, output_folder)
    ```
    """
    # Extract the last part of the PDF URL to use as the filename
    filename = os.path.join(output_folder, pdf_url.split("/")[-1] + ".md")

    # Extract text from the PDF
    extracted_text = extract_text(io.BytesIO(requests.get(pdf_url).content), laparams=LAParams())

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
    with open(filename, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_text)

    print(f"Markdown content saved to {filename}")
