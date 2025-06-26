'''
This contains functions to extract noun and verb phrases from a learner sentence
'''

def extract_noun_phrases(doc):
    '''

    :param doc: the full text of a learner written text
    :return: a list of noun phrases extracted from the text
    '''
    NP_list = []
    seen = set()

    for sentence in doc.sents:
        for token in sentence:
            if token.pos_ in ['NOUN', 'PROPN', 'PRON']:
                np = [token]
                for child in token.children:
                    if child.dep_ in ["amod", "compound", "nmod", "case", "det", "nummod"]:
                        np.append(child)
                    # sort by word order
                np=sorted(np, key=lambda x: x.i)
                np_text = tuple(tok.i for tok in np)
                if np_text not in seen:
                    seen.add(np_text)
                    NP_list.append(np)
    return NP_list

def extract_verb_phrases(doc):
    '''

    :param doc: the full text of a learner written text
    :return: a list of VP phrases extracted from the text
    '''
    VP_list =[]
    seen = set()
    for sentence in doc.sents:
        for token in sentence:
            if token.pos_ in ['VERB', 'AUX'] and token.dep_ in ['ROOT', 'CONJ', 'xcomp', 'advcl']:
                # make a new vp
                vp = [token]
                # find children
                for child in token.children:
                    if child.dep_ not in ['nsubj', 'nsubjpass', 'csubj', 'punct', 'mark','obl']:
                        vp.append(child)
                # check is ancestor also includes auxilary
                for ancestor in token.ancestors:
                    if ancestor.pos_ == "AUX" and ancestor.head == token:
                        vp.append(ancestor)
                #sort order
                vp= sorted(set(vp), key=lambda x: x.i)
                if vp:
                    vp_indices = tuple (tok.i for tok in vp)
                    if vp_indices not in seen:
                        seen.add(vp_indices)
                        VP_list.append(vp)
    return VP_list