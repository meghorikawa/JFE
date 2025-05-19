import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

"furthermore", "again", 

彼は父親よりさらに背が高い。
いらっしゃい！いらっしゃい！今日はいつもよりさらにお安くなっていますよ！
こちらの料理には、すこし塩を足すと、さらに美味しくなりますよ。
私はそれについてさらに知りたい。
彼は料理を2人分も食べた。さらに、食後にケーキも食べた。

'''


def match_sarani_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": {"IN": ["ADV", "CCONJ"]}, "lemma": "さらに"},
            {},
        ],
    ]

    matcher.add("sarani", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
