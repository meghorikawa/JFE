# main method I need to create separate line items for each participant and each writing.

# participant_writing num　


import spacy
from rules import rule_modules  # Dynamically import all rule files

nlp = spacy.load("ja_ginza")

def apply_matching(text):
    doc = nlp(text)  # Process text through pipeline first
    all_matches = {}

    for module_name, module in rule_modules.items():
        for attr in dir(module):
            if attr.startswith("match_"):
                match_func = getattr(module, attr)
                if callable(match_func):
                    all_matches[attr] = match_func(nlp, doc)
    print(f'Number of Forms: {len(rule_modules)}')
    return all_matches

# Example usage
text = ('''
きれいだと思わない？
それはかなりむずかしいと思います。
今日は午後から雨が降ると思います。
この問題、テストに出ると思いますか。
日本に留学しようと思っています。
仕事を続けるのはむりだと思う。
アメリカでは、何が一番人気のあるスポーツだと思う？
今度の休みに海へ行こうと思っています。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")