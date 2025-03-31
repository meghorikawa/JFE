import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Noun + 的

もっと具体的なアイディアを出してください。

'''


def match_tabini_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb
            {"lemma": {"REGEX": ".*的.*"}, "pos":{"IN":["ADJ","ADV"]}}
        ]
    ]

    matcher.add("teki", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
