

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"otherwise" with two options given


NOUN もしくは NOUN



遅刻するの場合は先生もしくは僕に連絡してください。
お問い合わせは、電話もしくはファックスでお願いします。
あの男は弁護士もしくは裁判官ですか。
参加費はクレジットカードもしくは現金で払うことができます。
この施設は、会員もしくはその家族に限り使用できる。
明日は社長もしくは部長が新計画を発表なさります。
同封の許可証にご両親もしくは保護者の同意署名をもらってください。




'''
def match_moshikuha_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "NOUN"},
            {"pos":"CCONJ","lemma": "もしくは"},
            {}
        ],
        ]


    matcher.add("moshikuha", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
