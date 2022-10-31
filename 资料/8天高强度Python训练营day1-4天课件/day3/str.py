# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

a = "Alex li 金角大王"

print(a.center(50,"-"))  # 居中字符串并填充左右 output : --------------------Alex 金角大王---------------------

print(a.endswith("王"))  # False 判断结尾
print(a.startswith("Ale"))  # Ture 判断开头

print(a.count("l",0,4))  # 从0到4查找l出现的次数
print(a.find("i"))  # 字符查找，返回-1代表没找到，如果找到了，就返回所查字符的索引

print(a.isdigit())  # 判断是否是整数 False
print("22".isdigit())  # 判断是否是整数 Ture

l = ["alex","black girl","peiqi"]
print("-".join(l)) # 拼接字符串， alex-black girl-peiqi

print(a.replace("l","M" ,1)) # 字符串替换，l替换成M，只替换一次 output: AMex li 金角大王
print(a.strip())  # 去掉字符串a中的空格
print(a.split("l",1))  # 字符串分割成列表 output: ['A', 'ex li 金角大王']
