

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"unable to ..." ; "can't afford to ..." 

VERB て form + はいられない
NOUN + で  + はいられない
なadjective + で　＋　はいられない
いadjective - い + くて+ はいられない

ぐずぐずしてはいられない
泣かないではいられない。
彼の言うことを信じないではいられない。
元気ではいられない。
もうすぐ試験だから遊んではいられない。勉強に集中しなきゃ。
今年から大学生になるから、いつまでも親に頼ってはいられない。
明日は早く起きるので、いつものように遅くまで本を読んではいられない。
やると決めたら、のんびりしてはいられない。今すぐ準備を始めよう。

'''


def match_tehairarenai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": {"IN": ["AUX", "VERB"]}},
            {"pos": "SCONJ", "orth":{"IN": ["て","で"]}},
            {"pos": "ADP", "lemma": "は"},
            {"pos": "VERB", "lemma": "いる"},
            {"pos": "AUX", "lemma": "られる"},
            {"pos": "AUX", "lemma": {"IN": ["ない","ます"]}}
        ],[ #adj pattern
            {"pos": "ADJ"},
            {"orth":{"IN": ["て","で"]}},
            {"pos": "ADP", "lemma": "は"},
            {"pos": "VERB", "lemma": "いる"},
            {"pos": "AUX", "lemma": "られる"},
            {"pos": "AUX", "lemma": {"IN": ["ない","ます"]}}

            ]
        ]


    matcher.add("tehairarenai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
