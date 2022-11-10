#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/11/2022 下午5:05
# @Author  : 刘双喜
# @File    : 5.鸢尾花种类预测-流程实现.py
# @Description : 添加描述
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

# 获取数据
iris = load_iris()
target_data = iris.target
feature_data = iris.data
print('目标值数据\n', target_data)
print('特征数据\n', feature_data)
# 数据分割测试集和训练集
feature_data_train, feature_data_test, target_data_train, target_data_test = train_test_split(feature_data, target_data,
                                                                                              test_size=0.2,
                                                                                              random_state=22)
print('训练集特征数据：\n', feature_data_train)
print('训练集目标数据：\n', target_data_train)
print('测试集特征数据：\n', feature_data_test)
print('测试集目标数据：\n', target_data_test)

# 特征预处理
# 实例化转换器
transfer = StandardScaler()
feature_data_train = transfer.fit_transform(feature_data_train)
feature_data_test = transfer.fit_transform(feature_data_test)
print('标准化后的特征值训练数据：\n', feature_data_train)
print('标准化后的特征值测试数据：\n', feature_data_test)

# 训练数据
# 实例化训练器
estimator = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
estimator.fit(feature_data_train, target_data_train)

# 预测数据
target_data_predict = estimator.predict(feature_data_test)
print('预测的目标值：\n', target_data_predict)
print('实际的目标值：\n', target_data_test)
print('对比的目标值：\n', target_data_predict == target_data_test)

score = estimator.score(feature_data_test, target_data_test)
print('准确度:\n', score)
