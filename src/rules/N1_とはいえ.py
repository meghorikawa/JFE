

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"though", "although", "nonethless"

教師とはいえ、答えられないこともある。
分かっているとはいえ、やっぱり別れは辛いものだ。
私は日本人だとはいえ、アメリカで育ったので、漢字があまり読めません。
まだ締め切りまで時間があるとはいえ、早めに完成したほうがいい。
もう過去のこととはいえ、そう簡単には許すことはできない。
知らなかったこととはいえ失礼なことをしてしまい、大変申し訳ありませんでした。
入社したばかりとはいえ、もう少しまともな挨拶が出来ないのだろうか。
彼はまだ未成年だとはいえ、自分の犯した行為にしっかりと責任を持つべきだ。

'''

def match_tohaie_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "ADP", "lemma": "と"},
            {"pos":"SCONJ", "lemma": "は"},
            {"pos": "SCONJ", "lemma": {"IN":["いう","言う"]}}
        ],
        ]


    matcher.add("tohaie", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
