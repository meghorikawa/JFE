# this is an implementation of the lexical frequency profile as described in Laufer1995}
# this uses a word list from the BCCWJ corpus
import pandas as pd

# remove items with a frequency under this number
min_freq = 50
file = 'WordLists/BCCWJ_frequencylist_luw_ver1_0.tsv'
df = pd.read_csv(file, sep='\t')

def make_bands(df, band_size):
    # make sure the df is ordered by frequency (highest numebr first)
    df = df.sort_values(by=['frequency'], ascending=False, inplace=True)

    # remove low frequency items
    df = df[df['frequency'] >= min_freq].reset_index(drop=True)

    # make bands
    bands = {}
    for i in range(0, len(df), band_size):
        band_label = f"{(i // band_size + 1)}k"
        band_lemmas = set(df['lemma'].iloc[i:i + band_size])
        bands[band_label] = band_lemmas
    return bands


# 1. load band list

# 2. classify lemmas into bands

# 3. Analyze the lists for score

# return percent per band,

