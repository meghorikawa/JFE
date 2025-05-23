

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"to be possible"

NOUNの/Verb + 可能性がある

これをいっぱい食べたら、病気の可能性があるよ。
その犬は暴れる可能性がある。
それは今後増える可能性があります。
このニュースレターを受け取った可能性があるのは誰ですか。
私はあなたにもその可能性があると思います。
あの行動が無駄になる可能性がある。
の会社は売り上げが減っているから、倒産の可能性がある。
それはこのままだと壊れる可能性がある。

'''
def match_kanousei_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": "NOUN", "lemma": "可能性"},
            {"pos":"ADP", "lemma": "が"},
            {"lemma": "ある"}
        ],
        ]


    matcher.add("kanousei", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
