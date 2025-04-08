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
花より団子
今日は昨日より暑いです。
今は恋愛より仕事だ。
彼女は、私より料理が上手。
それより安くは売られません。
今朝はいつもより早く学校へ来ました。
漢字はひらがなやカタカナより難しいだと思います。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")