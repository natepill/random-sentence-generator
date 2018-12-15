from random import randint


def random_word(self, histogram_dict):
    '''Random word with weighted probability'''
    counter = 0
    # Random number between 0 and the sum total of all frequencies
    hist_sum = sum(histogram_dict.values())
    rand_sum = randint(0,hist_sum - 1)

    for key, value in histogram_dict.items():
        counter += value
        if counter > rand_sum:
            return key
        else:
            continue
