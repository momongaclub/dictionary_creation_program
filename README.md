# dictionary_creation_program
作成中

# 進捗
ひとまずlex_prob.dictを出力できるように〇  
bigram_prob.dictの出力 〇

# 設計書
前処理部分

入力：
品詞情報付き英語コーパス

形式：
単語1/品詞1 単語2/品詞2 ... 単語n/品詞n

条件：
単語と品詞の組を要素と定義する.
一行一文形式、各要素は空白で区切られていて、単語と品詞は/で区切られている.

出力：
要素をkey,要素の出現回数を値とした辞書

形式：
{単語1/品詞1:出現回数, 単語2/品詞2:出現回数, ... ,単語n/品詞n:出現回数}

条件：
要素と出現回数のペアを要素出現回数と定義する.
要素出現回数の入った辞書を要素出現回数辞書と定義する.

1.データ読み込み
1-1.
sample.trainを要素ずつ読み込む

2.処理
2-1.
要素を要素出現回数辞書に代入する.
2-2.
要素が要素出現回数辞書にあれば要素出現回数の出現回数を＋1する.
要素がなければ出現回数は0に初期化する.

3.出力
3-1.
要素出現回数辞書を出力する.



・品詞分類部分

入力：
単語コーパス

形式：
単語1 単語2 ... 単語n

条件：
単語は半角スペース区切りで与えられる.

出力：
単語の品詞解析結果

形式：
単語1/品詞1 単語2/品詞2 ... 単語n/品詞n

条件：
単語に対して要素出現回数辞書の出現回数が最も多いものを品詞として付与する.


1.データ読み込み
1-1.
データ処理で作成した要素出現回数辞書を読み込む
1-2.
単語コーパスを１単語ずつ読み込む

2.分類用のデータの作成
2-1.
要素出現回数辞書から各単語の出現回数が最大の品詞を抽出する.

3.分類処理
3-1.
単語に対して抽出した品詞を付与する.

4.出力
4-1.
付与された文字列を出力する.



