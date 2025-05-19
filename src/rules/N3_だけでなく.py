import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

"not only.... but also~"

ここのレストランはどれも安いだけでなく、美味しい。
この公園では、子供だけではなく大人も楽しむことができる。
彼女は日本語が上手なだけでなく、英語もペラペラだ。
君だけでなく僕も悪かった。
彼は知識だけではなく、経験も豊かである。
肉だけでなく野菜も食べなさいよ。

'''


def match_dakedenaku_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {},
            {"pos": "ADP", "lemma": "だけ"},
            {"pos": "AUX", "orth":"で"},
            {"pos": "ADP", "lemma": "は", "OP": "?"},
            {"pos": "AUX", "lemma": "ない"},
        ],
    ]

    matcher.add("dakedenaku", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
