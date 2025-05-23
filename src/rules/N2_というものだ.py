

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"something like"; "something called~"

used to: 
    generalize or simplify an explanation of something.
    to introduce oneself / something.

VERB/NOUN +だ/なAdjective+だ/いadjective _ というもの　だ・です / というものが　ある・あります


これがいわゆる「天ぷら」というものです。
辛い時に助けてくれるのが、親友というものだ。
それがまさに愛というものだ。
人はみんな平等ではない。それが人生というものだ。
私は山田ケンというものです。
それは無理押しというものだ。
誰にでも好みというものはあります。
人間には理性というものがある。


'''
def match_toiumonoda_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "ADP", "lemma": "と"},
            {"pos":"VERB", "lemma": {"IN":["いう", "言う"]}},
            {"pos": "NOUN", "lemma": "もの"},
            {"pos": "AUX", "lemma": {"IN": ["だ","です"]}}
        ],[  # pattern with がある
            {},
            {"pos": "ADP", "lemma": "と"},
            {"pos":"VERB", "lemma": {"IN":["いう", "言う"]}},
            {"pos": "NOUN", "lemma": "もの"},
            {"pos": "ADP", "lemma": {"IN": ["が","は"]}},
            {"pos": "VERB", "lemma": "ある"}
        ]
        ]


    matcher.add("toiumonoda", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
