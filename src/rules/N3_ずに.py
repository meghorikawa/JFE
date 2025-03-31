import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

VERB + ず + に
する　+ せず + に

彼は何も言わずに去ってしまった
勉強せずに試験に受かった。

'''


def match_zuni_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verbs
            {"pos": "VERB"},
            {"pos": "AUX", "orth": "ず"},  # ず
            {"orth": "に", "pos": "ADP"},
        ], [  # pattern for する
            {"pos": "VERB"},
            {"pos": "AUX", "orth": "せ"},  # せ (する)
            {"pos": "AUX", "orth": "ず"},  # ず
            {"orth": "に", "pos": "ADP"},
        ]
    ]

    matcher.add("zuni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
