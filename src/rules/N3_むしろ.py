

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

"rather", "instead"

私はむしろ一人で行きたい。
私はむしろ電車で行くだろう。
この商品は、女性をターゲットに作られたが、実際は、むしろ男性に人気があるようだ。
遅くまで残業するより、むしろ早く帰ってしっかり頭と体を休んだほうが、効率がいい。
彼はいつも優しくないから、急に優しくなるとうれしいというより、むしろこわい。
自由な考え方が必要とされる仕事は、大人よりむしろ小さい子供の方が得意かもしれません。
観光客向けの商品より、むしろ地元の人がよく買う物の方が、お土産にはお勧めです。

'''
def match_mushiro_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos":"ADV", "lemma": "むしろ"},
        ],
        ]


    matcher.add("mushiro", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
