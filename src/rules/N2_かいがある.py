import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

["Verb (casual, past)", 
"Verb (ます stem)","Noun + の"]  +  かいがある
    かいがあって
    がいがある


努力の甲斐があって、希望の大学に合格した。
美味しいと言ってたくさん食べてくれると、頑張って作った甲斐があります。
毎日ダイエットを頑張った甲斐があって、５キロ痩せることができました。
お客さんに喜んでもらえると、この仕事は、やり甲斐があると思う。
毎日つまらない仕事ばかりしている。もっと働き甲斐がある会社に転職したい。


'''


def match_kaigaru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {},
            {"pos": "VERB"},
            {"pos": "AUX", "OP": "?"},
            {"pos": "NOUN", "lemma": {"IN": ["かい", "がい", "甲斐"]}},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "VERB", "lemma": "ある"}
          ],[  # general pattern with noun
            {},
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "の"},
            {"pos": "NOUN", "lemma": {"IN": ["かい", "がい", "甲斐"]}},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "VERB", "lemma": "ある"}
          ], # need a case for やり甲斐, 働き甲斐　- they are considered one word.
        [
            {"pos": "NOUN", "text": {"REGEX": ".+甲斐$"}},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "VERB", "lemma": "ある"}
        ]
    ]

    matcher.add("kaigaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
