# main method I need to create separate line items for each participant and each writing.

# make a list of each directory () in corpus

import spacy
from rules import rule_modules  # Dynamically import all rule files

nlp = spacy.load("ja_ginza")

def apply_matching(text):
    doc = nlp(text)  # Process text first
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
そんなことを信じられない。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")