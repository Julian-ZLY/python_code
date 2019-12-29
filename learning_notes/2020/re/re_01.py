"""正则表达式""" 

import re


# 普通字符
str_01 = "I'm is Julian"
result = re.findall('Julian', str_01)
print(result)

# 或
str_02 = 'abcdefg'
result = re.findall('ab|cd', str_02) 
print(result)

# 匹配单个字符
str_03 = '张三丰, 张四丰, 张五丰, 张六风'
result = re.findall('张.丰', str_03)
print(result)

# 匹配字符集
str_04 = 'I love python !'
result_01 = re.findall('[abcde]', str_04)
result_02 = re.findall('[a-z]', str_04)
print(result_01)
print(result_02)

# 匹配字符集取反
str_05 = 'I love python !'
result = re.findall('[^a-z]', str_05)
print(result)

# 匹配字符串开始位置
str_06 = 'Julian, hello'
result = re.findall('^Julian', str_06)
print(result)

# 匹配字符串结束位置 $
str_07 = 'Hi, Julian'
result = re.findall('Julian$', str_07)
print(result)

print('\n', '*' * 20, '\n')

# 匹配字符重复 *
str_08 = 'wooooooo ~~ w'
result = re.findall('wo*', str_08)
print(result)

result = re.findall('wo+', str_08)
print(result)

str_09 = 'age:24, score:-60, 00087'
result = re.findall('-?[0-9]+', str_09)
print(result)

# 匹配前面的字符出现 n 次
str_10 = 'tel: 13911122222'
result = re.findall('1[0-9]{10}', str_10)
print(result)

# 匹配前面的字符出现 m-n 次
str_11 = 'qq:11345632, 887654'
result = re.findall('[1-9][0-9]{4,11}', str_11)
print(result)

#

print('\n', '*' * 20, '\n')




