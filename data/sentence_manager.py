from wonderwords import RandomWord

class Sentence():
    def __init__(self):
        self.randomword = RandomWord()
    
    
    def get_sentence(self):
        words = [] # words are stored in the array
        sentence = "" # to construct the sentence
        for _ in range(15): # loop 15 times to create sentence with 15 words
            words.append(self.randomword.word(include_parts_of_speech=["nouns", "verbs", "adjectives"],
             word_max_length=5, word_min_length=2))
            sentence = " ".join(words) # adds a blank character 

        return sentence

sentence = Sentence()