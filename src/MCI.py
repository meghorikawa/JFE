# This is a method to calculate the Morphological Complexity Index as described in
# Brezina and Pallotti 2019 "Morphological Complexity in written L2 texts"

import random
from collections import defaultdict
from statistics import mean

'''
1. Exract all unique verb lemma+form tokens
2. Randomly select K verbs without repetition from each subset (k=5 or k=10)
3. Repeat sampling process n times
4. Calculate mean MCI across the n samples'''


def MCI_10(text, sample_size, n_samples):
    '''

    :param text: the processed learner text
    :param sample_size: number of samples (i.e. 5, or 10)
    :param n_samples: number of times to sample
    :return:
    '''

    verb_list = get_verb_list(text)

    if sample_size > len(verb_list):
        return None  # there aren't enough verbs to sample from the text

    surface_mcis = []
    inflection_mcis = []

    # random sampling without repetition
    for _ in range(n_samples):
        sample = random.sample(verb_list, sample_size)

        lemma_to_forms = defaultdict(list)
        lemma_to_inflections = defaultdict(list)

        for lemma, surface, inflections in sample:
            lemma_to_forms[lemma].append(surface)
            for infl in inflections:
                lemma_to_inflections[lemma].append(infl)

        # incorporate the calculation
        surface_mci = sum(len(forms) for forms in lemma_to_forms.values()) / len(lemma_to_forms)
        inflection_mci = sum(len(infls) for infls in lemma_to_inflections.values()) / len(lemma_to_inflections)

        # store values to average later
        surface_mcis.append(surface_mci)
        inflection_mcis.append(inflection_mci)
    return round(mean(surface_mcis), 2), round(mean(inflection_mcis), 2)


# method to extract verbs from the text
def get_verb_list(doc):
    verb_data = []
    for token in doc:
        if token.pos_ == 'VERB':
            lemma = token.lemma_
            surface = token.text
            inflections = token.morph.get("Inflection")
            verb_data.append((lemma, surface, inflections))
    return verb_data
