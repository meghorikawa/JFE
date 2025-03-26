#  Create a class to sort the participants by their number and JCAT score and score for each feature


class Participant:

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.tasks = []
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
        return f'Participant: {self.name} J-Cat Score: {self.score} Words per Sent: {self.WPSavg} CTTR: {self.CTTR}'
