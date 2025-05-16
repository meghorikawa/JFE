import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2
"in terms of ....."

NOUN + から言うと、から言えば、から言って

僕の成績から言えば、国立大学は無理だと思う。
能力から言って、彼がこの仕事に一番適切だと思います。
現状から言って、直ちにその計画を実行するのは無理だ。
この作文は、日本語能力から言えば、まだまだだが、内容はいい。
僕の経験から言うと、留学をする前に基本的な文法や単語は復習しておいた方がいい。


'''


def match_karaiuto_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　言えば
            {"pos": "ADP", "lemma": "から"},
            {"pos": "VERB", "lemma": "言う"},  # add optional argument for て form
            {"pos": "SCONJ", "lemma": {"IN": ["ば","て", "と"]}},
        ],
    ]

    matcher.add("karaiuto", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
