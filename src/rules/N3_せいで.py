import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual) + past tense	+ せい（で/に)
Noun + の + せい（で/に)
Adjective い + せい（で/に)
Adjective　な + だった + + せい（で/に)

事故のせいで遅刻した。
さっきコーヒーを飲んだせいで、なかなか寝られません。
頭が痛い。疲れたせいかな。
あなたの失敗を、私のせいにしないでよ！
図書館が静かだったせいで、うっかり寝てしまった。
成績が悪かったせいで、パーティー行けなかった。


'''


def match_seide_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for Nouns
            {"pos": {"IN": ["NOUN", "PRON"]}},
            {"pos": "ADP", "orth": "の"},
            {"orth": "せい", "pos": "NOUN"}
        ], [  # pattern for verbs (with past tense
            {"pos": "VERB"},
            {"pos": "AUX", "orth": {"IN": ["た", "だ"]}, "OP": "?"},  # past tense た だ variation
            {"orth": "せい", "pos": "NOUN"},  # ず
        ], [  # pattern for Adjectives
            {"pos": "ADJ"},
            {"pos": "AUX", "lemma": {"IN": ["だ", "た"]}, "OP": "?"}, # optional auxilary for だ or た
            {"pos": "AUX", "orth": {"IN": ["た", "だ"]}, "OP": "?"},  # optional past tense た だ variation
            {"orth": "せい", "pos": "NOUN"},  # ず
        ]
    ]

    matcher.add("seide", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
