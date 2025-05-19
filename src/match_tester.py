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
ここのレストランはどれも安いだけでなく、美味しい。
この公園では、子供だけではなく大人も楽しむことができる。
彼女は日本語が上手なだけでなく、英語もペラペラだ。
君だけでなく僕も悪かった。
彼は知識だけではなく、経験も豊かである。
肉だけでなく野菜も食べなさいよ。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")