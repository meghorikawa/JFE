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
まず、質問に答えなさい。
明日、学校に行くから、早く寝なさい！
うるさいだよ。静かにしなさい！
野菜は体にいいからもっと食べなさい！
明日の9時に私に電話しなさい！
次の質問を見て、ここに答えなさい！
分からなかったら先生に聞きなさい！
人からされたいと思うことを、自ら人にしなさい。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")