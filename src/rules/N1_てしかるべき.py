

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"should" , "appropriate" 

            て然るべきだ
VERB て + しかるべき

後輩なら先輩に敬語を使ってしかるべきだ。
退学する前に、親と相談してしかるべきだ。
この小説はもっと評価されてしかるべきだ。こんなに面白い本は読んだことがない。
この道には車がたくさん通っているのだから、信号があってしかるべきだ。
状況が変わったのだから、会社の経営計画も見直されてしかるべきだ。
優秀な学生には奨学金が与えられてしかるべきだ。
女性は料理ができてしかるべきだという考え方は古い。
老人のための国立の病院がもっとあってしかるべきだ。


'''
def match_teshikarubeki_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN":["VERB","AUX"]}},
            {"pos":"SCONJ", "lemma": "て"},
            {"pos": "VERB", "lemma": {"IN":["しかり", "然り"]}},
            {"pos": "AUX", "lemma": "べし"}
        ],
        ]


    matcher.add("teshikarubeki", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
