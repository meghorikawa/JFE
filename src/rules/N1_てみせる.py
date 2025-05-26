

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"I'll definitely", "To show"
This is used to show strong confidence, or that the speaker will demonstrate an action


VERB て みせる



今度の試験には、絶対合格してみせるよ。
将来必ず有名なピアニストになってみせる。
僕は小説を書いて賞をを取ってみせる。
今年の旧正月前に絶対、新しい仕事ゲットしてみせる。
彼は、一か月以内に結婚相手を見つけてみせると宣言した。
やり方がわからないので、一度やってみせてくれませんか。
失敗しないように、私がやってみせますね。
すみませんが、使い方が分からないので、一度やってみせてください。

'''
def match_temiseru_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["AUX", "VERB"]}},
            {"pos":"SCONJ","lemma": "て"},
            {"pos": "VERB", "lemma": {"IN":["みせる","見せる"]}}
        ],
        ]


    matcher.add("temiseru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
