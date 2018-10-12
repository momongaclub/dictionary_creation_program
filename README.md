# dictionary_creation_program
入力：英文品詞タグ付きコーパス  
出力：lex_prob_dict, bigram_prob_dict

# 実行手順
`$ python corpus2dict.py corpus.data`

# コーパスの形式
単語1/品詞1 単語2/品詞2 ... 単語n/品詞n
一行一文形式、各要素は空白で区切られていて、単語と品詞は/で区切られている.
(例)
