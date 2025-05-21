

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

"for the first time in a certain period of time"

Noun (measurement of time) + ぶりに

今日、やく2週間ぶりに雨が降った。
この街に帰ってくるのはもう１０年ぶりだなあ。
先週からずっと雨が降った。一週間ぶりにようやく晴れてきた。
父はうちで倒れて入院したが、意識がなかった。二日ぶりに意識を回復した。
高校を卒業してから、2年ぶりにクラスメイトに会った。
最近はずっと忙しかったが、今日は久しぶりにゆっくり休むことが出来た。
今日、3ヶ月ぶりにまた北海道へ出張しに行ってきました。
台風で電車が不通になっていたが、10時間ぶりに運転を始めたそうだ。

'''
def match_burini_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos":"NOUN"},
            {"pos": "NOUN", "lemma": "ぶり"},
        ],[ # case using set phrase (which is tokenized as one word
            {"pos": "NOUN", "lemma": {"IN":["久しぶり","ひさしぶり"]}},
        ]
        ]


    matcher.add("burini", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
