

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"before long"; "eventually"; "soon"


やがて + phrase

やがて真っ暗になった。
やがて考えがまとまってきた。
空は曇ってきた。やがて雨になるかもしれない。
やがてうちの近くの公園は桜が咲きます。
彼が親と喧嘩して家を出てからやがて三年になる。
やがて、彼らは厳しい現実を受け入れるようになった。
彼は来る途中ですから、やがて到着するでしょう。
父の病気はとてもよくなったから、やがて退院できるだろう。



'''
def match_yagate_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADV", "lemma": "やがて"},
            {},
        ],
        ]


    matcher.add("yagate", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
