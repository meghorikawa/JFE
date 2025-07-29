# this is a Japanese adaption of the Korean Morphological Richness Analyzer (KMRA)
# system Hwang2024

import MTLD

MATTR_window = 50 # default window size for MATTR

def sort_morphemes(doc):
    '''
    A method to sort morphemes into the three lists for further analysis
    :param doc: the processed document to analyze
    :return: the sorted lists of morphemes: all, content, and function
    '''

    # initialize the lists:
    all_morphemes = []
    content_morphemes = []
    function_morphemes = []

    for token in doc:
        pos = token.tag_ # use tag instead of pos to get more detailed information
        lemma = token.lemma_

        #add morpheme to all list
        all_morphemes.append(token)

        # sort by function and content morphemes
        if pos.startswith('名詞') or pos.startswith("動詞") or pos.startswith("形容詞") or pos.startswith("副詞"):
            # content morphemes have a label of Noun, Verb, Adjective, Adverb
            content_morphemes.append(token)
        elif pos.startswith("助詞") or pos.startswith("助動詞") or pos.startswith("接続詞"):
            # particles, auxiliaries, and conjunctions
            function_morphemes.append(token)

    return all_morphemes, content_morphemes, function_morphemes

def MATTR (morpheme_list):
    '''

    :param morpheme_list: a processed list of morphemes including tags
    :return: the MATTR score
    '''
    if len(morpheme_list) == 0:
        return 0.0  # no morphemes in list

    if len(morpheme_list) < MATTR_window:
        return len(set(morpheme_list))/len(morpheme_list)

    ttrs=[]
    for i in range(len(morpheme_list)-MATTR_window+1):
        window=morpheme_list[i:i+MATTR_window]
        ttr = len(set(window))/ MATTR_window
        ttrs.append(ttr)

    return sum(ttrs)/len(ttrs)

# implement a measure to look at elaboration of morphology by looking at
# the auxiliaries attached to verbs
def calculate_auxiliary_chain_density(doc):
    '''
    :param doc: the processed document to analyze
    :param doc:
    :return: A measure of density of auxilary chains
    '''
    total_verbs = 0
    total_auxiliaries = 0
    for token in doc:
        if token.pos_ =="VERB" and token.head == token:
            total_verbs += 1

            # find auxilaries
            for child in token.children:
                if child.pos_=="AUX" or "非自立" in child.tag_:
                    total_auxiliaries += 1
                elif child.orth_ in ["て","で"] and child.tag_.startswith("助詞"):
                    total_auxiliaries +=1

    if total_verbs ==0:
        return 0.0

    return total_auxiliaries / total_verbs

def calculate_JRMA_scores (doc):
    '''

    :param doc: a processed document to analyze
    :return: 6 lists of calculated MATTR and MTLD scores
    '''
    # first split into lists
    all_morphemes, content_morphemes, function_morphemes = sort_morphemes(doc)
    # calculate MTLD for each list

    all_MTLD_score = MTLD.mtld(all_morphemes, 'lemma')
    content_MTLD_score = MTLD.mtld(content_morphemes, 'lemma')
    function_MTLD_score = MTLD.mtld(function_morphemes, 'lemma')

    #calculate MATTR
    all_MATTR = MATTR([m.lemma_ for m in all_morphemes])
    content_MATTR = MATTR([m.lemma_ for m in content_morphemes])
    function_MATTR = MATTR([m.lemma_ for m in function_morphemes])

    # calculate elaboration via auxilary chains
    aux_chains_density = calculate_auxiliary_chain_density(doc)
    return all_MTLD_score, content_MTLD_score, function_MTLD_score, all_MATTR, content_MATTR, function_MATTR, aux_chains_density