# the main function which will build and return a nested list of clauses within a sentence
def extract_clauses(sent):
    '''

    :param adoc: a processed sentence
    :return: clauses: a list of clauses, subordinate_clauses: a list of subordinate clauses, coordinate_clauses: a list of coordinate_clauses
    '''
    root = None
    rootClause = []
    clauses = []
    clauseHeadList = []
    coordinate_clauses = []
    subordinate_clauses = []


    for aToken in sent:
        if aToken.dep_ == "ROOT":
            root = aToken
            rootClause.append(root)
            break

    # helper function that traverses tree branches recursively
    def traverse_tree(node):
        tokens = [node]
        for child in node.children:
            if child.dep_ in ["advcl", "ccomp", "acl", "xcomp", "relcl", "conj"]:
                clauseHeadList.append(child)
            else:
                tokens.extend(traverse_tree(child))
        return tokens

    # a helper function that will take in a head node and build a list containing the clause tokens.
    def clause_builder(aNode):
        aClause = [aNode]
        for child in aNode.children:
            aClause.extend(traverse_tree(child))
        return aClause

    for child in root.children:
        # if token in child node tagged as a clause head save in separate list to access later
        if child.dep_ in ["advcl", "ccomp", "acl", "xcomp", "relcl", "conj"]:
            clauseHeadList.append(child)
        # add the other nodes to the root clause
        else:
            rootClause.extend(traverse_tree(child))
    clauses.append(rootClause)

    # after building root clause iterate through the clause head list to also build those clauses
    for token in clauseHeadList:
        built_clause = clause_builder(token)
        clauses.append(built_clause)
        if token.dep_ in ["advcl", "ccomp", "acl", "xcomp", "relcl"]:
            subordinate_clauses.append(built_clause)
        elif token.dep_ == "conj":
            coordinate_clauses.append(built_clause)

    return clauses, subordinate_clauses, coordinate_clauses

# Extract Noun phrases from a clause returns list of noun phrases
def extract_NPs(text):
    '''
    function to extract NPs from a text
    :param text: the text to analyze
    :return: a list of NPs in the text
    '''
    clause_list = extract_clauses(text)
    NP_list = []
    for clause in clause_list:
        for token in clause:
            if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                np = [token]
                for child in token.children:
                    if child.dep_ in ["amod", "det", "nmod", "compound", "case"]:
                        np.append(child)
                np = sorted(np, key=lambda x: x.i) # keep original order of tokens
                NP_list.append("".join([t.text for t in np]))
    return NP_list

# extract verb phrases
def extract_VPs(text):
    '''
    function to extract VPs from a text
    :param text: the text to analyze
    :return: list of VPs in the text
    '''
    clause_list = extract_clauses(text)
    VP_list = []
    for clause in clause_list:
        for token in clause:
            if token.pos_ in ["VERB", "AUX"]:
                vp = [token]
                for child in token.children:
                    if child.dep_ in ["aux", "advmod", "mark", "compound"]:
                        vp.append(child)
                vp = sorted(vp, key=lambda x: x.i)
                VP_list.append("".join([vp.pop()]))
    return VP_list


def clause_count(sent):
    '''
    :param sent: a sentence
    :return: number of clauses in the sentence
    '''
    clauses, sclauses, cclauses =extract_clauses(sent)
    return len(clauses)

def words_per_clause(sent):
    '''
    :param sent: a sentence
    :return: average number of words per clause in the sentence
    '''
    clauses, sclauses, cclauses =extract_clauses(sent)
    return sum(len(clause)for clause in clauses)/len(clauses)