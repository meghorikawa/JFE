

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"To have not choice but~"

Two forms: 
    よりほかはない
    よりほか仕方がない

この仕事は君に信頼するよりほかはない。
バスがないので、歩いていくよりほか仕方がない。
頼れる人はいないから、自分がやるよりほか仕方がない。
僕は学力が足りないから勉強で補うよりほかはない。
自転車が壊れてしまった。学校へバスで行くよりほか仕方がない。
台風が来るので、残念だが明日の大会は延期するよりほかない。
こんな経営状況が続くようであれば、店を閉めるよりほかないですよ。
薬は嫌いだが、飲まないと病気を治せないから、飲むよりほか仕方がない。


'''
def match_yorihokanai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADP", "lemma": "より"},
            {"pos": "NOUN", "lemma": {"IN": ["ほか","他"]}},
            {"pos": "NOUN", "lemma": "仕方", "OP": "?"},
            {"pos": "ADP", "OP": "?"},
            {"pos": {"IN": ["ADJ", "AUX"]}, "lemma": "ない"} #consider polite formありません
        ], [  # polite form ありません
            {"pos": "ADP", "lemma": "より"},
            {"pos": "NOUN", "lemma": {"IN": ["ほか","他"]}},
            {"pos": "NOUN", "lemma": "仕方", "OP": "?"},
            {"pos": "ADP", "OP": "?"},
            {"pos": "VERB", "lemma": "ある"}
        ]
        ]


    matcher.add("yorihokanai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
