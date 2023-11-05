import xml.etree.ElementTree as ET
import urllib.request
from arxiv2text.utils import replace_enter_to_space, find_most_similar_subject
from arxiv2text.constant import SUBJECTS


def fetch_arxiv_papers(
    subject: str, start_page: int, page_step: int = 200, print_bool: bool = False
) -> dict:
    """
    Fetch a list of arXiv papers based on a subject and optional criteria.

    Args:
        subject (str): The subject or topic of the papers to search for. It will be
            converted to lowercase for case-insensitive matching.
        start_page (int): The starting page for retrieving search results.
        page_step (int): The maximum number of papers to retrieve (default is 200).
        print_bool (bool): Whether to print the retrieved paper information (default is False).

    Returns:
        dict: A list of dictionaries, each containing information about the retrieved papers.
            The dictionary has the following structure for each paper:

            {
                'Title': str,        # Title of the paper (or empty string if not available)
                'Abstract': str,     # Abstract or summary of the paper (or empty string if not available)
                'URL': str,          # URL link to the paper (or empty string if not available)
                'Published': str,    # Date the paper was published (or empty string if not available)
                'DOI': str           # Digital Object Identifier of the paper (or empty string if not available)
            }
    """
    subject = subject.lower()
    if subject not in SUBJECTS:
        possible_subjects = find_most_similar_subject(subject, SUBJECTS)
        if possible_subjects:
            print(f"Possible subjects: {possible_subjects}")
        else:
            print("No matching subjects found.")
            return {}

    search_query = f'all:{subject.replace(" ", "+")}'

    url = f'http://export.arxiv.org/api/query?search_query={search_query}&start={start_page}&max_results={page_step}'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    namespace = {'atom': 'http://www.w3.org/2005/Atom', 'opensearch': 'http://a9.com/-/spec/opensearch/1.1', 'arxiv': 'http://arxiv.org/schemas/atom'}
    root = ET.fromstring(data)
    entry_dict = []
    
    for entry in root.findall('.//atom:entry', namespaces=namespace):
        entry_info = {}

        title_element = entry.find('./atom:title', namespaces=namespace)
        entry_info['Title'] = replace_enter_to_space(title_element.text) if title_element is not None else ''

        abstract_element = entry.find('./atom:summary', namespaces=namespace)
        entry_info['Abstract'] = replace_enter_to_space(abstract_element.text.strip()) if abstract_element is not None else ''

        url_element = entry.find('./atom:id', namespaces=namespace)
        entry_info['URL'] = url_element.text if url_element is not None else ''

        published_element = entry.find('./atom:published', namespaces=namespace)
        entry_info['Published'] = published_element.text if published_element is not None else ''

        doi_element = entry.find('./arxiv:doi', namespaces=namespace)
        entry_info['DOI'] = doi_element.text if doi_element is not None else ''

        entry_dict.append(entry_info)

    if print_bool:
        for i, entry in enumerate(entry_dict):
            print(f"Paper {i + 1}")
            if entry['Title']:
                print("Title:", entry['Title'])
            if entry['Abstract']:
                print("Abstract:", entry['Abstract'])
            if entry['URL']:
                print("URL:", entry['URL'])
            if entry['Published']:
                print("Published:", entry['Published'])
            if entry['DOI']:
                print("DOI:", entry['DOI'])
            print("\n")

    return entry_dict
