# this is a Japanese adaption of the Korean Morpheme-based Richness Analysis (KMRA)
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

    if len(morpheme_list) < MATTR_window:
        return len(set(morpheme_list))/len(morpheme_list)

    ttrs=[]
    for i in range(len(morpheme_list)-MATTR_window+1):
        window=morpheme_list[i:i+MATTR_window]
        ttr = len(set(window))/ MATTR_window
        ttrs.append(ttr)

    return sum(ttrs)/len(ttrs)

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
    all_MATTR = MATTR(all_MTLD_score)
    content_MATTR = MATTR(content_MTLD_score)
    function_MATTR = MATTR(function_MTLD_score)

    return all_MTLD_score, content_MTLD_score, function_MTLD_score, all_MATTR, content_MATTR, function_MATTR