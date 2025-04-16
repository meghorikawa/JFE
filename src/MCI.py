# This is a method to calculate the Morphological Complexity Index as described in
# Brezina and Pallotti 2019 "Morphological Complexity in written L2 texts"
# Surface MCI (Morphological diversity) vs. Inflectional MCI (Grammatical variety)

import random
from collections import defaultdict
from itertools import combinations
from statistics import mean

import spacy

nlp = spacy.load('ja_ginza')

'''
1. Extract all unique verb lemma+form tokens
2. Randomly select K verbs without repetition from each subset (k=5 or k=10)
3. Repeat sampling process n times
4. Calculate mean MCI across the n samples'''


def MCI(text, sample_size, n_samples, mode):
    '''

    :param text: the processed learner text
    :param sample_size: number of samples (i.e. 5, or 10)
    :param n_samples: number of times to sample
    :param mode: 'surface' for only looking at surface forms or 'inflection'
    :return:
    '''

    verb_list = get_verb_list(text)

    if sample_size > len(verb_list):
        return None  # there aren't enough verbs to sample from the text

    sample_sets = []

    # random sampling without repetition
    for _ in range(n_samples):

        #sample values
        sample = random.sample(verb_list, sample_size)

        lemma_to_set = defaultdict(set)
        # add lemmas to set
        for lemma, orth, inflections, func_aux in sample:
            if mode == 'surface':
                lemma_to_set[lemma].add(orth)
            elif mode == 'inflection':
                for infl in func_aux:
                    lemma_to_set[lemma].add(infl)

        full_sample_set = set()
        for s in lemma_to_set.values():
            full_sample_set.update(s)
        sample_sets.append(full_sample_set)

        # Mean Within Subset Variety
    mean_subset_variety = mean(len(s) for s in sample_sets)

    # Mean Between Subset Variety
    bsv_values = []
    for a, b in combinations(sample_sets, 2):
        unique_diff = len(a.symmetric_difference(b))
        bsv_values.append(unique_diff)

    if bsv_values:
        between_subset_variety = mean(bsv_values)
    else:
        between_subset_variety = 0
    # final calculation
    mci = ((mean_subset_variety + (between_subset_variety/2))- 1)
    return round(mci,3)


# method to extract verbs and auxiliaries from the text
def get_verb_list(doc):
    verb_data = []
    for token in doc:
        if token.pos_ == 'VERB':
            lemma = token.lemma_
            orth = token.text
            inflections = token.morph.get("Inflection")

            # collect auxiliaries and their inflections
            func_aux = set()
            for child in token.children:
                if child.pos_ == 'AUX':
                    aux_lemma = child.lemma_
                    aux_infl = child.morph.get("Inflection")
                    func_aux.update(aux_infl)
                    func_aux.add(aux_lemma)

            # include the verb's inflection data as well
            func_aux.update(inflections)

            verb_data.append((lemma, orth, list(set(inflections)), list(func_aux)))
    print(verb_data)
    return verb_data

text = "昨日、友達と映画を見に行きました。映画はとても面白かったです。それから、カフェでコーヒーを飲みながら話しました。たくさん笑って、楽しい時間を過ごしました。"

doc = nlp(text)
print(MCI(doc, 5, 100, "inflection"))