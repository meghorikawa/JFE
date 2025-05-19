# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''
彼の症状からすると、心臓の病気かもしれません。
今度のJLPTですが、今の皆さんの実力からすると問題なく合格できるでしょう。
ラーメンを食べる時に音を出す習慣は外国人からすると、考えられないことだそうです。
親からすれば、子供はいくつになっても子供で心配なものだ。
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
