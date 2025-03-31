import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (dictionary form)	+ ついでに
Verb (た form) + ついでに
Noun + の + ついでに

コンビニに行くなら、ついでにお茶も買ってきてくれない？
買い物のついでに、本屋に寄りました。
仕事へ行くついでに駅まで送ってあげるよ。
出かけるの？それならついでにゴミを出してくれる？
引っ越しのついでに、新しい家具を買いたいです。


'''


def match_tsuideni_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"orth": "ついで", "pos": "NOUN"},
            {"orth": "に", "pos": "ADP"}

        ]
    ]

    matcher.add("tsuideni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
