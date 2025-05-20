

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"Furthermore", "in addition" - used to add additional information


かなり多くの人々が今なおそれを信じている。
とても寒く、なお悪いことに、雨が降り始めた。
今度の打ち合わせは土曜日です。なお、時間は後ほどお伝えします。
あとで起こったことはなお悪かった。
この件の説明は以上です。なお、詳細についてプリントをご覧ください。
この試合に申し込むとき、履歴書を提出してください。なお参加費も提出してください。


'''


def match_nao_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": {"IN":["CCONJ","ADV"]}, "lemma": "なお"},
        ],
        ]


    matcher.add("nao", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
