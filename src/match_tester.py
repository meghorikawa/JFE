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

彼女との思い出は語り出したら切りがない。
彼の欠点を数えれば切りがない。
日本戦争に関する本は数え上げたら切りがない。
彼がいったん不平を言い始めると切りがない。
欲を言えば切りがないから、このマンションに決めよう。
悩み出したら切りがないので、途中で吹っ切れることも重要だ。
旅行に行きたいところを挙げれば切りがないので、なるべく考えないことにする。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")