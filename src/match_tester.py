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

君はいかなる状況でも部屋を離れてはならない。
私はいかなる質問にも答えるつもりはない。
警察はいつもいかなる事態にも対処できる態勢にある。
私たちはいかなる損害にもその責任を負いません。
彼はいかなる難局にも処しうる男だ。
彼女はいかなる困難にであっても、気を落とすことはない。
我々はいかなる犠牲をはらっても目標を達成せねばならぬ。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")