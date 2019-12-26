# -*- coding:utf-8 -*- 

import ssl 
import urllib.request
import re


url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fromtitle=%E7%88%AC%E8%99%AB&fromid=22046949&fr=aladdin"
# context = ssl._create_default_https_context()
context = ssl._create_unverified_context()


html = urllib.request.urlopen(url, context=context).read()
# print(source_web.decode('utf-8'))

# 字节 转换 字符串
str_html = str(html, encoding='utf-8')

# print(type(html))
# print(str_html, end='', sep='')

pre = re.compile('>(.*?)<')
text = ''.join(pre.findall(str_html)).split()

for i in text:
    print(i)

# print(text)

