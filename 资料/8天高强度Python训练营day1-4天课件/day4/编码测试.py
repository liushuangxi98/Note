# -*- encoding:gbk -*-

s = "路飞"
print(s)  # unicode

# py2 test
gbk_2_unicode = s.encode("gbk")
print(gbk_2_unicode,type(gbk_2_unicode))


# utf-8 --> unicode
# gbk ---> unicode