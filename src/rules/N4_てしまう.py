import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb (て form)	+   しまう
                    しまいます
                    しまった
Verb	+   ちゃう
                    ちゃった
Verb	+   じゃう
                    じゃった

仕事は全部終わってしまいました。
疲れが出たので、寝ちゃった。
パスポートをなくしてしまいました。
漢字の宿題はもうやってしまいました。
明日までに宿題をしちゃいます。
ごめん！ジュースを全部飲んじゃった！

'''


def match_teshimau_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [[# general patern - Verb + で + しまう
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": "しまう"},
        ], [ # pattern for casual forms ちゃう and じゃう
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": {"IN":["ちゃう", "じゃう"]}},
    ]
    ]

    matcher.add("teshimau", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
