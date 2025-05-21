

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"but then"; "although"

もっとも

全員が参加しなければなりません。もっとも病気の場合は別です。
今回の失敗は田中さんの責任だ。もっとも、私たちも責任を一部持ちます。
検査の前夜から飲食禁止です。もっとも水は飲んでも構いません。
今年こそヨーロッパへ行きたいと思っています。もっとも休みが取れたらの話ですが。
今日の試合は私たちのチームが勝った。もっとも、次の試合はもっと難しいので無視にしないほうがいい。
ウィキペディアに全部書いてあるよ。もっともこのサイトは完全には信用できないけど。
関係ない人は書類をもらわないでください。もっとも、許可を持っている人がもらえます。


'''
def match_mottomo_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos":{"IN": ["ADV", "CCONJ"]}, "lemma": {"IN":["もっとも", "尤も"]}},
        ],
        ]


    matcher.add("mottomo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
