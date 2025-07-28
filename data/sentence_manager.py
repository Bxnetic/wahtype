from wonderwords import RandomWord
import random

class Sentence:
    def __init__(self):
        self.randomword = RandomWord()
    
    def get_easy_sentence(self):
        words = [] # words are stored in the array
        sentence = "" # to construct the sentence

        with open('data\\words.txt', 'r') as file:
            # reads through each line
            for line in file:
                # reads each word in the line
                for word in line.split():
                    words.append(word) # add word to words array

        sentence = " ".join(random.choices(words, k=15)) # randomly choose 15 words to be added into sentence
        # and add spaces between every word

        return sentence


    def get_sentence(self):
        words = [] # words are stored in the array
        sentence = "" # to construct the sentence
        for _ in range(15): # loop 15 times to create sentence with 15 words
            words.append(self.randomword.word(include_parts_of_speech=["nouns", "verbs", "adjectives"],
             word_max_length=5, word_min_length=2))
            sentence = " ".join(words) # put words into sentence and add spaces between every word

        return sentence

sentence = Sentence()