import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (dictionary form)	ことはない

謝ることはないよ。
明日のテストは簡単だから、心配することはないよ。
'''


def match_kotohanai_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb adjective constructions use である which will also be caught.
            {"pos":"VERB"},
            {"lemma": "する", "pos": "AUX", "OP": "?"},  # optional auxiliary to account for する
            {"orth": {"IN" :["こと","事"]}, "pos": "NOUN"},
            {"orth": "は", "pos": "ADP", "OP": "?"},
            {"lemma": "ない", "pos": "AUX"}, # use lemma to capture instances of polite form used also
        ],[ # pattern for oplie construction
            {"pos": "VERB"},
            {"lemma": "する", "pos": "AUX", "OP": "?"},  # optional auxiliary to account for する
            {"orth": {"IN": ["こと", "事"]}, "pos": "NOUN"},
            {"orth": "は", "pos": "ADP", "OP": "?"},
            {"lemma": "ある", "pos": "VERB"},  # use lemma to capture instances of polite form used also
            {"orth": "ませ", "pos": "AUX"},
            {"orth": "ん", "pos": "AUX"}
             ]
    ]

    matcher.add("kotohanai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
