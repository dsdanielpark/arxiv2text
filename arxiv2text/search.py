import xml.etree.ElementTree as ET
import urllib.request
from arxiv2text.utils import replace_enter_to_space, find_similar_subjects
from arxiv2text.constant import SUBJECTS


def fetch_arxiv_papers(subject: str, max_results: int, print_bool: bool = False) -> dict:
    """
    Fetch a list of arXiv papers based on a subject and optional criteria.

    Args:
    subject (str): The subject or topic of the papers to search for.
    max_results (int): The maximum number of papers to retrieve (default is 2).
    print_bool (bool): Whether to print the retrieved paper information (default is False).

    Returns:
    dict: A dictionary containing information about the retrieved papers.
        The dictionary has the following structure for each paper:
        {
            'Title': str,        # Title of the paper
            'Abstract': str,     # Abstract or summary of the paper
            'URL': str,          # URL link to the paper
            'Published': str,    # Date the paper was published
            'DOI': str           # Digital Object Identifier of the paper
        }
    """
    subject = subject.lower()
    if subject not in SUBJECTS:
        possible_subjects = find_similar_subjects(subject, SUBJECTS)
        if possible_subjects:
            print(f"Possible subjects: {', '.join(possible_subjects)}")
        else:
            print("No matching subjects found.")
        return {}

    search_query = f'all:{subject.replace(" ", "+")}'

    url = f'http://export.arxiv.org/api/query?search_query={search_query}&start=0&max_results={max_results}'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    namespace = {'atom': 'http://www.w3.org/2005/Atom', 'opensearch': 'http://a9.com/-/spec/opensearch/1.1', 'arxiv': 'http://arxiv.org/schemas/atom'}
    root = ET.fromstring(data)
    entry_dict = {}

    for i, entry in enumerate(root.findall('.//atom:entry', namespaces=namespace)[:max_results]):
        entry_info = {}
        entry_info['Title'] = replace_enter_to_space(entry.find('./atom:title', namespaces=namespace).text)
        abstract = entry.find('./atom:summary', namespaces=namespace).text.strip()
        abstract = replace_enter_to_space(abstract)
        entry_info['Abstract'] = abstract
        entry_info['URL'] = replace_enter_to_space(entry.find('./atom:id', namespaces=namespace).text)
        published = entry.find('./atom:published', namespaces=namespace).text
        entry_info['Published'] = published
        doi = entry.find('./arxiv:doi', namespaces=namespace).text
        entry_info['DOI'] = doi
        entry_dict[i] = entry_info

    if print_bool:
        for i, entry in entry_dict.items():
            print(f"Paper {i + 1}")
            print("Title:", entry['Title'])
            print("Abstract:", entry['Abstract'])
            print("URL:", entry['URL'])
            print("Published:", entry['Published'])
            print("DOI:", entry['DOI'])
            print("\n")

    return entry_dict