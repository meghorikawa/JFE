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
あらかじめ教科書を読んでください。
私たちはあらかじめスナックを用意しておきました。
僕は逃げ道をあらかじめ探しました。
私はその資料をあらかじめ印刷して持参します。
私たちはそれをあらかじめ考慮しておく必要がある。
訪ねていらっしゃる前にあらかじめ連絡してください。
会社の忘年会のためにあらかじめレストランを予約しました。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")