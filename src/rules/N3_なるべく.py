import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


ながらも + pattern

なるべく気をつけてください。
なるべく運動すべきです。
ミーティングは、なるべく早い時間に初めてもらいたいです。
寝る前にはなるべくストレッチをしてから、寝るようにしましょう。
うちのアパートは壁が薄いから、夜はなるべく大きい音を出さないようにしています。

'''


def match_nagaramo_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADV", "lemma": "なるべく"},
          ]
    ]

    matcher.add("nagaramo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
