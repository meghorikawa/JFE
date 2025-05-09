

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

君の話を信じるよ。だってこの世界ではどんなことでも起こり得るから。
事故はいつでも起こり得るので、気をつけてください。
タバコを吸いすぎや、お酒を飲み過ぎは病気の原因になり得ます。
運動不足は病気の原因になり得るので、できるだけ体を動かすようにしてください。
この不況では大手企業の倒産もあり得る。
1つのミスが、会社を倒産に導くこともあり得ることだ。気を抜かずに、頑張っていこう。


'''


def match_eru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["VERB", "AUX"]}},
            {"pos": "VERB", "lemma": {"IN": ["得る", "える","うる"]}},
            {"lemma": {"NOT_IN": ["ない"]}},
          ],
    ]

    matcher.add("eru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
