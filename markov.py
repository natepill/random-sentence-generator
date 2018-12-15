from dictogram import Dictogram
from rando_word import random_word
import sys
import random

class MarkovChain:

    def build_markov(self):
        dict = {}
        with open('holmes-text.txt') as file:
            corpus = file.read().split()

        i=0
        while i+1 < len(corpus):
            word = corpus[i]
            if dict.get(word) == None:
                next_word = corpus[i+1]
                list = [next_word]
                histogram = Dictogram(list)
                dict[word] = histogram
            else:
                next_word = corpus[i+1]
                dict.get(word).add_count(next_word)
            i += 1

        return dict

    def generate_sentence(self, dict):
        sentence = ""
        list_of_keys = list(dict.keys())
        index = random.randint(0, len(list_of_keys)-1)
        chosen_word = list_of_keys[index]
        sentence = sentence + chosen_word

        for _ in range(0,20):
            dictogram = dict.get(chosen_word)
            print(dictogram)
            new_word = random_word(self, dictogram)
            sentence = sentence +" "+ new_word
            chosen_word = new_word

        print(sentence)
        return sentence



if __name__ == '__main__':
    markov = MarkovChain()
    dict = markov.build_markov()
    markov.generate_sentence(dict)
