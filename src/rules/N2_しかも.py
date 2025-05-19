import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"moreover", "furthermore",  

この教科書の説明はわかりやすくて、しかも詳しい 。
今日はとても暑い。しかも、湿度も高いので何もしたくないだ。
彼は仕事がとても早い。しかも、正確で丁寧だから安心して任せられる。


'''


def match_shikamo_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": {"IN": ["ADV", "CCONJ"]}, "lemma": "しかも"},
            {},
        ],
    ]

    matcher.add("shikamo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
