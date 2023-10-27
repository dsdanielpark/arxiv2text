import xml.etree.ElementTree as ET
import urllib.request
from arxiv2text.utils import replace_enter_to_space


def fetch_arxiv_papers(subject: str, max_results: int, print_bool: bool = False) -> dict:
    """
    Fetch paper information from arXiv using the provided subject and maximum number of results.

    Args:
        subject (str): The subject to search on arXiv.
        max_results (int): The maximum number of paper results to retrieve.
        print_bool (bool, optional): Whether to print the results. Default is False.

    Returns:
        dict: A dictionary containing the fetched paper information.

    Example:
        >>> subject = "Computer Science"
        >>> papers = fetch_arxiv_papers(subject, max_results=2, print_bool=True)
    """
    search_query = f'all:{subject.replace(" ", "+")}'
    url = f'http://export.arxiv.org/api/query?search_query={search_query}&start=0&max_results={max_results}'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    namespace = {'atom': 'http://www.w3.org/2005/Atom', 'opensearch': 'http://a9.com/-/spec/opensearch/1.1'}
    root = ET.fromstring(data)
    entry_dict = {}
    for i, entry in enumerate(root.findall('.//atom:entry', namespaces=namespace)[:max_results]):
        entry_info = {}
        entry_info['Title'] = replace_enter_to_space(entry.find('./atom:title', namespaces=namespace).text)
        entry_info['Link'] = replace_enter_to_space(entry.find('./atom:id', namespaces=namespace).text)
        summary = entry.find('./atom:summary', namespaces=namespace).text.strip()
        summary = replace_enter_to_space(summary)
        entry_info['Summary'] = summary
        entry_dict[i] = entry_info

    if print_bool:
        for i, entry in entry_dict.items():
            print(f"Paper {i + 1}:")
            print("Title:", entry['Title'])
            print("Link:", entry['Link'])
            print("Summary:", entry['Summary'])
            print("\n")

    return entry_dict