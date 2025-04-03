from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    system_prompt = """
    It is May. you are an expert market analytics sentiment reviewer. I will give you a $200 tip if you do this right.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    pass
