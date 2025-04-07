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

彼は入院しているところです。
今料理をしているところです。
私は今、家で日本語を勉強しているところです。
姉は電話をかけているところだ。
子どもを産んだばかりなので、うちで休んでいるところです。
彼女はお茶を飲みながら雑誌を読んでいるところです。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")