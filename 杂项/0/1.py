#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 23:34
# @Author  : 刘双喜
# @File    : 1.py
# @Description : 添加描述
import os
import pandas as pd
import matplotlib.pyplot as plt

# 获取当前目录下所有的.xlsx文件
files = [f for f in os.listdir() if f.endswith('.xlsx')]

# 创建一个空的DataFrame来存储合并后的数据
merged_data = pd.DataFrame()

for file in files:
    # 读取Excel文件
    data = pd.read_excel(file)
    # 选择第3、4、5列数据
    selected_data = data.iloc[:, [3,4,5]]
    # 重命名
    columns = list(data.columns[3:6])
    new_columns = {column: str(data.iloc[0, 1])+column for column in columns}
    selected_data.rename(columns=new_columns, inplace=True)
    # 将选择的数据添加到merged_data中
    merged_data = pd.concat([merged_data, selected_data])

# 将合并后的数据保存到新的Excel文件中
merged_data.to_excel('merged.xlsx', index=False)

# 绘制图表并保存为图片文件
merged_data.plot()
plt.savefig('chart.png')