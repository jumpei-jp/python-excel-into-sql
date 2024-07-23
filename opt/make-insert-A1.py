import pandas as pd
import os

# Excelファイルを読み込む
excel_file = "../excel/sample_01.xlsx"
df = pd.read_excel(excel_file)

# テーブル名
table_name = 'sample_table_01'

# INSERT文を格納するリスト
insert_statements = []

# カラム名を指定
columns = ['No', 'Name', 'school', 'student_id', 'birthday', 'address']

# INSERT文を作成
for index, row in df.iterrows():
    # 行の値をカンマ区切りの文字列に変換
    values = ', '.join([f"'{str(v)}'" if isinstance(v, str) else str(v) for v in row])

    # INSERT文の作成
    insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"

    # リストに追加
    insert_statements.append(insert_stmt)

# ファイルに出力
output_directory = '../output'
output_file_name = 'insert_sample_01.sql'
output_file = os.path.join(output_directory, output_file_name)

# ディレクトリが存在しない場合は作成
os.makedirs(output_directory, exist_ok=True)

with open(output_file, 'w') as f:
    for stmt in insert_statements:
        f.write(stmt + '\n')

print(f"INSERT statements have been written to {output_file}")
