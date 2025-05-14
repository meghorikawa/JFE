import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

verb(non-past) + 限り
Noun + である+ 限り

明日は、雨が降らない限り、10時に学校で会いましょう。
この仕事は、私が生きている限り、ずっと続けていきたい。
私の知っている限りでは、彼女はまだ結婚していません。
学生である限り、学割が使えます。
日本にいる限り、日本語が必要だよ。
今のやり方を変えない限り、悪い状況は続くでしょう。
お店の中にお客様がいる限り、お店は閉めません。
悪い生活習慣を改めない限り、健康にはなれない。
自分の歌を聞いてくれる人がいる限り、路上で歌たい続けようと思います。


'''


def match_kaigiri_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": "VERB"},
            {"pos": "SCONJ", "lemma": "て", "OP": "?"}, # add optional argument for て form
            {"pos": "AUX", "OP": "?"},
            {"pos": "NOUN", "lemma": {"IN": ["限り","かぎり"]}},

          ],[  # pattern with noun
            {"pos": "NOUN"},
            {"pos": "AUX", "lemma": "で"},
            {"pos": "VERB", "lemma": "ある"},
            {"pos": "NOUN", "lemma": {"IN": ["限り","かぎり"]}},
          ],
    ]

    matcher.add("kagiri", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
