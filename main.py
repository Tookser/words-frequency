#!/usr/bin/env python3
'''Script counting some stats on word frequency'''
FILE_IN = 'google-10000-english.txt'
FILE_OUTPUT = 'output.txt'


words = []

def load_words():
    '''загружает слова в words'''
    with open(FILE_IN) as f:
        for line in f:
            word = line.strip()
            words.append(word)


def create_word_list():
    '''создаёт список из слов, подходящих под некоторые условия'''
    with open(FILE_OUTPUT, 'w') as f:
        query = words[:2000]
        # min_size = len(min(query, key=len))
        min_size = 12

        for i, word in enumerate(query):
            if len(word) >= min_size:
                f.write(word+'\n')


def create_hysto(words):
    STEP = 100

    def calc_mean_length(arr):
        return sum(arr) / len(arr)

    import matplotlib.pyplot as plt
    len_words = [len(word) for word in words]

    x = []
    y = []
    for i in range(0, len(words), STEP):
        x.append(f'{i//100}-{(i+STEP)//100}')
        y.append(calc_mean_length(len_words[i:i+STEP]))

    import matplotlib.pyplot as plt

    plt.bar(x,y)
    plt.title('Mean length by word frequency')
    plt.xlabel('Range (*100)')
    plt.ylabel('Mean length')
    plt.show()


if __name__ == '__main__':
    #load words
    load_words()

    #uncomment this string to create word-list
    #create_word_list()

    #show chart
    create_hysto(words[:2000])
