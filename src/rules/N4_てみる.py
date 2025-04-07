import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

Verb (て form)	+   みる
                    みます
                    みたい

やってみる！
これを使ってみる。
やってみないと分からない。
いつか海外に行ってみたいな。
おいしいかどうかわからないので、試しに食べてみます。
とにかく、彼女の予定を聞いてみます。

'''


def match_teshimau_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# general patern - Verb + で + みる
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": {"IN": ["みる", "見る"]}},
        ],
    ]

    matcher.add("teshimau", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
