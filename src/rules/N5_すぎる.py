

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

intend to; plan to do ~

Verb　stem + すぎる
            すぎます
            すぎた
            すぎました
            すぎて

このシャツは大きすぎる。
今年の夏は暑すぎた。
この問題は簡単すぎます。

'''


def match_sugiru_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "VERB", "lemma": {"IN": ["すぎる", "過ぎる"]}},
            {},
          ],
    ]

    matcher.add("sugiru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
