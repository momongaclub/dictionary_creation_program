import argparse
import re

FILE_SEPARATER = '[\s/]'


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


def max_element(word_list):
    u"""
    word_listは要素が全て文字列のlistを仮定
    word_list内の最も多い要素を返す
    """
    word_set_list = set(word_list)
    for element in word_list:
        cnt = 0
        maxcnt = -1
        for element in word_set_list:
            cnt += 1 
        if cnt > maxcnt:
            maxcnt = cnt
            maxelement = element
    return maxelement


def equal_word_list(train_word_class, test_word_class):
    u"""
    train_word_classはstring,test_word_classはstringを仮定
    train_word_classがtest_word_class同じであるかTrue,Falseを返す
    """
    if train_word_class == test_word_class:
        return True
    else:
        return False


def guess_word(word_dict, test_dict, word_list):
    u"""
    word_dictはkeyが文字列,要素が文字列のlist,word_listは要素が全て文字列のlistを仮定
    word_list内全ての単語とその品詞を'単語/品詞'の形で出力する
    """
    cnt = 0
    for word in word_list:
        if word in word_dict:
            print(word + '/' + max_element(word_dict[word]), end = " ")
            if equal_word_list(max_element(word_dict[word]), max_element(test_dict[word])) == True:
                cnt += 1
            #print(max_element(word_dict[word]), max_element(test_dict[word]))
        else:
            cnt += 1
            print(word + '/' + 'N', end=" ")
    return len(word_list)-cnt

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
    #print(guess_word(train_dict, test_dict, dict_words_set))

main()

