

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"so", "therefore", "the reason for something"

alternative forms: 
ものだから
ものですから
もんだから (spoken)


VERB/NOUN +だ/なAdjective+だ/いadjective _ もの　だから

目覚まし時計が壊れたものだから、遅刻してしまった。
すみません、風邪を引いてしまったものですから、今日は欠席です。
上着を着たままですみません。寒いものだから。
すみません。お酒は苦手なものですから。
一人っ子なものだからわがままに育ててしまいました。
遅くなってごめんなさい。道路が混んでいたものだから。
上着を脱いでもいいですか？熱いものですから。

'''
def match_monodakara_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "NOUN", "lemma": {"IN":["もの","もん"]}},
            {"pos": "AUX", "lemma": {"IN": ["だ","です"]}},
            {"pos": "SCONJ", "lemma": "から"},
        ],
        ]


    matcher.add("monodakara", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
