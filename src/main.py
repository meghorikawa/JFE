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
先生の答えがいつも正しいとは限りません。
こういう音楽は誰でも好きだとは限らない。
お金持ちになれば、必ず幸せになるとは限りません。
いい大学を卒業したから、いい会社に入れるとは限らない。
無料のほうがいいとは限らない。無料のものは質が低いものが多いです。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")