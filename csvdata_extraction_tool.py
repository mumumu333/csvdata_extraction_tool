import csv
import pprint
import io, sys

# 出力時の文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 引数の数が合っていなければエラーを出力
if len(sys.argv) != 5:
    sys.stderr.write("引数の数が違います。下記の引数を入れてください\n[第１引数：csvdata_extraction_tool.py] [第２引数：検索対象CSVファイルの親ディレクトリ] [第３引数：検索対象CSVファイル名] [第4引数：検索対象number] [第５引数：抽出対象列のアルファベット]\n")
    sys.exit()

# 検索対象CSVファイルの親ディレクトリ
search_target_csvfile_directry = sys.argv[1]
# 検索対象CSVファイル名
search_target_csvfile_name     = sys.argv[2]
# 検索対象number
search_target_num              = sys.argv[3]
# 抽出対象列のアルファベット
search_result_column_alp       = sys.argv[4]

# 抽出するCSVのファイルパスを生成
path = search_target_csvfile_directry + '/' + search_target_csvfile_name

def DistExtraction(num, search_result_column_alp):
    try:
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                # 検索対象numberに合致する行を抽出
                if(row[0] == num):
                    # 抽出対象列のアルファベットの値を取得する
                    search_result_column_alp = AlphabetToNumber(search_result_column_alp)    
                    result_value = row[search_result_column_alp]
                    flg = True
                    return result_value, flg

    # パスが長すぎる場合はエラーを出力
    except FileNotFoundError:
        sys.stderr.write("検索対象のファイルが見つかりません。ディレクトリ、ファイル名が正しいか確認してください")
        sys.exit()

def AlphabetToNumber(alphabet):
    alphabet = alphabet.upper()
    col_num = 0
    for char in alphabet:
        col_num = col_num * 26 + (ord(char) - 64)
    return col_num - 1

search_result_value = 0
is_search_result_found_flg = False

# 関数から返された値を受け取る
search_result_value, is_search_result_found_flg = DistExtraction(search_target_num, search_result_column_alp)

first_line   = search_target_csvfile_name + '\n'
secound_line = '【number】' + search_target_num + '\n'
third_line   = '【' + search_result_column_alp + '列の値】' + str(search_result_value) + '\n' + '\n'

print(first_line+secound_line+third_line)
