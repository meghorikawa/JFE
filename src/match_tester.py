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
試験の前だから、勉強しないではいられない。
態度悪いの店員に、一言文句を言わないではいられない。
友達がいじめられているところを見たので、何か言わないではいられなかった。
彼の真似を見るとおかしくて、笑わないではいられない。
台風 の影響が心配で、畑を見に行かないではいられなかった。
彼女はわからないことがあったら、辞書やインターネットですぐに調べないではいられない性格だ。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")