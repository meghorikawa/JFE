import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


する changes to	なさる
します changes to	なさいます
して changes to 	なさって

それからどうなさいました？
お飲み物は何になさいますか？
どうかなさいましたか？
今年の夏休みはどうなさるつもりですか。
その損を私のせいになさろうとするんですか。
なぜわざわざわたしに警告なんかなさるの？
あまり期待なさらないでくださいよ。
お気になさらないでください。彼は普段から無口なので…

'''


def match_nasaru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for てところ
            {},
            {"pos": "VERB", "lemma": "なさる"},
            {},
        ]
    ]

    matcher.add("nasaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
