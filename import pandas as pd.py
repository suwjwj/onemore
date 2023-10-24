import pandas as pd
import ast
from tqdm import tqdm

# 读取源数据文件
df = pd.read_excel("C:\\Users\\86159\\Desktop\\text\\fullvideo_data.xlsx")

# 转换时间戳并转换成北京时间
if "pubdate" in df.columns:
    print("正在转换时间戳...( •̀ ω •́ )y")
    df["pubdate"] = pd.to_datetime(df["pubdate"], unit='s') + pd.Timedelta(hours=8)

# 将字符串转换成列表和字典，方便后面的展开
cols_to_convert = ["member", "laststat"]
print("正在转换字符串到列表和字典...( •̀ ω •́ )y")
for col in tqdm(cols_to_convert):
    if col in df.columns:
        df[col] = df[col].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else {})

# 展开数据
print("正在展开数据...( •̀ ω •́ )y")
df_laststat = df['laststat'].apply(pd.Series, dtype='object')
df_member = df['member'].apply(pd.Series)
df.drop(["laststat"], axis=1, inplace=True)
df.drop(['member'], axis=1, inplace=True)

df = pd.concat([df, df_laststat, df_member], axis=1)

# 删除掉无用列表
columns_to_drop = ["videos", "added", "tid", "tname", "copyright", "code", 
                  "attribute", "state", "forward", "hasstaff", "singer", 
                  "solo", "original", "employed", "isvc", "engine", "freq", 
                  "activity", "recent", "dislike", "now_rank", "his_rank"]

print("正在删除无用列...( •̀ ω •́ )y")
for col in tqdm(columns_to_drop):
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)


# 保存处理好的文件
print("正在保存处理后的文件...( •̀ ω •́ )y")
output_path = "C:\\Users\\86159\\Desktop\\text\\VOCALOID分区数据_processed.xlsx"
df.to_excel(output_path, index=False)
print("处理完成!(❁´◡`❁)")



file_path = "C:\\Users\\86159\\Desktop\\text\\VOCALOID分区数据_processed.xlsx"  # 请替换为你的文件路径
df = pd.read_excel(file_path)

# 定义一个映射字典来转换性别为数值
sex_mapping = {
    '男': 1,
    '女': 2,
    '保密': 0
}

# 使用映射字典替换原始的性别值
print("正在转换性别...( •̀ ω •́ )y")
df['sex'] = tqdm(df['sex'].map(sex_mapping))

# 保存为新的Excel文件
output_path = "C:\\Users\\86159\\Desktop\\text\\类型转数值.xlsx"  # 请替换为你想要保存的文件路径
df.to_excel(output_path, index=False)

print("处理完成!(❁´◡`❁)")


file_path = "C:\\Users\\86159\\Desktop\\text\\类型转数值.xlsx"  # 请替换为你的文件路径
df = pd.read_excel(file_path)

# 2 & 3. 新增legend列，并根据view列的值为其赋值
df['legend'] = tqdm((df['view'] > 100000).astype(int))

# 4. 将更改后的数据保存到新的Excel文件
output_path = "C:\\Users\\86159\\Desktop\\text\\legend.xlsx"  # 更改为您想要保存新文件的路径
df.to_excel(output_path, index=False)

print("处理完成!(❁´◡`❁)")


import pandas as pd

# 从Excel文件读取数据
full = pd.read_excel("C:\\Users\\86159\\Desktop\\text\\legend.xlsx")

# 打印数据框的形状
print('Datasets:', 'full:', full.shape)

full.head()

full.describe()

full.info()


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 选择数值列，并计算相关性矩阵
numerical_columns = full.select_dtypes(include=[np.number])
correlation_matrix = numerical_columns.corr()

# 创建一个热力图
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# 设置图表标题
plt.title("Correlation Heatmap")

# 显示图表
plt.show()

df = pd.read_excel("C:\\Users\\86159\\Desktop\\text\\legend.xlsx")


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")  # 可以选择不同的样式，例如："darkgrid"、"white"、"ticks"等


# 设置字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义要可视化的变量列表
variables = ['view', 'favorite', 'coin', 'like']

# 为每个变量绘制箱线图
plt.figure(figsize=(15, 10))
for i, var in enumerate(variables, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(y=df[var])
    plt.title(f'箱线图 - {var}')
    plt.ylabel(var)

plt.tight_layout()
plt.show()


df = pd.read_excel("C:\\Users\\86159\\Desktop\\text\\VOCALOID分区数据_processed.xlsx")

sns.set_style("darkgrid")  # 可以选择不同的样式，例如："darkgrid"、"white"、"ticks"等

# 设置字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(15, 10))
for i, var in enumerate(variables, 1):
    plt.subplot(2, 2, i)
    sns.violinplot(y=df[var])
    plt.title(f'小提琴图 - {var}')
    plt.ylabel(var)

plt.tight_layout()
plt.show()