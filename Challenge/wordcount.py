def word_count_function(filename):

    word_count = {}

    input_file = open(filename,'r')

    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if not word in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    input_file.close()
    return word_count


def print_function(filename):
    word_count = word_count_function(filename)

    words = sorted(word_count.keys())

    for word in words:
        print("{}:{}".format(word,word_count[word]))



print_function('TestData.txt')