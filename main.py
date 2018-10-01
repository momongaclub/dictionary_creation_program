import argparse
import re

FILE_SEPARATER = '[\s/]'

def parse():

    parser = argparse.ArgumentParser()
    parser.add_argument('sample_train')

    args = parser.parse_args()

    return args


def load_input_file(fname):

    word_dict = {}
    pos_list = []

    with open(fname, 'r') as fp:
        for line in fp:
            line = re.split(FILE_SEPARATER, line)
            for word, pos in zip(line[0::2], line[1::2]):
                print('word', word, 'pos', pos)
                word_dict[word] = pos
    return word_dict


def convert_text_to_dict(text, ope='r'):
    u"""
    text,opeは文字列を仮定する
    """
    with open(text, ope) as f:
        letter, letters = '', ''
        word, word_class = '', ''
        word_dict = {}
        flag = False
        str = f.read()
        for i in ('\n', ':', ';', '.', ',', "''", '(', ')'):
            str = str.replace(i, '')
        for letter in str:
            if letter == '/' or letter == ' ':
                if flag == False:
                    word = letters
                    flag = True
                else:
                    word_class = letters
                    if word in word_dict:
                        word_dict[word].append(word_class)
                    else:
                        word_dict[word] = [word_class]
                    flag = False
                    word, word_class = '', ''
                letters=''
            else:
                letters += letter
    return word_dict


def convert_text_to_dict_split(text, ope='r'):

    with open(text, ope) as f:
        str = f.read()
        str.replace('\n', '')
        splitstring = str.split('/')
    #print(splitstring)
    return 0


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


def guess_word(word_dict, word_list, test_dict):
    u"""
    word_dictはkeyが文字列,要素が文字列のlist,word_listは要素が全て文字列のlistを仮定
    word_list内全ての単語とその品詞を'単語/品詞'の形で出力する
    """
    cnt = 0
    for word in word_list:
        if word in word_dict:
            #print(word + '/' + max_element(word_dict[word]), end = " ")
            if equal_word_list(max_element(word_dict[word]), max_element(test_dict[word])) == True:
                cnt += 1
            #print(max_element(word_dict[word]), max_element(test_dict[word]))
        else:
            cnt += 1
            #print(word + '/' + 'N', end=" ")
    return len(word_list)-cnt


def main():
    args = parse()
    print(load_input_file(args.sample_train))
    #train_dict = convert_text_to_dict('sample.train.txt', 'r')
    #test_dict = convert_text_to_dict('sample.test.txt', 'r')
    #a = convert_text_to_dict_split('sample.train.txt', 'r')
    #print(train_dict)
    #print(guess_word(train_dict, test_dict.keys(), test_dict))

main()
