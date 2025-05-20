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
ぐずぐずしてはいられない
泣かないではいられない。
彼の言うことを信じないではいられない。
元気ではいられない。
もうすぐ試験だから遊んではいられない。勉強に集中しなきゃ。
今年から大学生になるから、いつまでも親に頼ってはいられない。
明日は早く起きるので、いつものように遅くまで本を読んではいられない。
やると決めたら、のんびりしてはいられない。今すぐ準備を始めよう。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")