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
あの人が結婚したって本当！？え～！あり得ないよ！
あの真面目な彼が犯人？そんなことはあり得ない。
地震がいつ来るかなんて、予測し得ないことだ。
君の話を信じるよ。だってこの世界ではどんなことでも起こり得るから。
事故はいつでも起こり得るので、気をつけてください。
タバコを吸いすぎや、お酒を飲み過ぎは病気の原因になり得ます。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")