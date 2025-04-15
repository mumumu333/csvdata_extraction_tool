## ＜ツール概要＞  
csvの1列目のnumberと検索対象列のアルファベットをrun.batで指定。データを抽出し、result.txtに出力する。

## ＜インストール編＞  
■Python インストール（このプロジェクトではPython 3.12.4を使用しています）  
https://www.python.org/downloads/

## ＜事前準備編＞  
①仮想環境作成  
参考URL：https://qiita.com/nosniklim/items/1d4c480e3accd3eb8c0f  

・仮想環境作成  
py -m venv csvdata_extraction_tool  

・仮想環境を有効にする  
cd csvdata_extraction_tool  
Scripts\activate    

②csvdata_extraction_tool.py、run.bat、list.csvを①で作成した仮想環境配下に持っていく  

③run.batファイルの中身を編集。下記の引数で実行されるため抽出したいデータに応じて変更する  
py csvdata_extraction_tool 検索対象CSVファイルの親ディレクトリ  検索対象CSVファイル名 csv1列目の番号 csv抽出対象列のアルファベット　>> result.txt  

(例.)csv1列目のnumberが2かつB列の値を抽出したい場合  
set file_path="C:\Users~\csvdata_extraction_tool"  
set file_name="namelist.csv"  
py csvdata_extraction_tool.py %file_path% %file_name% 2 "B" >> result.txt  

④コマンドプロンプトにてrun.batファイルを実行。結果がresult.txtに出力される。  
run.bat  

## ＜run.batファイル実行時に文字化けしているとき、ディレクトリ指定でエラーが出る場合＞
chcp 65001  
を入力して再度実行
