# a method created to test the different functions.

from src import pipeline, clauseExtractor, PhraseExtractor
import json
import spacy
from ginza import clauses, clause_head, clause_head_i



text = ('''
彼は学校へ行き勉強をし友達と話した後で家に帰った。
''')
processed_text = pipeline.preprocess(text)

nlp = spacy.load("ja_ginza")
doc = nlp(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")
sentences = doc.sents

print(f'Verb phrases {PhraseExtractor.extract_verb_phrases(doc)}')
print(f'Noun phrases {PhraseExtractor.extract_noun_phrases(doc)}')
for sentence in sentences:
    clause_list, subordinate, coordinate = clauseExtractor.extract_clauses(sentence)
    print(f' Clauses: {clause_list}, Subordinate: {subordinate}, Coordinate: {coordinate}')
