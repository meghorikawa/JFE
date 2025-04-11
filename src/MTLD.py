# modified MTLD implementation from this github repository https://github.com/jennafrens/lexical_diversity/tree/master
import string
import spacy

# The MTLD calculation method
# MTLD = Total number of words / number of factors

ttr_threshold = 0.72

def mtld_calc(tokenized_text, ttr_threshold):
    '''

    :param tokenized_text: the tokenized text
    :param ttr_threshold:
    :return:
    '''
    current_ttr = 1.0
    token_count = 0
    type_count = 0
    types = set()
    factors = 0.0

    clean_text = remove_punctuation(tokenized_text)
    for token in clean_text:
        token_count += 1
        if token not in types:
            types.add(token)
            type_count += 1
        current_ttr = type_count / token_count
        if current_ttr <= ttr_threshold:
            factors += 1
            token_count = 0
            type_count = 0
            types = set()
            current_ttr = 1.0

    # handle partial factor
    excess = 1.0 - current_ttr
    excess_val = 1.0 - ttr_threshold
    factors += excess / excess_val
    if factors != 0:
        return len(tokenized_text) / factors
    return -1

def mtld (tokenized_text,ttr_threshold):
    if isinstance(tokenized_text, str):
        raise ValueError("Input should be tokenized text")
    if len(tokenized_text)< 50:
        raise ValueError("Input should be at least 50 tokens")
    return mtld_calc(tokenized_text, ttr_threshold)

def remove_punctuation(text):
    """
    uses spacy pos tags to remove punctuation from tokenized text.

    Parameters:
        text - the tokenized text (via spacy)

    Returns:
        List[str]: A list with punctuation removed.
    """
    return [token for token in text if token.pos_ != "PUNCT"]
