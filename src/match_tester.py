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
お母さんは優しい一方で、お父さんはこわい。
父は自分に厳しい一方で、他人には優しい。
彼女の仕事は夏は非常に忙しい一方、冬は暇になる。
彼は俳優である一方で、歌手としても活躍している。
海外旅行は非日常を体験できることから、楽しいと感じることが多い一方で、不安なこともある。
その仕事はあまり面白くなかったが、その一方で給与はよかった。
老人の人口が増えている一方で、若年労働力の数がどんどん減っています。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")