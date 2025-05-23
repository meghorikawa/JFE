

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"Without caring"

彼女は服が汚れるのもかまわず、公園で犬と遊んでいる。
あの男は人目もかまわず、電車の中で弁当を食べている。
あの二人は、みんなが見ているのもかまわず、キスをした。
彼は値段もかまわず、好きな料理をどんどん注文した。
病院であるのもかまわず、あの女性は携帯電話で大きな声で話している。
隣の人たちは近所の人の迷惑もかまわず毎晩遅くまで騒いでいる。
最近、電車の中で、人目もかまわず化粧をしている若い女性をよく見かける。
雨が降っていたが、ナナさんは濡れるのもかまわず走って帰ってしまった。

'''
def match_mokamawazu_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "ADP", "lemma": "も"},
            {"pos":"VERB", "lemma": {"IN":["構う", "かまう"]}},
            {"pos": "AUX", "lemma": "ず"}
        ],
        ]


    matcher.add("mokamawazu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
