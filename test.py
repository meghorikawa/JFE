# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''
今まで以上に仕事を頑張ります。
必要以上にたくさんのお金を使わないでください。
私が予想していた以上に彼の様態はよくなかった。
今以上に日本語ができるようになりたいです。
私たちが泊まったホテルは、予想以上に豪華だった。
彼らは、わたしが考えた以上に強い反応を示した。
''')
processed_text = pipeline.preprocess(text)

nlp = spacy.load("ja_ginza")
doc = nlp(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")
sentences = doc.sents
for sentence in sentences:
    clauses, subordinate, coordinate = clauseExtractor.extract_clauses(sentence)
    print(f' Clauses: {clauses}, Subordinate: {subordinate}, Coordinate: {coordinate}')
