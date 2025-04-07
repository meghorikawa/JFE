import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb (て form)	+   くる
                    きた
                    きます
                    きました

見えてくる。
雨が降ってきた。
雨が降ってきた。
お腹がすいてきた。
ここまで歩いてきました。

'''


def match_tekuru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# pattern for てくる (and きた)
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": {"IN": ["くる", "来る"]}},

        ]
    ]

    matcher.add("tekuru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
