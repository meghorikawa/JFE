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
大学生にも関わらず、基本的な漢字が書けない人もいる。
問題が易しかったにも関わらず、不注意でミスをしてしまった。
一生懸命勉強したにも関わらず、入りたかった大学の試験に落ちてしまった。
彼は全く日本語が話せないにも関わらず、日本で生活したいと言っている。
校則で禁止されているにも関わらず、授業中にスマホを使う学生が多い。
彼女は日本語が上手であるにも関わらず、日本人と会話する時はいつも英語を使う。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")