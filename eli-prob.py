import random
# import histogramDict
# 2,3,5
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


def histogram(corpus_list):
    dictogram = {}

    for word in corpus_list:
        dictogram[word] = 0

    for word in corpus_list:
        dictogram[word] += 1

    return dictogram

if __name__ == '__main__':
    weights_list = list()
    for _ in range(1000):
        weights_list.append(weighted_choice([2,3,5]))
        weights_list = map(str, weights_list)
        weights_list = list(weights_list)
    print(histogram(weights_list))
    # stringify_list = ' '.join(weights_list)



    # print(random_word(histogram(corpus_list)))
