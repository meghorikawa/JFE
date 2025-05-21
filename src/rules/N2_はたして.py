

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"surely", "as was expected"

果たして  + Phrase

果たしてそうだろうか。
果たして本当に足音が聞こえたのかどうかはわからない。
そのうわさは果たして本当だろうか。
私があの店にいるとき、彼らがそこにやってきたのは果たして偶然だろうか？
この程度の金額で、果たして彼が承知するだろうか。
皆さんにも果たしていただく役割があります。
機械には特に悪いところがないと、果たして何が故障の原因だったのだろうか。

'''
def match_hatashite_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos":"ADV", "lemma": {"IN":["果たして", "はたして"]}},
        ],
        ]


    matcher.add("hatashite", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
