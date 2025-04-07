import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

Verb (て form) +    もらう
                    もらいます
                    もらいたい
                    もらわない
                    もらいません
彼に来てもらう。
あなたにぜひ見てもらいたいものがある。
彼は病院でみてもらう必要がある。
母に車で送ってもらった。
あなたに日本語を教えてもらいたい。

'''


def match_temorau_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# general patern
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": {"IN": ["もらう", "貰う"]}},
        ]
    ]

    matcher.add("temorau", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
