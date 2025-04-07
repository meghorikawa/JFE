import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4
N3 level form uses a verb instead of a noun

Noun + しかない (しかありません)

一時間しかありません。
この店には現金しか使えません。
彼には真実しか話していません。
昨日はパンしか食べてない。
この町にはコンビニしかないよ。
クラスに女の子が二人しかいない。
彼しか信じられない。
行ける場所がここしかないんだ


'''


def match_shikanai_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for plain form
            {"pos": {"IN": ["NOUN", "PRON", "ADV"]}},
            {"pos": "ADP", "orth": "しか"},
            {"pos": "VERB" , "lemma": "いる", "OP": "?"},
            {"lemma": "ない", "pos": {"IN": ["AUX", "ADP", "ADJ"]}},
            {"orth": "た", "pos": "AUX", "OP": "?"}  # optional argument for た to capture past tense casual form
        ], [  # Pattern for polite form
            {"pos": {"IN": ["NOUN", "PRON", "ADV"]}},
            {"pos": "ADP", "orth": "しか"},
            {"lemma": {"IN": ["ある","いる"]}, "pos": "VERB"},
            {"lemma": "ます", "pos": "AUX"},
            {"lemma": "ぬ", "pos": "AUX"},
        ]
    ]

    matcher.add("shikanaiN4", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
