

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

to have the intention of doing....

Verb + た + つもりで
Noun+の + つもりで

冗談のつもりで言ったのです。
私は死んだつもりで働いた。
彼はそれをどんなつもりで言ったのだと思いますか。


'''


def match_tsumoride_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "VERB"},
            {"pos": "AUX", "OP": "?"},
            {"pos": "NOUN", "lemma": "つもり"},
            {"pos": "ADP", "lemma":"で"}
          ],[ # noun pattern
            {"pos": {"IN": ["PRON","NOUN"]}},
            {"pos": "ADP", "lemma": "の", "OP": "?"},
            {"pos": "NOUN", "lemma": "つもり"},
            {"pos": "ADP", "lemma": "で"}

        ]
    ]

    matcher.add("tsumoride", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
