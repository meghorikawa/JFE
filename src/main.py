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

    return all_matches

# Example usage
text = ('''
もしかしたら、明日行けないかもしれない。
もしかしたら病気かもしれない。
もしかしたら彼は気が変わるかもしれません。
もしかすると彼の話はうそかもしれない。
もしかするとあそこに座っている人は有名な人かもしれない。
もしかすると、それは偽物かもしれない。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")