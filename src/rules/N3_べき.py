import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (standard form) + べき（だ）
Special verb
する OR す + べき（だ）
な-adjective + である
い-adjective + くある

私はそれについてもっと知るべきだ。
約束は守るべきだ。
早く帰宅すべきだ。
真実を言うべきだ。
おもちゃは、先ず安全であるべきです。
最初に私に電話するべきだった。
何をすべきか、もう彼女の心は決まっていた。


'''


def match_bekida_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb adjective constructions use である which will also be caught.
            {"pos":"VERB"},
            {"lemma": "する", "pos": "AUX", "OP": "?"},  # optional auxiliary to account for する
            {"orth": "べき", "pos": "AUX"},
        ]
    ]

    matcher.add("bekida", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
