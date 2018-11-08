import sys

# reads in a text files, returns a list
def read_txt_file(file_name):
    with open(file_name) as file:
        corpus_list = file.read().split()
        return corpus_list

def histogram(corpus_list):
 # stores each unique word along with the number of times the word appears in the source text
    dictogram = {}

    for word in corpus_list:
        dictogram[word] = 0

    for word in corpus_list:
        dictogram[word] += 1

    # for word in corpus_list:
    #     word_index = corpus_list.index(word)
    #     if word in corpus_list[word_index:-1]
    #         dictogram[word] =1

    # for word in corpus_list:
    #     if word in dictogram:
    #         dictogram[word] += 1

    return dictogram




def unique_words(histogram):
    # takes a histogram argument and returns the total count of unique words in the histogram.
    # return histogram.keys()
    unique_count = 0
    for word in histogram:
        unique_count += 1
    return unique_count


def frequency(word, histogram):
    # takes a word and histogram argument and returns the number of times that word appears in a text.
    return histogram[word]



# print(histogram(blog))
# print(unique_words(histogram(blog)))
# print(frequency('was', histogram(blog)))
