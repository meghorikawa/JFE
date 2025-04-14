import spacy
import ja_ginza

nlp = spacy.load('ja_ginza')
# the root verb of the sentence
root = None
# the root clause of the sentence
rootClause = []
# the sentence being analyzed
doc = None
# the list of all clauses found in the document
clauses = []
# global list of clause heads
clauseHeadList = []
# global list of NP
NP_list = []
# global list of VP
VP_list = []

# the main function which will build and return a nested list of clauses within a sentence
def extract_clauses(adoc):
    global root
    global rootClause

    find_root(adoc)

    for child in root.children:
        # if token in child node tagged as a clause head save in separate list to access later
        if child.dep_ in ["advcl", "ccomp"]:
            clauseHeadList.append(child)
        # add the other nodes to the root clause
        else:
            rootClause.extend(traverse_tree(child))
    clauses.append(rootClause)

    # after building root clause iterate through the clause head list to also build those clauses
    for token in clauseHeadList:
        clauses.append(clause_builder(token))

    return clauses

# Extract Noun phrases from a clause returns list of noun phrases
def extract_NPs(clause_list):
    for token in clause_list:
        if token.pos_ in ["NOUN", "PROPN", "PRON"]:
            np = [token]
            for child in token.children:
                if child.dep_ in ["amod", "det", "nmod", "compound", "case"]:
                    np.append(child)
            np = sorted(np, key=lambda x: x.i) # keep original order of tokens
            NP_list.append("".join([t.text for t in np]))
    return NP_list

# extract verb phrases
def extract_VPs(clause_list):
    for token in clause_list:
        if token.pos_ in ["VERB", "AUX"]:
            vp = [token]
            for child in token.children:
                if child.dep_ in ["aux", "advmod", "mark", "compound"]:
                    vp.append(child)
            vp = sorted(vp, key=lambda x: x.i)
            VP_list.append("".join([vp.pop()]))
    return VP_list

# helper function that traverses tree branches recursively
def traverse_tree(node):
    tokens = [node]
    for child in node.children:
        if child.dep_ in ["advcl", "ccomp"]:
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


# function to traverse tree and find root
def find_root(aSent):
    global root
    for aToken in aSent:
        if aToken.dep_ == "ROOT":
            root = aToken
            rootClause.append(root)
            break


# function which will return the number of clauses per sentence
def clause_count():
    return len(clauses)


# function which will return the average number of "words" per clause
def wordsp_clause():
    sum = 0
    for clause in clauses:
        sum = sum + len(clause)
    return sum / len(clauses)


# function that returns the list of clauses
def get_clause():
    return clauses


# clear everything for the next sentence to be processed
def clear():
    global root
    global rootClause
    global doc
    global clauses
    global clauseHeadList
    root = None
    # the root clause of the sentence
    rootClause = []
    # the sentence being analyzed
    doc = None
    # the list of all clauses found in the document
    clauses = []
    # global list of clause heads
    clauseHeadList = []
    # reset NP
    NP_list = []
    # reset VP
    VP_list = []
