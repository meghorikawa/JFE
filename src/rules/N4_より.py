import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


[A]より[B]
OR より + adjective

花より団子
今日は昨日より暑いです。
今は恋愛より仕事だ。
彼女は、私より料理が上手。
それより安くは売られません。
今朝はいつもより早く学校へ来ました。
漢字はひらがなやカタカナより難しいだと思います。

'''


def match_yori_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for より
            { },
            {"pos": "ADP", "lemma": "より"},
            {}
        ],
    ]

    matcher.add("yori", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
