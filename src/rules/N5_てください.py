import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

polite request
"pelase do"

Verb (て form)	+ ください


ちょっと待ってください。
もっとゆっくり言ってください
静かにしてください。

'''


def match_tekudasai_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "SCONJ", "orth": {"IN":["て", "で"]}},
            {"pos": "AUX", "lemma": {"IN": ["くださる","下さる"]}},
        ]
    ]

    matcher.add("tekudasai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
