# This is a method to calculate the Morphological Complexity Index as described in
# Brezina and Pallotti 2019 "Morphological Complexity in written L2 texts"

import random
from collections import defaultdict
from statistics import mean

'''
1. Exract all unique verb lemma+form tokens
2. randomly select K verbs without repition from each subset (k=5 or k=10)
3. Repeat sampling process n times
4. Calculate mean MCI across the n samples'''

def MCI_10 (verb_list, sample_size, n_samples):
    if sample_size > len(verb_list):
        return None # there aren't enough verbs to sample from the text

    surface_mci = []
    inflection_mci = []

    for i in range(n_samples):
        sample = random.sample(verb_list, sample_size)


# method to extract verbs from the text
def get_verb_list (doc):
    verb_data = []
    for token in doc:
        if token.pos_ == 'VERB':
            lemma = token.lemma_
            surface = token.text
            inflections = token.morph.get("Inflection")
            verb_data.append((lemma, surface, inflections))
    return verb_data
