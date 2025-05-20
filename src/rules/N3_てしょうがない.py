

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

"can't help but", "very", "extremely

VERB て form + しょうがない　（しかたない）
なadjective - な + で　しょうがない　（しかたない）
い adjective -い +くて　+　しょうがない　（しかたない）

私はそれが気になってしょうがない。
今日は寒くてしょうがない。
今日は何もすることがなくて、暇で仕方がない。
お金をくれて、嬉しくてしょうがない。
バスで行くのは、時間がかかってしょうがない。
海外で一人暮らしを始めたばかりなので、寂しくてしかたがありません。
最近はやることがないので、毎日が暇でしかたがない。

'''


def match_deshouganai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "VERB"},
            {"orth": {"IN":["て","で"]}},
            {"pos": "NOUN", "lemma": {"IN": ["しょう","しかた","しか"]}},
            {"pos": "ADP", "lemma": "が"},
            {"lemma": {"IN": ["ない","ある"]}} # add masu form
        ],[ #adj pattern
            {"pos": "ADJ"},
            {"orth": {"IN": ["て","で"]}},
            {"pos": "NOUN", "lemma": {"IN": ["しかた", "仕方", "しょう"]}},
            {"pos": "ADP", "lemma": "が"},
            {"lemma": {"IN": ["ない","ある"]}}


            ]
        ]


    matcher.add("deshouganai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
