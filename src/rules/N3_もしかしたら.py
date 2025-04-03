import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

もしかしたら
もしかすると	+ phrase + (commonly with かもしれない)

もしかしたら、明日行けないかもしれない。
もしかしたら病気かもしれない。
もしかしたら彼は気が変わるかもしれません。
もしかすると彼の話はうそかもしれない。
もしかするとあそこに座っている人は有名な人かもしれない。
もしかすると、それは偽物かもしれない。

'''


def match_moshikashitara_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # もしかしたら pattern
            {"pos": "ADV", "lemma": "もし"},
            {"pos": "ADP", "lemma": "か"},
            {"pos": "VERB", "lemma": "する"},
            {"pos": "AUX", "orth": "たら"}
        ], [# もしかすると pattern
            {"pos": "ADV", "lemma": "もし"},
            {"pos": "ADP", "lemma": "か"},
            {"pos": "VERB", "lemma": "する"},
            {"pos": "SCONJ", "orth": "と"}

        ]
    ]

    matcher.add("moshikashitara", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
