import pandas as pd

# 读取Excel文件
df = pd.read_excel('1111.xlsx')

col1 = df['id1']
col2 = df['id2']


#判断id1 在不在id2中，如果不在 输入id2中多余的数据
diff_ids = df[df['id1'].isin(df['id2']) == False]['id2'].tolist()
print(diff_ids)

# diff = col1.compare(col2)
# diff = col1.compare(col2)
# missing_values = pd.concat([df['id1'], df['id2']]).isnull().sum()
# # print(missing_values)
# #
# missing_ids = df['id2'].isin(df['id1'])
#
# # 输出id2列中缺失的数据
# missing_ids_list = df[~missing_ids]['id2'].tolist()
# print(missing_ids_list)

