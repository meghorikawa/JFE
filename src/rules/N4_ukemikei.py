import spacy
from spacy.matcher import Matcher
from collections import Counter

# 安っぽい is tokenized as one word and won't be caught by this rule.....

'''
Level: N4

Passive form in Japanese

ケーキが誰かに食べられた！
みんなに変だと言われます。
この本は多くの人に読まれている。
私は先生にほめられました。
'''


def match_ukemi_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [# 一段　-られる
            {"pos":"VERB"},
            {"pos": "AUX", "lemma": "られる"}
        ],[ # 五段　ーれる
            {"pos": "VERB"},
            {"pos": "AUX","lemma": "れる"},
        ]
    ]

    matcher.add("ukemi", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
