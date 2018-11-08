from random import randint
from histogramDict import *

# histogram = histogram-dict.histogram(str(sys.argv[1]))

#TODO Make function truly pick a random word based upon frequency
def file_words(text):
     word_list = read_txt_file(text)
     return word_list


def get_frequency(corpus_list, word):
    # print(corpus_list)
    hist = histogram(corpus_list)
    list_of_frequency = list()
    for key, value in hist.items():
        list_of_frequency.append([key, value/len(corpus_list)])

    return list_of_frequency

def weighted_choice(weights):
    values = [] # 2,5,10
    running_total = 0 #10

    for w in weights:
        running_total += w
        values.append(running_total)

    rnd = random.random() * running_total
    for i, value in enumerate(values):
        if rnd < value:
            return weights[i]
#https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python

def true_random_selection(freq_weight, word):

    random_prob = random.random()
    for word-probability in freq_list:


    # Generate a number between 0 and 1.
    # Walk the list substracting the probability of each item from your number.
    # Pick the item that, after substraction, took your number down to 0 or below.


if __name__ == '__main__':
    # rand_wrd = random_word()
    corpus_list = file_words('fish.txt') #Need to integrate sys.argv[1] instead of file name
    print(get_frequency(corpus_list, "red"))
    # print(random_word(histogram(corpus_list)))
