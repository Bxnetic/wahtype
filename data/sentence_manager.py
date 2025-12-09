import random

class Sentence:
    def __init__(self):
        pass

    def get_easy_sentence(self, number):
        words = [] # words are stored in the array
        sentence = "" # to construct the sentence

        with open('data\\databases\\words.txt', 'r') as file:
            # reads through each line
            for line in file:
                # reads each word in the line
                for word in line.split():
                    words.append(word) # add word to words array

        sentence = " ".join(random.choices(words, k=number)) # randomly choose x words to be added into sentence
        # and add spaces between every word

        return sentence

sentence = Sentence()