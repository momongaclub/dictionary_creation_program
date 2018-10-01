import argparse
import re

FILE_SEPARATER = '[\s/]'
MIN_NUMBER = -1
CONECT_W_AND_P = '/'
TAB_SPACE = '\t'
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


def lex_prob(word, pos_list):
    u"""
    input: pos_list
    output: lex
    """
    pos_set = set(pos_list)
    lex = []

    for pos in pos_set:
        lex.append(pos)
        lex.append(pos_list.count(pos) / len(pos_list))
    return lex


def make_lex_dict(word_dict, test_dict, word_list):
    
    lex_list = []

    for word in word_list:
        pos_list = word_dict.get(word, ['None'])
        lp = lex_prob(word, pos_list)
        for pos, prob in zip(lp[0::2], lp[1::2]):
            lex = word + CONECT_W_AND_P + \
            pos + TAB_SPACE + str(prob)
            lex_list.append(lex)
    
    write_dict('lex_prob.dict', lex_list)

def make_bigram_dict(word_dict, test_dict, word_list):

    bigram_list = []



    return 0


def write_dict(fname, prob_list):

    with open(fname, 'w') as fp:
        fp.writelines('\n'.join(prob_list))


def main():
    args = parse()
    train_dict = load_input_file(args.sample_train)
    # ここでbigram_dictを作成しないと遷移がわからない
    test_dict = load_input_file(args.sample_test)
    dict_words_set = train_dict.keys()# before test
    make_lex_dict(train_dict, test_dict, dict_words_set)

main()

