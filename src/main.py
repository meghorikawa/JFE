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
箸は使いにくいです
この質問には答えにくいです。
この本は字が小さくて読みにくいです。
この漢字は覚えにくいです。
この自転車は古くて乗りにくいです。
魚は骨が多くて食べにくいだ。
彼の説明が難しくて分かりにくいだった。
この道は狭くて、車も多いので、運転しにくいです。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")