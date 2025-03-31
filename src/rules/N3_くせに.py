import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (dictionary form) + くせに
Noun + の + くせに
な-adjective + な + くせに
い-adjective + くせに

背が高いくせに早く走れない。
元気なくせに、病気のふりをしている。
医者でもないくせに。
彼女はお金持ちのくせにケチだ
'''


def match_kuseni_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verbs
            {"tag": {"NOT_IN": ["助動詞"]},"pos": {"IN": ["VERB", "AUX"]}}, # need aux but make sure な particle is
            # excluded
            {"orth": "くせ", "pos": "NOUN"},
            {"orth": "に", "pos": "ADP"},
        ], [  # pattern for nouns
            {"pos": "NOUN"},
            {"orth": "の", "pos": "ADP"},
            {"orth": "くせ", "pos": "NOUN"},
            {"orth": "に", "pos": "ADP"},
        ], [  # pattern for nouns
            {"pos": "ADJ"},
            {"orth": "な", "pos": "AUX", "OP": "?"},
            {"orth": "くせ", "pos": "NOUN"},
            {"orth": "に", "pos": "ADP"},
        ],
    ]

    matcher.add("kuseni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
