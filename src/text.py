''' a class to handle the texts, it should log to different measures, and the stats of the participant
native language - taken from participant list
proficency level - taken from participant meta data list



'''

class text:

    def __init__(self, name, score, lang):
        # text name
        self.name = name
        # proficiency level
        self.score = score
        # native language
        self.lang = lang

        # complexity measures and frequency data

        # Average sent length (words per sentence)
        self.WPSavg = 0
        # Corrected type token ratio
        self.CTTR = 0
        # Frequency of Coordinating Conjunctions per 100 words
        self.CCfreq = 0
        # Frequency of subordinating conjunctions per 100 words
        self.SCfreq = 0
        # Avg clause length
        self.clauseLen = 0
        # Avg clause count per sent
        self.clauseCount = 0

    # The to string method
    def __str__(self):
        return (f'Text type: {self.name} Native Language: {self.lang} J-Cat Score: {self.score} Words per Sent:'
                f' {self.WPSavg} '
                f'CTTR:'
                f' {self.CTTR}')
