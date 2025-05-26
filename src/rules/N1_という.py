

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"all", "every single" 
NOUN + という + SAME NOUN

津波によって家という家が全て流されてしまった。
大雪で東京に行くの電車という電車が中止されている。
家に変な匂いがこもったので、窓という窓を全部開けた。
息子の部屋は壁という壁に車のポスターが貼ってある。
チラシをこの地域の家という家に配って歩いた。
今日という今日は、この仕事をやり遂げなければならない。
彼女は学校の規則をよそに爪という爪すべてを真っ赤に塗っていた。

'''

def match_toiu_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["NOUN", "PRON"]}},
            {"pos": "ADP", "lemma": "と"},
            {"pos": "VERB", "lemma": {"IN":["いう","言う"]}},
            {"pos": {"IN": ["NOUN","PRON"]}}
        ],
        ]


    matcher.add("N1_toiu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        span = doc[start:end]
        #add something to make sure that the first Noun is the same as the second
        first_token = span[0]
        last_token = span[-1]
        if first_token.lemma_ == last_token.lemma_:
            match_counts[span.text] += 1

    return dict(match_counts)
