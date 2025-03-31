import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual) + んだ/のだ + けど
Noun + だ/だった/です + けど
Noun + なんだ/なのだ 
な-adjective + だ/だった + けど
な-adjective + なんだ/なのだ + けど
い-adjective + い/いかった
い-adjective + いんだ/いのだ

スキー行きたいんだけど、お金が全然ないよ。
昨日からダイエットを始めたのだけど、もう甘いものが食べたくなってしまった。
彼女はかわいいんだけど僕のタイプではない。
若かったけど、とても賢かった。
今週は暇だけど、来週は忙しい。
彼に電話したんだけど、話し中で通じなかった。
そうだといいんだけど。
今、勉強してるんだけど…
'''


def match_dakedo_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for Noun + だ/だった/です ＋　けど
            {"pos": {"IN": ["NOUN", "ADJ", "PRON"]}},
            {"pos": "AUX", "lemma": "だ"},
            {"orth": "けど", "pos": "SCONJ"}
        ], [  # pattern for Verb (casual) + んだ/のだ　+ けど
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"}, # optional argument for する
            {"pos": "AUX", "lemma": {"IN": ["たい","てる"]}, "OP": "?"}, #optional argument for たい and てる form
            {"pos": "AUX", "orth": {"IN": ["た", "だ"]}, "OP": "?"},  # past tense た だ variation
            {"orth": {"IN": ["ん","の"]}, "pos": "SCONJ"},
            {"pos": "AUX", "lemma": "だ"},
            {"orth": "けど", "pos": "SCONJ"}
        ], [  # pattern for な-adjective + だ/だった, な-adjective + なんだ/なのだ, い-adjective + い/いかった
            {"pos": "ADJ"},
            {"pos": "AUX", "lemma": {"IN": ["だ","た"]}, "OP": "?"},
            {"orth": {"IN": ["ん", "の"]}, "pos": "SCONJ", "OP": "?"},
            {"orth": "だ", "pos": "AUX", "OP": "?"},
            {"orth": "けど", "pos": "SCONJ"}
        ], [  # pattern for , い-adjective + いんだ/いのだ
            {"pos": "ADJ"},
            {"orth": {"IN": ["ん", "の"]}, "pos": "SCONJ", "OP": "?"},
            {"orth": "だ", "pos": "AUX", "OP": "?"},
            {"orth": "けど", "pos": "SCONJ"}
        ]
    ]

    matcher.add("dakedo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
