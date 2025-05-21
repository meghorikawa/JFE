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
私はむしろ一人で行きたい。
私はむしろ電車で行くだろう。
この商品は、女性をターゲットに作られたが、実際は、むしろ男性に人気があるようだ。
遅くまで残業するより、むしろ早く帰ってしっかり頭と体を休んだほうが、効率がいい。
彼はいつも優しくないから、急に優しくなるとうれしいというより、むしろこわい。
自由な考え方が必要とされる仕事は、大人よりむしろ小さい子供の方が得意かもしれません。
観光客向けの商品より、むしろ地元の人がよく買う物の方が、お土産にはお勧めです。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")