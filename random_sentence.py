from random import randint
from histogramDict import read_txt_file
from stochasticAttempt2 import *

"""
Will read in text and then output sentence with random words from a text

Read in text (Currently reading in from stochastic-attempt2, but can refactor to read a different text file--> comment out stochastic-attempt2's main function and just pass in differnt text once you've imported it into this file)
Random number of words for sentence
Choose words randomly from the text and store in list
Once all words have been chosen, take list and convert it into sentence.

"""
#turns text into list so we can choose random words
def text_to_list(file_name):
    return read_txt_file(file_name)

#choose random number of words to have in our sentence
def random_num_words():
    return randint(8, 20)

#takes in the source text as a list and returns a random word from the list
def get_random_word(text_list):
    return random_word(text_list)


#Takes random number of words to create a sentence and generates a sentence by picking random words and putting them together
def generate_sentence(text_list):
    num_of_words = random_num_words()
    sentence_list = list()

    for _ in range(num_of_words):
        sentence_list.append(get_random_word(text_list))

    return ' '.join(sentence_list)



# if __name__ == "__main__":
#
#     text_list = text_to_list('blog-text')
#     # print(get_random_word(text_list))
#     print(generate_sentence(text_list))
