import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

Verb (て form)	+ すみません

遅れてすみません。
心配をかけてすみません。
電話に出れなくてすみません。

'''


def match_teshimau_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# general patern - Verb + で + みる
            {"pos": {"IN": ["VERB", "AUX"]}},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": "すむ"},
            {"pos": "AUX", "lemma": "ます"},
            {"pos": "AUX", "lemma": "ぬ"}
        ],
    ]

    matcher.add("teshimau", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
