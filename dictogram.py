from __future__ import division, print_function # Python 2 and 3 compatability

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dictionary type"""


    def __init__(self, word_list=None):
        """Initialize this histogram as a new dictionary and count given words"""
        super(Dictogram, self).__init__() # Initialize this as a new dictionary

        self.types = 0 # unique count of words
        self.tokens = 0 # total len of words in histogram

        # Initialize the dictogram with the passed in word list
        if word_list is not None:
            self.add_count(word_list)

    def add_count(self, word_list, count=1):
        """Increase frequency count of given word by given count amount"""
        for word in word_list:
            # check to see if word is not in dictogram
            # IF NOT: add word and increment count, tokens, types
            if word not in self:
                self[word] = count
                self.tokens += count
                self.types += count

            # if word is in dictogram, increment count, tokens
            else:
                self[word] += count
                self.tokens += count

    def frequency(self, word, word_list):
        """Return frequency count of given word, or 0 if word is not found"""
        word_frequency = 0
        for key in word_list:
            if key == word:
                word_frequency += 1
        return word_frequency


def print_histogram(word_list):
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))



def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())



if __name__ == '__main__':
    main()
