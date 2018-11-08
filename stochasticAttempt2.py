from random import randint


def file_words(text):
     word_list = histogramDict.read_txt_file(text)
     return word_list


def histogram_to_list(corpus_list):
    # print(corpus_list)
    hist = histogram(corpus_list)
    list_of_frequency = list()

    for key, value in hist.items():
        # list_of_frequency.append(key) * value
        list_of_frequency += [key for _ in range(value)]
        # list_of_frequency.append([key, value/len(corpus_list)])
        # print(new_list)
    return list_of_frequency


def get_frequency(corpus_list, word):
    # print(corpus_list)
    hist = histogram(corpus_list)
    list_of_frequency = list()
    for key, value in hist.items():
        list_of_frequency.append([key, (value/len(corpus_list))])

    return list_of_frequency


def random_word(freq_list):
    index = randint(0, len(freq_list)-1)
    return freq_list[index]


# def weighted_choice(weights):
#
#     values = [] # 2,5,10
#     running_total = 0 #10
#
#     for w in weights:
#         running_total += w
#         values.append(running_total)
#
#     rnd = random.random() * running_total
#     for i, value in enumerate(values):
#         if rnd < value:
#             return weights[i]
#             #https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python

def generateRandomSentence(dictionaryOfProbability, num_words):
    counter = 1
    test_dict = {}
    list_of_word_types = list(dictionaryOfProbability.keys())
    while counter < num_words:
        random_word = random.choice(list_of_word_types) #use generate random word function
        random_chance = random.random()
        if dictionaryOfProbability[random_word] > random_chance:
            if random_word not in test_dict: # counter function
                # add to dictionary
                test_dict[random_word] = 1
            else:
                # already exists in dictionary, so increment counter at that key
                test_dict[random_word] += 1
            counter += 1
    print(test_dict)

    #Nicolai's code ^^^




# if __name__ == "__main__":
#     corpus_list = file_words('fish.txt') #Need to integrate sys.argv[1] instead of file name
#     freq_list = histogram_to_list(corpus_list)
    # print(get_frequency(corpus_list, "fish"))
    # print(random_word(freq_list))
