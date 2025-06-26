# this is an implementation of the lexical frequency profile as described in Laufer1995}
# this uses a word list from the BCCWJ corpus
from collections import Counter
import pandas as pd
import spacy

nlp = spacy.load('ja_ginza')

# remove items with a frequency under this number
min_freq = 100
max_bands = 10
band_size = 1000
file = '/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/WordLists/BCCWJ_frequencylist_luw_ver1_0.tsv'
df = pd.read_csv(file, sep='\t')

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
        band_lemmas = set()
        for lemma in df['lemma'].iloc[i:i + band_size]:
            doc = nlp(lemma)
            tokenized = tuple(tok.lemma_ for tok in doc if not tok.is_punct and not tok.is_space)
            band_lemmas.add(tokenized)
        bands[band_label] = band_lemmas
    return bands

# 1. load band list
bands = make_bands(df, band_size)
# helper method to classify a lemma to a band
def classify_token(lemma_seq, bands):
    for band, lemma_set in bands.items():
        if lemma_seq in lemma_set:
            return band
    return "OOV" # if token not found add it to off list

def LFP(text):
    '''
    :param text: the tokenized learner text to analyze
    :return: dictionary of the lfp percentages by band
    '''
    oov_list = []

    band_counts = Counter()

    # 2. remove punctuation
    lemmas = [token.lemma_ for token in text if not token.is_punct and not token.is_space]

    # 3. classify lemmas into bands
    all_band_lemmas = set()
    for band_lemma_set in bands.values():
        all_band_lemmas.update(band_lemma_set)
    max_len = max(len(seq) for seq in all_band_lemmas)

    i = 0
    while i< len(lemmas):
        matched = False
        for n in range(max_len, 0, -1): # try the longest match first
            if i + n <= len(lemmas):
                seq = tuple(lemmas[i:i+n])
                band = classify_token(seq, bands)
                if band != "OOV":
                    band_counts[band] += 1
                    i += n
                    matched = True
                    break
        if not matched:
            oov_list.append(lemmas[i])
            band_counts["OOV"] += 1
            i += 1


    # 4. Analyze the lists for score
    total_tokens = sum(band_counts.values())
    band_percentages = {band: round(count / total_tokens * 100, 2) for band, count in band_counts.items()}
    return band_percentages, band_counts, total_tokens, oov_list

'''
for testing purposes
nlp = spacy.load('ja_ginza')
doc = nlp(
    "私はドラえもん好きなのだ。")

percent, count, tokens, oovs = LFP(doc)
print(f"Percentage {percent}, Total Count: {count}, Total tokens:{tokens}, OOV: {oovs}")
'''