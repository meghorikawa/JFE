from os import listdir
from os.path import isdir, join

import spacy
from rules import rule_modules  # Dynamically import all rule files
import MCI
import MDD_MHD
import MTLD
import LexFreqPro
import pipeline
import pandas as pd
import TextAnalysis
import WordStats
import JRMA
import JLPTWordList
import mojimoji

#load spacy model
nlp = spacy.load('ja_ginza')

# main method I need to create separate line items for each participant and each writing.
path= "/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/Corpus"
# load participant data
participant_data = pd.read_csv("/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/participant_data.csv")
# make a list of each directory () in corpus
participant_list = [
    p for p in listdir(path)
    if isdir(join(path, p)) and not p.startswith(".")
]

# List of text objects
all_text_data = []

for participant in participant_list:
    # get a list of their texts written
    text_list = listdir(path+"/"+participant)

    #pull metadata on participant
    meta_data = participant_data[participant_data["協力者"] == participant]
    gender = meta_data["性別"].values[0]
    age = meta_data["年齢"].values[0]
    loc = meta_data["調査地"].values[0]
    score = meta_data["J-CAT (合計)"].values[0]
    lang = meta_data["母語"].values[0]
    jlpt = meta_data["JLPT"].values[0]

    # go through each text in the list
    for text in text_list:
        print(f"loaded : {text}")
        # remove file extension and participant name to get text name
        text_name1 = text.replace(".txt","")
        text_name = text_name1.replace(f"{participant}_","")
        # open and load text
        with open(f"{path}/{participant}/{text}","r",encoding="utf-8") as f:
            raw_text = f.read()
        # convert any half-width characters to full width for easier processing
        raw_text=mojimoji.han_to_zen(raw_text)

        #process it
        doc = nlp(raw_text)
        # make new text_analysis object
        text_obj = TextAnalysis.Text_analysis(participant,text_name, gender, age, loc, score, lang,jlpt)
        # pull stats and set them to text analysis object

        # next get count of grammar forms used
        text_obj.count_grammar_forms(doc)

        text_obj.text_len = WordStats.get_docLen(doc) # to find avg length of text per JLPT lvl
        # Syntactic Measures
        text_obj.WPSavg = WordStats.avgWPS(doc)
        text_obj.clauseLen=WordStats.clause_len(doc)
        text_obj.clauseCount = WordStats.clauses_per_sentence(doc)
        text_obj.NPlen = WordStats.avg_NP_length(doc)
        text_obj.VPlen = WordStats.avg_VP_length(doc)
        text_obj.sc_per_sent= WordStats.sc_per_sentence(doc)
        text_obj.sc_per_clause = WordStats.sc_per_clause(doc)
        text_obj.cc_per_sent = WordStats.cc_per_sentence(doc)
        text_obj.cc_per_clause = WordStats.cc_per_clause(doc)
        text_obj.sc_per_cc = WordStats.sc_per_cc(doc)
        text_obj.CCfreq = WordStats.ccFreq(doc)
        text_obj.SCfreq = WordStats.scFreq(doc)
        text_obj.MDD, text_obj.MHD = MDD_MHD.calculate_MDD_MHD(doc)
        # lexical Density
        text_obj.noun_density = WordStats.get_noun_density(doc)
        text_obj.verb_density = WordStats.get_verb_density(doc)
        text_obj.adjective_density = WordStats.get_adv_density(doc)
        text_obj.adverb_density = WordStats.get_adv_density(doc)

        # lexical freq profile
        band_percentages, band_counts, total_tokens, oov_list = LexFreqPro.LFP(doc)
        text_obj.LFP_band_percentages = band_percentages
        text_obj.LFP_band_counts = band_counts
        text_obj.LFP_total_tokens = total_tokens
        text_obj.LFP_oov_list = oov_list

        #JLPT Vocab Useage
        jlpt_counts, jlpt_percents = JLPTWordList.JLPT_tango_counter(doc)
        text_obj.JLPT_Tango_N1 = jlpt_counts.get('N1')
        text_obj.JLPT_Tango_N2 = jlpt_counts.get('N2')
        text_obj.JLPT_Tango_N3 = jlpt_counts.get('N3')
        text_obj.JLPT_Tango_N4 = jlpt_counts.get('N4')
        text_obj.JLPT_Tango_N5 = jlpt_counts.get('N5')

        text_obj.JLPT_Tango_N5

        # MTLD
        text_obj.MTLD_surface = MTLD.mtld(doc, 'surface')
        text_obj.MTLD_lemma = MTLD.mtld(doc, 'lemma')
        #CTTR
        text_obj.CTTR = WordStats.cttr(doc)

        # morphological Complexity index
        text_obj.mci_5_surface = MCI.MCI(doc, 5, 100, 'surface')
        #print(f"MCI5-Surface = {text_obj.mci_5_surface}")
        text_obj.mci_10_surface = MCI.MCI(doc, 10, 100, 'surface')
        #print(f"MCI10-Surface = {text_obj.mci_10_surface}")
        text_obj.mci_5_inflection = MCI.MCI(doc, 5, 100, 'inflection')
        #print(f"MCI5-inflection = {text_obj.mci_5_inflection}")
        text_obj.mci_10_inflection = MCI.MCI(doc, 10, 100, 'inflection')
        #print(f"MCI10-inflection = {text_obj.mci_10_inflection}")

        (text_obj.JRMA_all_MTLD, text_obj.JRMA_content_MTLD, text_obj.JRMA_function_MTLD, text_obj.JRMA_all_MATTR,
         text_obj.JRMA_content_MATTR, text_obj.JRMA_function_MATTR, text_obj.JRMA_aux_chains) = JRMA.calculate_JRMA_scores(doc)


        # add the text analysis object to text lists
        all_text_data.append(text_obj.to_dict()) # convert to dictionary and add to text list
        print(f"finished with {text}")


df = pd.DataFrame(all_text_data)
df.to_csv('learner_data1.csv', index=False)
