

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"but", "although", "even though"


VERB/NOUN/Adjective + ものの

秋であるものの、まだ暑い。
申し込みはしたものの、試験を受けるかどうか未定です。
車の免許は持っているものの、ほとんど運転したことがありません。
買ったものの、使い方が分からない。
金欠ではあるものの、毎日美味しい食事を楽しんでいる。
私のアパートは駅からはちょっと遠いものの、静かできれいな住宅街にある。
友人に勧められてスポーツジムの会員になったものの、ほとんど利用していない。

'''
def match_monono_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "SCONJ", "lemma":"もの"},
            {"pos": "SCONJ", "lemma": "の"},
        ],
        ]


    matcher.add("monono", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
