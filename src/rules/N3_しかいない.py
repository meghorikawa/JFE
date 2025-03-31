import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

VERB + しかない (しかありません)

やるしかない。
歩くしかない。
勉強するしかなかった。
もう両親に頼むしかありません。
'''


def match_shikanai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for plain form
            {"pos": "VERB"},
            {"pos": "PART", "orth": "しか"},
            {"lemma": "ない", "pos": "AUX"},
            {"orth": "た", "pos": "AUX", "OP": "?"}  # optional argument for た to caputure past tense casual form
        ], [  # Pattern for polite form
            {"pos": "VERB"},
            {"pos": "PART", "orth": "しか"},
            {"lemma": "ある", "pos": "VERB"},
            {"lemma": "ます", "pos": "AUX"},
            {"lemma": "ぬ", "pos": "AUX"},
        ]
    ]

    matcher.add("shikanai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
