import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


Verb (stem form)　+	っぱなし

このドアはいつも開けっぱなしだ。
水を出しっぱなしにしないでください。
窓を開けっぱなしで出てきた。

'''


def match_ppanashi_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [
            {"pos": "VERB"},
            {"pos":"PART", "orth":"っぱなし"}
        ]
    ]

    matcher.add("ppanashi", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
