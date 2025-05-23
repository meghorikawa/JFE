

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"once", "formerly"

かつて　+ sentence

彼女はフランスにかつて住んでいた。
ロンドンはかつて霧で有名だった。
京都はかつて日本の首都でした。
かつて彼はそこで父に会った。
彼はかつて事故を起こしそうになった。
私はかつてある手術をうけたことがあった。
かつて私たちの学校に前に大きな建物があった。

'''
def match_katsute_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": "ADV", "lemma": "かつて"},
        ],
        ]


    matcher.add("katsute", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
