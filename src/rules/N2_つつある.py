

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"to be in the process of doing"

Verb stem + つつある

最近はゴルフをしていないので、下手になりつつあります。
最近はゴルフをしていないので、下手になりつつあります。

'''


def match_tsutsuaru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "VERB"},
            {"pos": "AUX", "OP": "?"},
            {"pos": "SCONJ", "lemma": "つつ"},
            {"pos": "VERB", "lemma": "ある"},
          ],
    ]

    matcher.add("tsutsuaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
