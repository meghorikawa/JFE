# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''
寒い日は、熱いラーメンに限る。
風邪には寝ているに限る。
何といっても我が家に限る。
夏は冷たいビールに限る。
うちの娘に限って、人をいじめるようなことはしません。
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
