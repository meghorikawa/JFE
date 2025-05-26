

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"I didn't know" 
Used to express surprise, or used to ask what something is

彼が犯人だったとは…
才能のある彼女が急に亡くなるとは、とても残念です。
自分だけで日本語を勉強して、あそこまで会話が上手とはすごいなあ。
サンフランシスコは家賃が高いと聞いていたが、こんなに高いとは驚きだ。
彼女がオリンピックで金メダルを取るとは誰も予想しなかった。
あんなに女らしく美しく見える人が、実は男だったとは…
妹の結婚式に出られないとは、残念な限りだ。
JLPTとはJapanese Language Proficiency Test の略で、日本語能力試験のことである。
今まで明かされなかった衝撃の真実とは…

'''
def match_toha_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "ADP", "lemma": "と"},
            {"pos":"ADP", "lemma": "は"},
            {"pos": "SCONJ", "lemma": {"NOT_IN":["いう","言う"]}}
        ],
        ]


    matcher.add("toha", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
