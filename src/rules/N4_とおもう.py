import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

Verb +                   と思う
Noun + だ                と思います
な-adjective + だ        と思わない
い-adjective             と思いません


きれいだと思わない？
それはかなりむずかしいと思います。
今日は午後から雨が降ると思います。
この問題、テストに出ると思いますか。
日本に留学しようと思っています。
仕事を続けるのはむりだと思う。
アメリカでは、何が一番人気のあるスポーツだと思う？
今度の休みに海へ行こうと思っています。

'''
omou_forms = ["思う", "おもう", "おもい", "思い","おもわ", "思わ" ]

def match_toomou_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# general patern - Item と　おもう
            {"pos": "ADP", "lemma": "と"},
            {"pos": "VERB", "orth": {"IN": omou_forms}},
            {} # capture the next token for insight on the endings learners use?
        ],
    ]

    matcher.add("toomou", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
