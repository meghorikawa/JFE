#This is an implementation of counting the raw useage of vocab used in a text
# from each JLPT level
# This list was taken from the open source JISHO.org

from collections import Counter
import pandas as pd


file = '/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/WordLists/JLPT単語リスト-JISHO.csv'
df = pd.read_csv(file)

#convert to str type and remove any possible whitespace
df['Word']=df['Word'].astype(str).str.strip()
df['Reading']=df['Reading'].astype(str).str.strip()
df['JLPT']=df['JLPT'].astype(str).str.strip()


def JLPT_tango_counter(text):
    '''
    the method to count the number of vocab used at each level of JLPT
    :param text: the processed text from a learner
    :return: the counter object with counts at each level of JLPT
    '''

    #remove punctuation
    filtered_tokens = [token.lemma_ for token in text if not token.is_punct and not token.is_space]
    #go through list of tokens and look for match
    counter = Counter()

    JLPT_levels = ['N5', 'N4', 'N3', 'N2', 'N1']

    for lemma in filtered_tokens:
        # match by either "Word" or "Reading"
        match = df[(df['Word'] == lemma) | (df['Reading'] == lemma)]
        if not match.empty:
            jlpt_level = match.iloc[0]['JLPT'] # get level
            counter[jlpt_level] += 1 # increment
    #calculate percentages
    if len(filtered_tokens) == 0:
        percentages = {}
    else:
        percentages ={
            level: round(count.get(level,0)/len(filtered_tokens)*100,2)
            if len(filtered_tokens) > 0 else 0.0
            for level in JLPT_levels
        }
    return counter, percentages
