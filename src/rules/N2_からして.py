import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

Noun + からして
"based on", "Since", "even..." 

タイトルからして、面白そうな本ですね。
その新社員は顔つきからして優しそうだ。
この子は笑い方からして母親にそっくりだ。
このレストランは雰囲気からして結構高そうだね。
これまでの実績からして、Aチームが勝つと予想した人が多かった。


'''


def match_karashite_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "から"},
            {"pos": {"IN": ["AUX","VERB"]}, "lemma": "する"},
            {"pos": "SCONJ", "lemma": "て"},
        ],
    ]

    matcher.add("karashite", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
