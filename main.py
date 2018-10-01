import argparse
import re

FILE_SEPARATER = '[\s/]'
MIN_NUMBER = -1
BRANK = ''


def parse():

    parser = argparse.ArgumentParser()
    parser.add_argument('sample_train')
    parser.add_argument('sample_test')

    args = parser.parse_args()

    return args


def load_input_file(fname):

    word_dict = {}

    with open(fname, 'r') as fp:
        for line in fp:
            line = re.split(FILE_SEPARATER, line)
            for word, pos in zip(line[0::2], line[1::2]):
                pos_list = word_dict.get(word, [])
                pos_list.append(pos)
                word_dict[word] = pos_list

    return word_dict


def max_element(pos_list):
    u"""
    word_listは要素が全て文字列のlistを仮定
    word_list内の最も多い要素を返す
    """
    pos_set = set(pos_list)
    max_NOO = MIN_NUMBER
    max_pos = BRANK

    for pos in pos_set:
        NOO = pos_list.index(pos)# number of occurrences
        if NOO > max_NOO:
            max_NOO = NOO
            max_pos = pos

    return max_pos


def define_pos(word_dict, test_dict, word_list):

    for word in word_list:
        pos_list = word_dict.get(word, ['None'])
        print(word + '/' + max_element(pos_list)) # TODO max elements is not correct.


def main():
    args = parse()
    train_dict = load_input_file(args.sample_train)
    test_dict = load_input_file(args.sample_test)
    dict_words_set = test_dict.keys()
    define_pos(train_dict, test_dict, dict_words_set)

main()

