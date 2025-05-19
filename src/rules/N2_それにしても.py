import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"nevertheless", "even so", 

それにしてもあなたは絵が上手ですね。
それにしても私はあなたが優秀だと思います。
今日は早く帰ると言ったが、それにしても8時半まで残業した。
それにしてもあなたは遅くまで働くつもりですか。
彼女がちょっと遅刻すると言ったが、それにしても遅くない？
日本の夏はいつも蒸し暑いですよ。それにしても今年はずいぶん蒸し暑いですね。

'''


def match_sorenishitemo_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": "PRON", "lemma": "それ"},
            {"pos": "SCONJ", "lemma":"に"},
            {"pos": {"IN":["VERB", "AUX", "SCONJ"]}, "lemma": "する"},
            {"pos": "SCONJ", "lemma": "て"},
            {"pos": "SCONJ", "lemma": "も"},
        ],
    ]

    matcher.add("sorenishitemo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
