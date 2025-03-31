# main method I need to create separate line items for each participant and each writing.

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
text = ("この曲を聞くたびに、家族を思い出す。友人は旅行のたびにお土産を買ってきてくれます。あの人を会うたびに用事を頼まれる。ミスをするたびに部長にしかられる。買い物のたびに、袋をたくさんもらう。")
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")