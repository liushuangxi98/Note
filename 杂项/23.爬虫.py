import re
import requests

url = 'https://mp.weixin.qq.com/s?__biz=MzU5MDYwMDA0OQ==&mid=2247485995&idx=3&sn=44cf46cc595d45ab1f991fd799a3559b&chksm=fe3a8835c94d012399e00624aa2f64723646df6eb7d799b5f891df3b515a2ac654c1d3476c12&scene=27'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
header = {'User-agent': agent}
response = requests.get(url, headers=header)
a = response.text
s = re.findall(re.compile('[\u4e00-\u9fff]+'), a)
print(s)
