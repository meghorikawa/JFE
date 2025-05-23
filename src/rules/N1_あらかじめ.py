

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1
"beforehand", "in advance", "previously"

あらかじめ + verb

あらかじめ教科書を読んでください。
私たちはあらかじめスナックを用意しておきました。
僕は逃げ道をあらかじめ探しました。
私はその資料をあらかじめ印刷して持参します。
私たちはそれをあらかじめ考慮しておく必要がある。
訪ねていらっしゃる前にあらかじめ連絡してください。
会社の忘年会のためにあらかじめレストランを予約しました。


'''
def match_arakajime_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADV", "lemma": "あらかじめ"},
        ],
        ]


    matcher.add("arakajime", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
