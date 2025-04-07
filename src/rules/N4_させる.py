import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb causative form させる

Ru-verb	る -> させる
U-verb	(ない form) ない -> せる
する	-> させる
やる	-> やらせる
くる	-> こさせる

子どもに勉強をさせる。
食べさせてください。
結婚させる。
母は私に自分の部屋を片付けさせた。
この仕事は部下にやらせます。
君を泣かせるつもりはなかった！
僕にやらせてください
息子はアニメを見たがっていますが、宿題が終わっていないので、見させません。

'''


def match_saseru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos":"VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos":"AUX", "lemma": {"IN": ["せる","させる"]}},
            {"lemma": {"NOT_IN" : ["られる"]}},
        ],
    ]

    matcher.add("saseru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
