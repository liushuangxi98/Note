#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/10/2022 下午1:15
# @Author  : 刘双喜
# @File    : try.py
# @Description : 添加描述
import pandas as pd
s = pd.Series({1:2},)
#print(s.values)
s1= pd.DataFrame([[1, {2},[3,4],5,6],[11]], {1,2},{1,2,3,7,9})
print(s1)
s1.to_excel('1.xlsx',)