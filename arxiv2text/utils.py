def replace_enter_to_space(x):
    x = x.replace("\n", " ")
    x = " ".join(x.split())
    return x


def find_similar_subjects(
    input_subject: str, subject_list: list, threshold: float = 0.7
) -> list:
    """
    Find subjects in a list that are similar to the given input subject.

    Args:
    input_subject (str): The input subject to find similar subjects for.
    subject_list (list): List of subjects to compare against.
    threshold (float): The minimum similarity threshold (default is 0.7).

    Returns:
    list: A list of subjects from subject_list that are similar to the input subject.
    """
    input_subject = input_subject.lower()
    similar_subjects = []
    for subject in subject_list:
        subject = subject.lower()
        common_chars = set(input_subject) & set(subject)
        similarity = len(common_chars) / max(len(input_subject), len(subject))
        if similarity >= threshold:
            similar_subjects.append(subject)
    return similar_subjects
