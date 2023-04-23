import matplotlib.pyplot as plt

# 	1.创建画布
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(8,5),dpi=100)

# 	2.建立数据
x = [2000+i for i in range(10)]
y = [1658,1687,894,1568,2321,1444,2311,4546,5555,6879]
y2 = [2658,2687,1894,1598,3321,1444,3311,4546,5155,6279]

# 	3.绘制图像
# plt.plot(x,y, label = '北京', color = 'g')  # 折线图
# plt.plot(x,y2, label = '上海', color = 'r')  # 折线图
plt.bar(x, y, width=0.8, align='center',color=['g'])  # 柱状图
plt.xticks(x, [f'{i}year' for i in range(10)])
plt.legend(loc='best')
plt.title('GDP时间增长', )
plt.show()

