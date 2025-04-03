

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


ながらも + pattern

に比べると (ni kureberu to).
に比べれば (ni kurabereba).
に比べ (ni kurabe).

きのうにくらべて、きょうはすこしさむいね。
ロンドンはパリに比べると大きい。
以前に比べて、彼の日本語は上手になった。
日本はアメリカや中国に比べれば小さな国です。

'''


def match_nikuraberu_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for くらべる and くらべ form
            {"pos": "ADP", "lemma": "に"},
            {"pos": "VERB", "lemma": {"IN":["くらべる", "比べる"]}}, # allow for both hiragana and kanji

          ]
    ]

    matcher.add("nikuraberu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
