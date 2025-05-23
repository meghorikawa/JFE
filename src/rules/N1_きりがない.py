

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"endless", "going on forever" 

VERBば
VERBたら  + きりがない
VERBと

彼女との思い出は語り出したら切りがない。
彼の欠点を数えれば切りがない。
日本戦争に関する本は数え上げたら切りがない。
彼がいったん不平を言い始めると切りがない。
欲を言えば切りがないから、このマンションに決めよう。
悩み出したら切りがないので、途中で吹っ切れることも重要だ。
旅行に行きたいところを挙げれば切りがないので、なるべく考えないことにする。


'''
def match_kirigani_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {},
            {},
            {"pos": "NOUN", "lemma": {"IN":["きり","切り"]}},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "VERB", "lemma": "ある", "OP":"?"},
            {"lemma":{"IN":["ない","ます"]}}
        ],
        ]


    matcher.add("kiriganai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
