# implementation of the MDD and MHD syntactic complexity mesures
# used in Komori et. al 2019
# measures average distance between different dependencies in a sentence, across text etc.

# method to compute depth of each token in a sentence
def compute_token_depth(sent):
    '''
    This method calculate the token depth of a sentence.
    :param sent: the sentence to calculate the depth of each token
    :return: a tuple of the token depth and the sentence length
    '''
    depths = {}
    for token in sent:
        depth = 0
        current = token # set current token
        while current.head != current:
            depth += 1
            current = current.head
        depths[token.i] = depth
    return depths

# MDD = (sum of head dist.) / (num. Tokens -1 )
# per komori 2019

# HD = sum(distance each token has to its root)
# MHD = HD / (V - 1)

def calculate_MDD_MHD(doc):
    '''
    This method calculate the MDD and MHD of a document.
    :param doc: the processed/tokenized text via spacy's ginza package
    :return: the calculated MDD and MHD
    '''

    total_mdd = 0 # counters to add each linear distance
    total_mhd = 0 # counter to add hierarchical distance
    num_dependencies = 0 # counter for number of tokens

    for sent in doc.sents:
        token_depths = compute_token_depth(sent)

        for token in sent:
            if token.dep_ != "ROOT":
                head_i = token.head.i
                dep_i= token.i

                # MDD - difference between head token and dependent (linear distance)
                total_mdd+= abs(head_i-dep_i)
                # MHD - difference in depth of head and dependent are from root
                total_mhd+= abs(token_depths[head_i]-token_depths[dep_i])

                num_dependencies += 1
    mdd = total_mdd/num_dependencies if num_dependencies > 0 else 0
    mhd = total_mhd/num_dependencies if num_dependencies > 0 else 0
    return mdd, mhd