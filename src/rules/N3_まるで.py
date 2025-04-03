

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


まるで	Verb (casual form) + よう
Noun + のよう


合格した！まるで夢のようだ。
すごい！まるで魔法のようだ！
あの女の人は、美しくて、優しくて、まるで天使のようだ。
彼の日本語はまるで日本人が話しているように聞こえる。
'''


def match_marude_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADV", "lemma": "まるで"},

          ]
    ]

    matcher.add("marude", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
