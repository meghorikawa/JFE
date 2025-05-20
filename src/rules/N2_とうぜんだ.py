

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"natural" , "as a matter of course" 

VERB て form + 当然(当たり前)だ
なadjective + で　＋　当然(当たり前)だ
いadjective - い + くて+ 当然(当たり前)だ

毎日遅くまで残業しているから、疲れて当然だ。
人間だから間違いがあって当然です。そんなに落ち込まないでください。
マンションの近くに電車が走っているから、うるさくて当たり前だ。
今回のテストはとても簡単なので満点が取れて当然です。
女性だから料理ができて当たり前だと思わないでください。
彼女はいつも人の悪口ばかり言っているので、みんなに嫌われて当然だ。
マンションの近くに電車が走っているから、うるさくて当たり前だ。

'''


def match_tetouzenda_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "VERB"},
            {"pos": "AUX", "OP": "?"},
            {"pos": "SCONJ", "lemma":"て"},
            {"pos": "ADJ", "lemma": {"IN":["当然", "とうぜん", "当たり前"]}},
            {"pos": "AUX", "lemma": {"IN": ["だ","です"]}},
        ],[ #adj pattern
            {"pos": "ADJ"},
            {"orth": {"IN": ["て","で"]}},
            {"pos": "ADJ", "lemma": {"IN":["当然", "とうぜん", "当たり前"]}},
            {"pos": "AUX", "lemma": {"IN": ["だ","です"]}},


            ]
        ]


    matcher.add("tetouzenda", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
