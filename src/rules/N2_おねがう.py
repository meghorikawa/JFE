import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

お + Verb ます (stem form)	願います ; 願えますか


しばらくお待ち願います。
図書館では小さな声でお話し願います。
ご提案の詳細についてお聞かせ願えますか？
ご自分のシートベルトが安全にかかっているかお確かめ願います。

'''


def match_onegau_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["NOUN", "VERB"]}, "lemma": {"IN": ["お","ご"]}},
            {"pos": {"IN": ["VERB", "NOUN"]}},
            {"pos": "AUX", "OP": "?"},
            {"pos": "VERB", "lemma": {"IN": ["願う","願える"]}},
          ],
    ]

    matcher.add("onegau", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
