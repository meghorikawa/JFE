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
この教科書の説明はわかりやすくて、しかも詳しい 。
今日はとても暑い。しかも、湿度も高いので何もしたくないだ。
彼は仕事がとても早い。しかも、正確で丁寧だから安心して任せられる。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")