import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb ます (stem form)	切れない

この部屋に100人は入り切れない。
彼は使い切れないほど金がある。
このお酒は強すぎて、飲み切れなかった。
いっぱい注文しないで、二人で食べ切れないから。

'''


def match_kirenai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for Verb (stem) + きれない
            {"pos": "VERB", "tag": "動詞-一般"},
            {"lemma": {"IN": ["切る", "きる", "切れる", "きれる"]}, "tag": "動詞-非自立可能"},
            {"lemma":"ない","pos" : "AUX"} # using the lemma captures cases when the past tense is used
        ],
        [  # Pattern for exceptions of 言い切るand 売り切る。
            {"lemma": {"IN": ["言い切れる", "売り切れる"]}, "tag": "動詞-一般"}
        ]
    ]

    matcher.add("kirenai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
