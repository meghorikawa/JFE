

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"based on", "on the basis of ~" 

Noun に基づいて、に基づく

この小説は実際にあったことに基づいて書かれたそうです。
このテストの結果に基づいて君たちのクラスを分けるので、頑張ってください。
集めた資料に基づいて、卒業の論文を書きました。
私は長年の経験に基づき新入社員を教育する。
公務員の給与は、法律に基づいて決められています。
アンケート結果に基づいて、新商品の方向性を決めるつもりだ。

'''
def match_nimotodzuite_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "に"},
            {"pos": "VERB", "lemma": {"IN": ["基づく","もとづく"]}},
            {},
        ],
        ]


    matcher.add("nimotodzuite", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
