import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

approximately; about; around

____ + くらい・ぐらい

今は100人くらいが部屋にいる。
彼女が私と同じくらい背が高いんだ。
カレーが大好き。毎日食べたいくらいだ。


'''


def match_kurai_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": {"IN": ["ADP","PART"]}, "lemma": {"IN":["ぐらい","くらい"]}},
          ],
    ]

    matcher.add("kurai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
