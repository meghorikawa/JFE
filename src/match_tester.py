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
僕の成績から言えば、国立大学は無理だと思う。
能力から言って、彼がこの仕事に一番適切だと思います。
現状から言って、直ちにその計画を実行するのは無理だ。
この作文は、日本語能力から言えば、まだまだだが、内容はいい。
僕の経験から言うと、留学をする前に基本的な文法や単語は復習しておいた方がいい。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")