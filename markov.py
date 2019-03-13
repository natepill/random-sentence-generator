from dictogram import Dictogram
from rando_word import random_word
import sys
import os
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


    def nth_order_markov_chain(order, text_list):
        """ this function takes in a word and checks to see what words come after it
        to determine the word sequence for our generated markov chain"""
        markov_dict = dict()
        # for each word in list, key is word and value is dictogram
        for index in range(len(text_list) - order):
            # text_list[index] should be our word from list, and we're slicing based on the order of the markov chain
            window = tuple(text_list[index: index + order])
            # check if key is stored already
            if window in markov_dict:
                # if it is, then append it to the existing histogram
                # NOTE: Instead of going through the corpus repeatedly, lets save text_list[index + order] in scope
                markov_dict[window].add_count([text_list[index + order]])
            else:
                # if not, create new entry with window as key and dictogram as value
                markov_dict[window] = Dictogram([text_list[index + order]])
        # return dictionary
        return markov_dict


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
