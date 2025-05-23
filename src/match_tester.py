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
やがて真っ暗になった。
やがて考えがまとまってきた。
空は曇ってきた。やがて雨になるかもしれない。
やがてうちの近くの公園は桜が咲きます。
彼が親と喧嘩して家を出てからやがて三年になる。
やがて、彼らは厳しい現実を受け入れるようになった。
彼は来る途中ですから、やがて到着するでしょう。
父の病気はとてもよくなったから、やがて退院できるだろう。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")