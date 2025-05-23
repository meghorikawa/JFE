

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1
"only because~"

VERB (conditional) + こそ
Noun + であれば +こそ
なadjective + であれば+ こそ
いadjective + ければ + こそ

優勝できたのは、チーム全員の協力あればこそだ。
家族を愛すればこそ、自分が犠牲になることなどは恐れない。
子供のためを思えばこそ、費用は子ども自身に用意させたのです。
自分の努力を認めてくれる人がいればこそ、やる気も出てくるというものだ。
忙しければこそ、時間の使い方が上手になってくるものだ。
夜中に一人で歩いて帰れるのも、この街が安全であればこそだ。
娘の将来を思えばこそ、彼との結婚には賛成できない。


'''
def match_bakoso_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "SCONJ", "lemma": "ば"},
            {"pos": "ADP", "lemma": "こそ"}
        ],
        ]


    matcher.add("bakoso", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
