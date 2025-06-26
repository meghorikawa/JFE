import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4



Verb (た form)	+ らどう

一緒に来たらどうですか？
静かにしたらどうですか。
先生に聞いてみたらどうですか？
彼に電話したらどうですか。

'''


def match_tara_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "AUX", "orth": "たら"},
            {"lemma": {"NOT_IN": ["どう"]}},
        ]
    ]

    matcher.add("tara", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
