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
空が急に暗くなってきたかと思うと、雨が降ってきた。
うちの近くの公園の花が咲いたかと思ったら、もう散ってしまった
この時期は、晴れていたかと思えば、急に雨が降り出すことが多いから、傘をもっていったほうがいい。
さっきまで笑っていたかと思ったら、急に泣き出してしまった。
日曜日なのに、お父さんは忙しそうだね。さっき戻ったかと思うと、また出かけて行った。
彼は食事を始めたかと思ったら寝てしまった。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")