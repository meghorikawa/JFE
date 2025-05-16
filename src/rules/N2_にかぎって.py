import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2


うちの娘に限って、人をいじめるようなことはしません。
私は学校に休んだ日に限って、テストがある。
仕事が忙しい日に限って、なぜかシステムトラブルが発生する。
ここから富士山が見えるそうだけど、今日に限って雲が多いね。
彼は、いつも家にいるのに、今日に限って留守でした。

'''


def match_nikagitte_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # pattern with noun
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "に"},  # add optional argument for て form
            {"pos": "VERB", "lemma": {"IN": ["かぎる", "限る"]}},
            {"pos": "SCONJ", "lemma": "て"}
          ],
    ]

    matcher.add("nikagitte", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
