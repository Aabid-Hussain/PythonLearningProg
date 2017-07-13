
def word_count_func(filename):
    word_count_dic = {}

    input_filename = open(filename, 'r')

    for line in input_filename:
        words = line.split()
        for word in words:
            word = word.lower()
            #word = word.lower().isalpha()
            if not word in word_count_dic :
                word_count_dic[word] = 1

            else:
                word_count_dic[word] += 1

    input_filename.close()

    return word_count_dic


 #defing print function

def print_word_count(filename):

    word_count = word_count_func(filename)

    words = sorted(word_count.keys())

    for word in words:
        print("{} : {}".format(word, word_count[word]))
        # if not word.isalnum():
        #     print("{} : {}".format(word, word_count[word]))
        # else:
        #     pass
    print("Total Length of dict: {}".format(len(words)))

print_word_count("E:\ME\Agile testing.txt")