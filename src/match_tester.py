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
こんな蒸し暑い天気は、どうにも我慢できない。
彼女が亡くなったことをどうにも信じられない。
彼の怠惰な性格は、どうにも直しようがない。
その携帯電話はどうにも直しようがないほどに壊れてしまった。
彼はどうにも身の置き場がないような様子だ。
聴衆はコンサートが始まるのをどうにも待ちきれなかった。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")