from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def replace_enter_to_space(x):
    x = x.replace("\n", " ")
    x = " ".join(x.split())
    return x

def find_most_similar_subject(
    input_subject: str, subject_list: list, threshold: float = 0.7
) -> str:
    """
    Find the most similar subject to the given input subject.

    Args:
    input_subject (str): The input subject to find the most similar subject for.
    subject_list (list): List of subjects to compare against.
    threshold (float): The minimum similarity threshold (default is 0.7).

    Returns:
    str: The most similar subject from subject_list to the input subject.
    """
    vectorizer = TfidfVectorizer()
    subject_vectors = vectorizer.fit_transform([input_subject] + subject_list)
    
    input_vector = subject_vectors[0]
    subject_vectors = subject_vectors[1:]
    
    similarities = cosine_similarity(input_vector, subject_vectors)[0]
    
    max_similarity = max(similarities)
    
    if max_similarity >= threshold:
        most_similar_index = similarities.argmax()
        most_similar_subject = subject_list[most_similar_index]
        return most_similar_subject
    else:
        return "No matching subjects found."
