# this is a python script to test the matcher as I continue implementation.
# I am keeping this separate from the main method for now
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
    #print(f'Number of Forms: {len(rule_modules)}')
    return all_matches

# Example usage
text = ('''
単に幸運だったにすぎない。
これはまだ始まりにすぎない。
そんなのは言い訳に過ぎない。
それはただの道具にすぎない。その道具をどう使うかが大切だ。
病気で病院へ行ったといっても、ただの風邪に過ぎない。
私はこの会社の一社員にすぎませんから、決定権はありません。
いくら働いても一ヶ月の収入は２０万円にすぎない。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")