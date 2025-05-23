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
彼はあえて一人で行く気ですか。
私はあえて彼女に忠告した。
あえて彼の意見を支持した。
私は、あえて彼に電話をしない。
その時彼女はあえて何も言わなかった。
正社員じゃなく、あえてアルバイトとして働く人も多いです。
私だったらそれを思いのまま言うようなことはあえてしない。
最近は、車じゃなくてあえて自転車で通勤する人が増えている。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")