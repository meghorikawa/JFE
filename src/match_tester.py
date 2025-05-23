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
仕事は君に信頼するよりほかはない。
バスがないので、歩いていくよりほか仕方がない。
頼れる人はいないから、自分がやるよりほか仕方がない。
僕は学力が足りないから勉強で補うよりほかはない。
自転車が壊れてしまった。学校へバスで行くよりほか仕方がない。
台風が来るので、残念だが明日の大会は延期するよりほかない。
こんな経営状況が続くようであれば、店を閉めるよりほかないですよ。
薬は嫌いだが、飲まないと病気を治せないから、飲むよりほか仕方がない。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")