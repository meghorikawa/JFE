import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb (て form) +     くれる
                    くれます
                    くれない
                    くれた
                    くれました

手伝ってくれる？
彼ならやってくれる。
すみません、写真を取ってくれませんか？
部長は私に寿司をおごってくれました。

'''


def match_tekureru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# general patern
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": "くれる"},

        ]
    ]

    matcher.add("tekureru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
