import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb (causative passive form させ)	られる
くる	 = こさせられる
やる	= やらせられる

仕事を辞めさせられた。
息子は退学させられた。
彼女に2時間も待たせられた。
その映画は考えさせられる。
毎日母に野菜を食べさせられる。
フィアンセのお父さんにお酒を飲ませられた。

'''


def match_saserareru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos":"VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos":"AUX", "lemma": {"IN": ["せる","させる"]}},
            {"pos": "AUX", "lemma": "られる"},
        ],
    ]

    matcher.add("saserareru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
