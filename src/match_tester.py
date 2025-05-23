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
秋であるものの、まだ暑い。
申し込みはしたものの、試験を受けるかどうか未定です。
車の免許は持っているものの、ほとんど運転したことがありません。
買ったものの、使い方が分からない。
金欠ではあるものの、毎日美味しい食事を楽しんでいる。
私のアパートは駅からはちょっと遠いものの、静かできれいな住宅街にある。
友人に勧められてスポーツジムの会員になったものの、ほとんど利用していない。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")