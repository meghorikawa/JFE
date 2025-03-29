# main method I need to create seperate line items for each participant and each writing.

# participant_writing num　


import spacy
from rules import rule_modules  # Dynamically import all rule files

nlp = spacy.load("ja_ginza")

def apply_matching(text):
    doc = nlp(text)  # Process text through pipeline first
    all_matches = {}

    for module_name, module in rule_modules.items():
        for attr in dir(module):
            if attr.startswith("match_"):
                match_func = getattr(module, attr)
                if callable(match_func):
                    all_matches[attr] = match_func(nlp, doc)

    return all_matches

# Example usage
text = "この映画はあまり面白くない。私はあまり食べない。今日こそ早く寝るつもりだ。あなたこそ私の大切な友達です。努力こそ成功への鍵だ。今こそ行動を起こすべきだ。この本こそ探していたものだ。健康こそ何よりも大切だ。愛こそ人生の意味だと思う。あなたの努力こそ認められるべきだ。今度こそ試験に合格してみせる！親の気持ちこそ子供にはなかなか分からないものだ。"
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")