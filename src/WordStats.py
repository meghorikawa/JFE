# clean this up so that the text processing is done in the main method
import math
from collections import Counter
import spacy
import clauseExtractor

# global list of coordinating conjunctions list
ccList = []
# global list of subordinating conjunctions
scList = []



def avgWPS(text):
    '''
    function to return the average words per sentence in a document
    :param text: the text to analyze
    :return: the average WPS
    '''
    sentences = list(text.sents)
    return sum(len(sent) for sent in sentences) / len(sentences)


# function to return the Corrected Type Token Ratio (number of unique words used per text)
# # of tokens over the squ. root of 2* # of words in text.
def cttr(text):
    '''
    function to return the Corrected Type Token Ratio (number of unique words used per text)
    # of tokens over the squ. root of 2* # of words in text.
    :param text: to analyze
    :return: the CTTR
    '''
    # get unique list of words using helper method
    return len(get_uniqueWords(text)) / (math.sqrt(2 * len(text)))



def scFreq(text):
    '''
    function to return a normalized count per 100 words of subordinating conjunctions
    :param text:
    :return: normalized count per 100 words of subordinating conjunctions
    '''
    sentences = list(text.sents)
    scCounter = 0
    wordCount = 0
    for sent in sentences:
        for token in sent:
            if token.pos_ == "SCONJ":
                scCounter += 1
                wordCount += 1
                scList.append(token)
            else:
                wordCount += 1

    return (scCounter / wordCount) * 100


def ccFreq(text):
    '''
    function to return a normalized count per 100 words of subordinating conjunctions
    :param text: the text to analyze
    :return: normalized count per 100 words of coordinating conjunctions
    '''
    sentences = list(text.sents)
    ccCounter = 0
    wordCount = 0
    for sent in sentences:
        for token in sent:
            if token.pos_ == "CCONJ":
                ccCounter += 1
                wordCount += 1
                ccList.append(token)
            else:
                wordCount += 1

    return (ccCounter / wordCount) * 100

def sc_per_sentence(text):
    '''
    function to return the number of subordinate clauses per sentence in a document
    :param text: the text to analyze
    :return: the ratio of subordinate clauses per sentence
    '''
    sentences = list(text.sents)
    sc_list = []
    for sent in sentences:
        clauses, sclauses, cclauses = clauseExtractor.extract_clauses(sent)
        sc_list.append(sclause for sclause in sclauses)
    return sum(sc_list) / len(sentences)
def sc_per_clause(text):
    '''
    function to return the ratio of subordinate clauses over all clauses in a text
    :param text: the text to analyze
    :return: the ration of subordinate clauses to clauses
    '''
    sentences = list(text.sents)
    sc_list = []
    clause_count = []
    for sent in sentences:
        clauses, sclauses, cclauses = clauseExtractor.extract_clauses(sent)
        sc_list.append(sclause for sclause in sclauses)
        clause_count.append(len(clauses))
    return sum(sc_list) / sum(clause_count)

def cc_per_sentence(text):
    '''
    function to return the ratio of coordinate clauses over all sentences in a text
    :param text: the text to analyze
    :return: the Coordination Ratio
    '''
    sentences = list(text.sents)
    cc_list = []
    for sent in sentences:
        clauses, sclauses, cclauses = clauseExtractor.extract_clauses(sent)
        cc_list.append(cclause for cclause in cclauses)
    return sum(cc_list) / len(sentences)

def cc_per_clause(text):
    '''
    function to return the ratio of coordinate clauses over all clauses in a text
    :param text: the text to analyze
    :return: the ratio of coordinate clauses to clauses
    '''
    sentences = list(text.sents)
    cc_list = []
    clause_count = []
    for sent in sentences:
        clauses, sclauses, cclauses = clauseExtractor.extract_clauses(sent)
        cc_list.append(cclause for cclause in cclauses)
        clause_count.append(len(clauses))
    return sum(cc_list) / sum(clause_count)

def sc_per_cc(text):
    def cc_per_clause(text):
        '''
        function to return the ratio of subordinate clauses over coordinate clauses in a text
        :param text: the text to analyze
        :return: the ratio of subordinate clauses to coordinate clauses
        '''
        sentences = list(text.sents)
        cc_list = []
        sc_list = []
        for sent in sentences:
            clauses, sclauses, cclauses = clauseExtractor.extract_clauses(sent)
            cc_list.append(cclause for cclause in cclauses)
            sc_list.append(ssclause for ssclause in sclauses)
        return len(sc_list) / len(cc_list)

def get_noun_density(text):
    '''
    function to return the ratio of nouns to the overall token count
    :param text: the text to analyze
    :return: the ratio of nouns to the overall token count
    '''
    # remove punctuation
    filtered_tokens = [token for token in text if not token.is_punct]

    #proportion of Nouns vs. tokens
    total_nouns = sum(1 for token in filtered_tokens if token.pos_ in {"NOUN", "PROPN", "PRON"})
    total_tokens = len(text)

    return total_nouns / total_tokens

def get_verb_density(text):
    '''
    function to return the ratio of verbs to the overall token count
    :param text: the text to analyze
    :return: the ratio of verbs to the overall token count
    '''
    # remove punctuation
    filtered_tokens = [token for token in text if not token.is_punct]

    # proportion of Nouns vs. tokens
    total_nouns = sum(1 for token in filtered_tokens if token.pos_ in {"VERB", "AUX"})
    total_tokens = len(text)

    return total_nouns / total_tokens

def get_adj_density(text):
    '''
    function to return the ratio of adjectives to the overall token count
    :param text: the text to analyze
    :return: the ratio of adjectives to the overall token count
    '''
    # remove punctuation
    filtered_tokens = [token for token in text if not token.is_punct]

    # proportion of Nouns vs. tokens
    total_nouns = sum(1 for token in filtered_tokens if token.pos_ =="ADJ")
    total_tokens = len(text)

    return total_nouns / total_tokens
def get_adv_density(text):
    '''
    function to return the ratio of adverbs to the overall token count
    :param text: the text to analyze
    :return: the ratio of adverbs to the overall token count
    '''
    # remove punctuation
    filtered_tokens = [token for token in text if not token.is_punct]

    # proportion of Nouns vs. tokens
    total_nouns = sum(1 for token in filtered_tokens if token.pos_ =="ADV")
    total_tokens = len(text)

    return total_nouns / total_tokens

def avg_NP_length(text):
    '''
    function to return the average length of NP in a text
    :param text: the text to analyze
    :return: the average length of NP
    '''
    NP_list = clauseExtractor.extract_NPs(text)
    return sum(len(NP)for NP in NP_list) / len(NP_list)
def avg_VP_length(text):
    '''
    function to return the average length of VP in a text
    :param text: the text to analyze
    :return: the average length of VP
    '''
    VP_list = clauseExtractor.extract_VPs(text)
    return sum(len(VP) for VP in VP_list) / len(VP_list)
def clause_len(text):
    '''
    function to return the average count of words per clause
    :param text: the text to analyze
    :return: the average count of words per clause
    '''
    sentences = list(text.sents)
    # instantiate a list to track each clauses' length
    wpc_count = []

    # first iterate through list of sentences
    for sent in sentences:
        clauses, sclauses, cclauses = clauseExtractor.extract_clauses(sent)
        # update value of wpc_count
        wpc_count.extend(len(clause) for clause in clauses)
    # return the average of words per clause
    return sum(wpc_count) / len(wpc_count)


def clauses_per_sentence(text):
    '''
    function to return the average count of clauses per sentence
    :param text: the text to analyze
    :return: the average count of clauses per sentence
    '''
    sentences = list(text.sents)
    clauseCountList = []
    clauseCountList.append(clauseExtractor.clause_count(sent) for sent in sentences)
    return sum(clauseCountList) / len(sentences)

def get_docLen(text):
    '''
    function to return the raw document length
    :param text: the text to analyze
    :return: the raw document length
    '''
    return len(text)


def get_uniqueWords(text):
    '''
    function to return the unique words in a text
    :param text: the text to analyze
    :return: the number of unique words in a text
    '''
    seen = set()
    uniqueWord = []
    for token in text:
        if token.orth not in seen:
            uniqueWord.append(token)
        seen.add(token.orth)
    return uniqueWord


# method to write outputs to SC lists
def write_SClist():
    file = open('SClist.txt', 'a')
    # iterate through the SC list and write to file
    for item in scList:
        file.write(f'{item}\n')
    file.close()
# method to write outputs to CC lists
def write_CClist():
    file = open('CClist.txt', 'a')
    # iterate through the CC list and write to file
    for item in ccList:
        file.write(f'{item}\n')
    file.close()