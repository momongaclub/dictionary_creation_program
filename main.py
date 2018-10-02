import argparse
import re

FILE_SEPARATER = '[\s/]'
CONECT_W_AND_P = '/'
TAB_SPACE = '\t'
BRANK = ''


def parse():

    parser = argparse.ArgumentParser()
    parser.add_argument('corpus', 
                        help = 'English word corpus with part of speech tag')
    args = parser.parse_args()

    return args


def corpus2dict(fname):

    word_dict = {}

    with open(fname, 'r') as fp:
        for line in fp:
            line = re.split(FILE_SEPARATER, line)
            for word, pos in zip(line[0::2], line[1::2]):
                pos_list = word_dict.get(word, [])
                pos_list.append(pos)
                word_dict[word] = pos_list

    return word_dict


def calc_lex_prob(word, pos_list):
    u"""
    input: pos_list
    output: lex
    """
    pos_set = set(pos_list)
    lex_prob = []

    for pos in pos_set:
        lex_prob.append(pos)
        lex_prob.append(pos_list.count(pos) / len(pos_list))

    return lex_prob


def make_lex_dict(word_dict, word_list):
    
    lex_list = []

    for word in word_list:
        pos_list = word_dict.get(word, ['None'])
        lp = calc_lex_prob(word, pos_list)
        for pos, prob in zip(lp[0::2], lp[1::2]):
            lex = word + CONECT_W_AND_P + \
            pos + TAB_SPACE + str(prob)
            
            lex_list.append(lex)
    
    write_dict('lex_prob.dict', lex_list)

def calc_bigram_prob(bigram_dict):

    num = 0

    for value in bigram_dict.values():
        num += value

    for key, value in bigram_dict.items():
        bigram_dict[key] = value / num

    return bigram_dict


def make_bigram_dict(fname):

    bigram_dict = {}
    bigram_list = []

    with open(fname, 'r') as fp:
        for line in fp:
            line = re.split(FILE_SEPARATER, line)
            pos_list = line[1::2]
            for b_pos, a_pos in zip(pos_list[0::], pos_list[1::]):
                bigram = b_pos + '-' + a_pos
                bigram_num = bigram_dict.get(bigram, 0)
                bigram_dict[bigram] = bigram_num + 1

        bigram_dict = calc_bigram_prob(bigram_dict)
        for bigram, prob in bigram_dict.items():
            bigram_list.append(bigram + TAB_SPACE + str(prob))
        write_dict('bigram_prob.dict', bigram_list)
    
    return bigram_dict


def write_dict(fname, prob_list):

    with open(fname, 'w') as fp:
        fp.writelines('\n'.join(prob_list))


def main():
    args = parse()
    english_dict = corpus2dict(args.corpus)
    make_bigram_dict(args.corpus)
    dict_words_set = english_dict.keys()
    make_lex_dict(english_dict, dict_words_set)

main()

