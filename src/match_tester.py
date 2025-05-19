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
それにしてもあなたは絵が上手ですね。
それにしても私はあなたが優秀だと思います。
今日は早く帰ると言ったが、それにしても8時半まで残業した。
それにしてもあなたは遅くまで働くつもりですか。
彼女がちょっと遅刻すると言ったが、それにしても遅くない？
日本の夏はいつも蒸し暑いですよ。それにしても今年はずいぶん蒸し暑いですね。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")