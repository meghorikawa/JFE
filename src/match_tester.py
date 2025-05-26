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

彼は物事を少しすぎる嫌いがある。
彼女は面接の時に緊張する嫌いがある。
この頃の若者は協調性に欠ける嫌いがある。
最近の子供はスマホやゲームの影響で夜遅くまで起きる嫌いがある。
うちの部長は自分と違う考え方を認めようとしない嫌いがある。
話をおもしろくするためだろうか、彼はものごとを大げさに言う嫌いがある。
彼は一度言い出したら、人の意見に耳を傾けない。少し独断の嫌いがある。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")