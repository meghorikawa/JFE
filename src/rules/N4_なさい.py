import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb ます (stem form)	なさい
                        な (conversation) - I won't include this

まず、質問に答えなさい。
明日、学校に行くから、早く寝なさい！
うるさいだよ。静かにしなさい！
野菜は体にいいからもっと食べなさい！
明日の9時に私に電話しなさい！
次の質問を見て、ここに答えなさい！
分からなかったら先生に聞きなさい！
人からされたいと思うことを、自ら人にしなさい。

'''


def match_nasai_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for てところ
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "なさる"},
        ]
    ]

    matcher.add("nasai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
