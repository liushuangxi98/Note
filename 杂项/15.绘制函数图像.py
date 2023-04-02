#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 21:09
# @Author  : 刘双喜
# @File    : 15.绘制函数图像.py
# @Description : 添加描述
import matplotlib.pyplot as plt
import math


plt.figure()
x = [i*0.001 for i in range(-1000,1000)]
y = [-math.log(1-i,10) for i in x]
plt.plot(x,y)
plt.show()