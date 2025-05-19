

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"while", "even though","despite~"

Verb stem + つつ(も)

彼は時々車を運転しつつ、電話をする。
彼は忙しいと言いつつ、長電話をしている。

'''


def match_tsutsu_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "VERB"},
            {"pos": "AUX", "OP": "?"},
            {"pos": "SCONJ", "lemma": "つつ"},
            {"lemma": {"NOT_IN": ["ある"]}},
          ],
    ]

    matcher.add("tsutsu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
