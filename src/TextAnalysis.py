'''
a class to handle the texts, it should log the different measures,
and the metadata of the participant
'''
import spacy


class Text_analysis:

    def __init__(self, participant, text_name, gender,age,loc, score, lang, JLPT):
        # participant number
        self.participant = participant
        self.age = age
        self.loc = loc
        self.gender = gender
        # native language
        self.lang = lang
        # text name
        self.text_name = text_name
        # J-cat score
        self.score = score
        # JLPT level
        self.JLPT = JLPT
        self.nlp = spacy.load('ja_ginza')

        # complexity measures and frequency data

        # text length
        self.text_len = 0
        # Average sent length (words per sentence)
        self.WPSavg = 0
        # Average NP length
        self.NPlen=0
        # Average VP length
        self.VPlen=0
        # Subordination Ratio (Subordinate Clauses per Sentence)
        self.sc_per_sent=0
        # Subordination Ratio (Subordinate Clauses per total Clauses)
        self.sc_per_clause = 0
        # Coordination ratio (Coordinate Clauses per Sentence)
        self.cc_per_sent=0
        # Coordination ratio (Coordinate Clauses per total Clauses)
        self.cc_per_clause=0
        # Ration of Subordinate Clauses to Coordinate Clauses
        self.sc_per_cc = 0
        # Frequency of Coordinating Conjunctions per 100 words
        self.CCfreq = 0
        # Frequency of subordinating conjunctions per 100 words
        self.SCfreq = 0
        # Avg clause length
        self.clauseLen = 0
        # Avg clause count per sent
        self.clauseCount = 0
        #MDD
        self.MDD = 0
        #MDH
        self.MHD = 0

        # Lexical Measures
        self.CTTR = 0
        self.MTLD_surface = 0
        self.MTLD_lemma = 0

        # Lexical Density
        self.noun_density = 0
        self.verb_density = 0
        self.adjective_density = 0
        self.adverb_density = 0

        #lexical Sophistication
        self.LFP_band_percentages = {}
        self.LFP_band_counts = {}
        self.LFP_total_tokens=0
        self.LFP_oov_list=[]


        # Morphological Complexity
        self.mci_5_surface = 0
        self.mci_10_surface = 0
        self.mci_5_inflection = 0
        self.mci_10_inflection = 0
        self.JRMA_all_MTLD = 0
        self.JRMA_content_MTLD = 0
        self.JRMA_function_MTLD = 0
        self.JRMA_all_MATTR = 0
        self.JRMA_content_MATTR = 0
        self.JRMA_function_MATTR = 0
        self.JRMA_aux_chains = 0
        # Criterial Features raw counts of grammar forms
        self.pattern_matches = {} # refine this later to have a flat list for each feature

        #JLPT Vocab Count
        self.JLPT_Tango_N1 =0
        self.JLPT_Tango_N2 =0
        self.JLPT_Tango_N3 =0
        self.JLPT_Tango_N4 =0
        self.JLPT_Tango_N5 =0
    # A to_dict method to easily convert to df later
    def to_dict(self):
        # Start with metadata and basic stats
        data = {
            "participant": self.participant,
            "text_name": self.text_name,
            "gender": self.gender,
            "age": self.age,
            "loc": self.loc,
            "JCATscore": self.score,
            "lang": self.lang,
            "JLPT": self.JLPT,
            "Text Length": self.text_len,
            "Avg Sent Length": self.WPSavg,
            "Avg NP length": self.NPlen,
            "Avg VP length": self.VPlen,
            "Subordinate Clauses per sentence": self.sc_per_sent,
            "Subordinate Clauses per clause": self.sc_per_clause,
            "Coordinate Clauses per sentence": self.cc_per_sent,
            "Coordinate Clauses per clause": self.cc_per_clause,
            "Subordinate Clauses per Coordinate Clauses": self.sc_per_cc,
            "CCfreq": self.CCfreq,
            "SCfreq": self.SCfreq,
            "Avg Clause Length": self.clauseLen,
            "Avg Clause per Sent": self.clauseCount,
            "MDD": self.MDD,
            "MHD": self.MHD,
            "CTTR": self.CTTR,
            "MTLD_surface": self.MTLD_surface,
            "MTLD_lemma": self.MTLD_lemma,
            "noun_density": self.noun_density,
            "verb_density": self.verb_density,
            "adjective_density": self.adjective_density,
            "adverb_density": self.adverb_density,
            "mci_5_surface": self.mci_5_surface,
            "mci_10_surface": self.mci_10_surface,
            "mci_5_inflection": self.mci_5_inflection,
            "mci_10_inflection": self.mci_10_inflection,
            "JRMA_all_MTLD": self.JRMA_all_MTLD,
            "JRMA_content_MTLD": self.JRMA_content_MTLD,
            "JRMA_function_MTLD": self.JRMA_function_MTLD,
            "JRMA_all_MATTR": self.JRMA_all_MATTR,
            "JRMA_content_MATTR": self.JRMA_content_MATTR,
            "JRMA_function_MATTR": self.JRMA_function_MATTR,
            "JRMA_aux_chains": self.JRMA_aux_chains,
            "LFP_total_tokens": self.LFP_total_tokens,
            #"LFP_OOV_List": ", ".join(self.LFP_oov_list)  # Convert list to string

            "JLPT Vocab N1": self.JLPT_Tango_N1,
            "JLPT Vocab N2": self.JLPT_Tango_N2,
            "JLPT Vocab N3": self.JLPT_Tango_N3,
            "JLPT Vocab N4": self.JLPT_Tango_N4,
            "JLPT Vocab N5": self.JLPT_Tango_N5,

    }

        # Add LFP band percentages
        for band, value in self.LFP_band_percentages.items():
            data[f"LFP_{band}_percent"] = value

        # Add LFP band counts
        for band, value in self.LFP_band_counts.items():
            data[f"LFP_{band}_count"] = value

        # Add grammar form pattern match data
        for match_key, match_val in self.pattern_matches.items():
            data[match_key] = match_val

        return data

# set attribute method to set value without manually defining a set method for each attribute
    def __setattr__(self, key, value):
        if key in ["participant", "name", "gender", "age", "loc", "score", "lang", "JLPT"]:
            # Check if the key is already initialized (set in the constructor)
            if key in self.__dict__:
                raise AttributeError(f"Cannot modify attribute {key} once object is initialized.")
        # Allow other attributes to be set freely
        super().__setattr__(key, value)

    # add method to set the raw count of grammar form useage
    def count_grammar_forms(self, doc):
        '''

        :param doc: the document to return raw counts for JLPT Grammar Forms
        :return:
        '''

        from rules import rule_modules
        # list to keep track of match counts
        matches={}

        for module_name, module in rule_modules.items():
            for attr in dir(module):
                if attr.startswith("match_"):
                    match_function = getattr(module, attr)
                    if callable(match_function):
                        result = match_function(self.nlp,doc)

                        # handle output as dict
                        if isinstance(result, dict):
                            matches[attr] = result
                        elif isinstance(result, tuple) and isinstance(result[0], dict):
                            form_dict,count = result
                            matches[attr] = form_dict
                        else:
                            matches[attr] = 0
        self.pattern_matches = matches