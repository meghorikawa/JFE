# this is an implementation of the lexical frequency profile as described in Laufer1995}
# this uses a word list from the BCCWJ corpus
from collections import Counter
import pandas as pd
import spacy


# remove items with a frequency under this number
min_freq = 100
max_bands = 10
band_size = 1000
file = '/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/WordLists/BCCWJ_frequencylist_luw_ver1_0.tsv'
df = pd.read_csv(file, sep='\t')

# out of vocab list for tracking
oov_list = []

def make_bands(df, band_size):
    # make sure the df is ordered by frequency (highest numebr first)
    df = df.sort_values(by=['frequency'], ascending=False)

    # remove low frequency items
    df = df[df['frequency'] >= min_freq].reset_index(drop=True)

    # keep only necessary columns
    keep_cols = ['rank', 'lForm', 'lemma', 'pos', 'frequency']
    df = df[[col for col in keep_cols if col in df.columns]]

    # trim to max_bands
    max_size = max_bands * band_size
    df = df.iloc[:max_size]


    # make bands
    bands = {}
    for i in range(0, len(df), band_size):
        band_label = f"{(i // band_size + 1)}k"
        band_lemmas = set(df['lemma'].iloc[i:i + band_size])
        bands[band_label] = band_lemmas
    return bands

# helper method to classify a lemma to a band
def classify_token(lemma, band):
    for band, words in band.items():
        if lemma in words:
            return band
    return "OOV" # if token not found add it to off list

def LFP(text):
    '''
    :param text: the tokenized learner text to analyze
    :return: dictionary of the lfp percentages by band
    '''
    band_counts = Counter()

    # 1. load band list
    bands = make_bands(df, band_size)

    # 2. remove punctuation
    filtered_tokens = [token.lemma_ for token in text if not token.is_punct and not token.is_space]

    # 3. classify lemmas into bands
    for lemma in filtered_tokens:
        band = classify_token(lemma, bands)
        if band == "OOV":
            oov_list.append(lemma)
        band_counts[band] = band_counts[band] + 1
    # 4. Analyze the lists for score
    total_tokens = sum(band_counts.values())
    band_percentages = {band: round(count / total_tokens * 100, 2) for band, count in band_counts.items()}
    return band_percentages, band_counts, total_tokens, oov_list

'''
nlp = spacy.load('ja_ginza')
doc = nlp("昨日、私は友だちと新しいカフェに行きました。お店は駅の近くにあり、とても静かで落ち着いた雰囲気でした。私たちはコーヒーとケーキを注文して、ゆっくり話をしました。ケーキは甘すぎず、美味しかったです。今度は別の友だちも連れて行きたいと思います。")

percent, count, tokens, oovs = LFP(doc)
print(f"Percentage {percent}, Total Count: {count}, Total tokens:{tokens}, OOV: {oovs}")
'''