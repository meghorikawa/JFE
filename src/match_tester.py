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
大学生は宿題やらアルバイトやらで忙しい。
さっきコンビニでおにぎりやらお茶やらを買った。
疲れやら空腹やらで、彼は死んだように倒れた。
サイクリングをする時は嬉しいやら楽しいやら、とてもいい気分だ。
カバンにはパソコンやらノートやら教科書やらが入っている。
両親からの仕送りは、家賃やら食費やらでほとんどなくなってしまった。
たくさんの蚊に食われて、かゆいやら痛いやらで大変だった。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")