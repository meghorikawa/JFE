

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1
"not ... by any means", "no matter how hard one tries, cannot...." 
どうにも+ VERB(neg)
どうにも+　NOUN がない

こんな蒸し暑い天気は、どうにも我慢できない。
こんな蒸し暑い天気は、どうにも我慢できない。
彼女が亡くなったことをどうにも信じられない。
彼の怠惰な性格は、どうにも直しようがない。
その携帯電話はどうにも直しようがないほどに壊れてしまった。
彼はどうにも身の置き場がないような様子だ。
聴衆はコンサートが始まるのをどうにも待ちきれなかった。



'''
def match_dounimonai_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": "ADV", "lemma": "どう"},
            {"pos": "ADP", "lemma": "に"},
            {"pos": "ADP", "lemma": "も"},
            {"pos": "VERB"},
            {"OP":"?"},
            {"pos": {"IN":["AUX", "ADJ"]}, "lemma": "ない"},
        ],[ # noun pattern
            {"pos": "ADV", "lemma": "どう"},
            {"pos": "ADP", "lemma": "に"},
            {"pos": "ADP", "lemma": "も"},
            {"OP":"?"}, #optional slot for verb which can be turned into noun
            {"OP": "?"},
            {"pos": "NOUN"},
            {"OP": "?"},
            {"pos": "ADP","lemma": "が"},
            {"pos": {"IN": ["AUX", "ADJ"]}, "lemma": "ない"},
        ]
        ]


    matcher.add("dounimonai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
