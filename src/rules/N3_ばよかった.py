import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


Verb (ば conditional form)	よかった（のに）

そうすればよかった。
傘を持ってくればよかった。
遅刻してしまった。もっと早く家を出ればよかった。

'''


def match_bayokatta_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb
            {"pos": "VERB"},
            {"pos": "SCONJ", "orth": "ば"},
            {"lemma": "よい", "pos": "ADJ"},
            {"orth": "た", "pos": "AUX"},
            {"orth": "の", "pos": "SCONJ", "OP": "?"},
            {"orth": "に", "pos": "ADP", "OP": "?"},
        ]
    ]

    matcher.add("bayokatta", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
