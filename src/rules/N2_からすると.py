import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

Noun + からすると、　からすれば
"juding from" , "Considering"

彼の症状からすると、心臓の病気かもしれません。
今度のJLPTですが、今の皆さんの実力からすると問題なく合格できるでしょう。
ラーメンを食べる時に音を出す習慣は外国人からすると、考えられないことだそうです。
親からすれば、子供はいくつになっても子供で心配なものだ。

'''


def match_karasuruto_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "から"},
            {"pos": {"IN": ["AUX","VERB"]}, "lemma": "する"},
            {"pos": "SCONJ", "lemma": {"IN" : ["と","ば"]}},
        ],
    ]

    matcher.add("karasuruto", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
