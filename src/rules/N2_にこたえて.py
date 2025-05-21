

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"in response to~"

NOUN に応えて（応える）（応え）

大学は、学生たちの要望にこたえて、図書館の利用時間を延ばした。
お客様の意見にこたえて、営業時間を延長することいたしました。
クライアントの要望にこたえて、新しい機能を追加いたしました。
多くのファンの声援にこたえる完璧なプレーをし遂げた。
我が社では消費者のニーズにこたえる新しい商品を開発中です。
両親の期待にこたえて、私はイギリスに留学した。

'''
def match_nikotaete_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "ADP", "lemma": "に"},
            {"pos": "VERB", "lemma": {"IN": ["応える","こたえる"]}},
            { },
        ],
        ]


    matcher.add("nikotaete", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
