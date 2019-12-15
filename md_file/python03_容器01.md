# 朱李延
`2019-10-20，地点：上海浦东图书馆。所有光鲜亮丽的背后，必然有着常人未曾预料的艰辛和坚持。` 

<br> 

# Python_day03 容器
- 容器通用操作
- 字符串
- 列表
<br> 

# 一、容器通用操作
## 定义： 
"容器" 这两个字很少被 Python 技术文章提起。一看到“容器”，大家想到的多是那头蓝色小鲸鱼：Docker。这里的 "容器" 是 Python 中的一个抽象概念，是对专门用来装其他对象的数据类型的统称。

 `ps: 容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用 in；not in关键字判断元素是否包含在容器中。`
 <br> 
 
 ## 数学运算： 
 
|运算描述|运算符号  |
|--|--|
|  拼接两个容器|+  |
|重复生成容器元素|*|
|用原容器的拼接并重新绑定|+=| 
|用原容器生成重复的元素并重新绑定|*=| 
|依次比较两个容器中的元素|>, <, >=, <=, ==, !=|


 <br> 
 
## 成员运算：
用于判断该元素是否存在于容器内，返回结果为 bool 值。 
| 描述 |成员运算符  |
|--|--|
|  存在|in  |
|不存在|not in| 

```python
'''成员运算'''

# 以字符串为例
value = "a" 
str_01 = "abcd" 

value in str_01 			# True 
value not in str_01 		# False 
```

<br> 

## 索引：
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字`索引`，第一个索引值为 0，第二个索引值为 1，依此类推；最后一个元素的索引值为 -1。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191020134209133.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDgxNDY3Mg==,size_16,color_FFFFFF,t_70)
```python
'''索引''' 

# 查看索引值对应的元素
str_02 = "PYTHON"
print(str_02[0]) 			# P
print(str_02[1])			# Y
print(str_02[-1])			# N 
```

<br> 

## 切片 ：
在容器中获取指定长度的元素。格式：[start : end : step]
1. start：起始索引下标 
2. end：结束索引下标
3. step：步长，正数表示“从左往右”取值，负数表示“从右往左”取值。当step省略时，默认为1

```python
'''切片''' 

str_03 = "PYTHON" 
print(str_03[0:3])			# PYT 
print(str_03[0:-1])			# PYTHO 
print(str_03[-1:])			# N 
print(str_03[0:-1:1]) 		# PYTHO
print(str_03[0:-1:2])		# PTO 
print(str_03[::-1])			# NOHTYP
print(str_03[-1::-2])		# NHY
print(str_03[::])			# PYTHON
```

<br> 

## 内建函数：
|函数功能描述|函数名  |
|--|--|
|  返回容器长度|len(容器)  |
|返回容器内所有数值之和(容器内元素必须为数值)| sum(容器)|
|返回容器中最大的元素|max(容器) | 
|返回容器中最小的元素| min(容器) | 

```python
'''内建函数''' 

# 字符串
str_04 = "hello world" 
print(len(str_04)) 			# 11

# 列表
list_01 = [1, 2, 3, 4, 5]
print(len(list_01))			# 5
print(sum(list_01))			# 15 
print(max(list_01)) 		# 5
print(min(list_01)) 		# 1 
```

<br> 




# 二、字符串 
## 定义：
字符串就是一系列字符。在Python中，用引号括起来的都是字符串。由一系列字符组成的不可变序列容器；存储的是`字符串编码值`。 

## 编码和解码： 
**`1. 首先我们需要弄清楚一个概念`**
- 在计算机中，所有的数据在存储和运算时都要使用二进制数表示（因为计算机用高电平和低电平分别表示1和0），例如，像a、b、c、d这样的52个字母（包括大写）以及0、1等数字还有一些常用的符号（例如*、#、@等）在计算机中存储时也要使用二进制数来表示，大家如果要想互相通信而不造成混乱，那么大家就必须使用相同的编码规则，于是美国有关的标准化组织就出台了ASCII编码（美国信息交换标准代码），统一规定了上述常用符号用哪些二进制数来表示；`ps：终端可使用 man ascii 查看；总共为128个字符编码。`

**`2. 中文编码`** 
- 众所周知，计算机是老美发明的，也制定了自己的ASCII编码；但是全球不是所有人都会英文，以中国为例；计算机在中国使用就必须拥有中国自己的中文编码：<br>
-- GB2312编码：1981年5月1日发布的简体中文汉字编码国家标准。GB2312对汉字采用双字节编码，收录7445个图形字符，其中包括6763个汉字。 <br>
-- BIG5编码：台湾地区繁体中文标准字符集，采用双字节编码，共收录13053个中文字，1984年实施。<br>
-- GBK编码：1995年12月发布的汉字编码国家标准，是对GB2312编码的扩充，对汉字采用双字节编码。GBK字符集共收录21003个汉字，包含国家标准GB13000-1中的全部中日韩汉字，和BIG5编码中的所有汉字。<br> 
-- GB18030编码：2000年3月17日发布的汉字编码国家标准，是对GBK编码的扩充，覆盖中文、日文、朝鲜语和中国少数民族文字，其中收录27484个汉字。GB18030字符集采用单字节、双字节和四字节三种方式对字符编码。兼容GBK和GB2312字符集。

**`3. unicode编码`**
- Unicode（统一码、万国码、单一码）是计算机科学领域里的一项业界标准，包括字符集、编码方案等。为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码，以满足跨语言、跨平台进行文本转换、处理的要求。Unicode 编码共有三种具体实现，分别为utf-8,utf-16,utf-32，其中utf-8占用一到四个字节，utf-16占用二或四个字节，utf-32占用四个字节。

**`4. 相关概念`** 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191026105025461.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDgxNDY3Mg==,size_16,color_FFFFFF,t_70)
- 字节byte：计算机及存储的最小单位，一字节等于8位bit。
- 字符：单个的数字，文字，符号。
- 字符集(码表)：存储字符与二进制序列的对应关系。
- 编码：将字符转换为对应的二进制序列的过程。
- 解码：将二进制序列转换为对应的字符的过程。

**`5. 编码方式`**
- ASCII编码：包含英文、数字等字符；每个字符 1 个字节。
- GBK编码：兼容 ASCII，包含 21003 个中文；每个英文 1 个字节，汉字两个字节。
- Unicode字符集：国际统一编码；旧字符集每个字符 2 个字节，新字符集每个字符 4 字节。
- UTF-8编码：Unicode的存储和传输方式；英文 1 个字节，中文 3 个字节。
<br> 


## 字符串相关函数： 
|功能描述|函数|
|--|--|
|返回字符串的Unicode编码|ord(字符串)|
|返回对应的字符串|chr(Unicode编码)|
|将字符串首个单词改为大写|字符串.title()|
|将字符串改为大写|字符串.upper()|
|将字符串改为小写|字符串.lower()|
|去除字符串开头空白|字符串.rstrip()|
|去除字符串末尾空白|字符串.lstrip()|
|去除字符空白|字符串.strip()| 

```python
'''字符串相关函数''' 

str_01 = '你'
print(ord(str_01))			# 20320 

str_02 = '24310'
print(chr(int(str_02)))		# 延

str_03 = 'i love python' 
print(str_03.title()) 		# I Love Python 

str_04 = 'PYthon' 
print(str_04.upper()) 		# PYTHON
print(str_04.lower())		# python

str_05 = '    Shanghai    ' 
str_05.rstrip() 			# '    Shanghai'
str_05.lstrip()				# 'Shanghai    '
str_05.strip()				# 'Shanghai'     
```

<br> 

## 字符串使用方式：
 
1. 单引号和双引号：
单引号内的双引号不算结束符；双引号中的单引号不算结束符。

```python
'''字符串单引和双引''' 

str_01 = 'python' 
str_02 = "python" 
print(str_01) 				# python
print(str_02) 				# python 

str_03 = '"py"thon'
str_04 = "py'thon'" 
print(str_03) 				# "py"thon 
print(str_04) 				# py'thon' 

```

2. 三引号：
可以包含单引号和双引号，可见即所得，常常作为文档注释。 

```python
'''字符串三引号''' 

str_05 = """python""" 
str_06 = '''python''' 
print(str_05) 				# python 
print(str_06) 				# python 

str_07 = '''py'th'on'''		
str_08 = """pyth"o"n"""
print(str_07) 				# py'th'on 
print(str_08) 				# pyth"o"n 


str_09 = ''''hello' "world"''' 
print(str_09) 				# 'hello' "world" 

str_10 = '''hello 
world''' 
print(str_10) 				# hello 
							# world 
```

3. 转义符： 
可以改变原有字符含义的特殊字符。
 
|功能描述|转义符号  |
|--|--|
| 显示一个单引号 |\ '  |
|显示一个双引号| \ "| 
|显示一个反斜符号|\ \|
|换行| \n| 
|水平制表符|\t| 
|空字符串| \0| 



```python
'''字符串转义符''' 

str_11 = "I\'m is Zhuliyan!"
print(str_11) 				# I'm is Zhuliyan

str_12 = "\"hello world\""
print(str_12) 				# "hello world" 

str_13 = "C:\\Python\\Scripts"
print(str_13) 				# C:\Python\Scripts 

str_14 = "My name is: \nZhuliyan"
print(str_14) 				# My name is: 
    						# Zhuliyan 
    						
str_15 = "I love China"
print(str_15)				# I love China 
str_16 = "\tI love China"
print(str_16) 				# 		I love China 

str_17 = "I\0love\0python"
print(str_17)				# Ilovepython 
```
<br> 

# 三、列表
## 定义： 
由一系列变量组成的可变序列容器，列表是最常用的Python数据类型，一个方括号内的逗号分隔值组成。
<br> 

## 定义列表： 
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。 

```python
'''定义列表''' 

# 定义空列表
list_01 = []

list_02 = [1, 2, 3]

list_03 = ["hello", "world"] 

list_04 = [1, 2, 'a', 'b'] 

str_01 = 'hello' 
list_05 = list(str_01) 
print(list_05) 					# ['h', 'e', 'l', 'l', 'o']
```
<br> 


## 列表操作： 
|描述| 相关函数 |
|--|--|
| 定义列表 |list(seq)  |
|添加元素|insert(index, obj)，append()|
|删除元素|remove(obj)，pop(index=-1)，del(list[index])| 
|获取列表中最大，最小元素|max(list_03)，min(list_04)|
|获取列表长度|len(list_05)
|统计列表中元素出现的次数|count(obj)| 
|追加序列| extend(seq)| 
|查找列表中第一个元素的索引值| index(obj) | 
|反向列表| reverse() | 

```python
'''列表操作''' 

# 定义列表
str_01 = '1234ABCD' 
list_01 = list(str_01) 
print(list_01) 					# ['1', '2', '3', '4', 'A', 'B', 'C', 'D']


# 添加元素
list_02 = ['A', 'B', 'C']
list_02.insert(1,1)
print(list_02) 					# ['A', 1, 'B', 'C']

list_02.append("hello")
print(list_02)					# ['A', 1, 'B', 'C', 'hello'] 

str_02 = '你好'
list_02.extend(str_02)
print(list_02) 					# ['A', 1, 'B', 'C', 'hello', '你', '好']


# 删除元素
list_03 = list("hello".upper())
# 删除第一次出现的元素
list_03.remove('L')				
print(list_03)					# ['H','E','L','O']

# 删除指定索引元素，默认删除最后一个
list_03.pop(0)					
print(list_03)					# ['E', 'L', 'O']
list_03.pop()					
print(list_03)					# ['E', 'L']


# 统计元素出现的次数
list_04 = list('ABCACC')
list_04.count('C')				# 3 
list_04.count('A')				# 2 


# 查找元素的索引
list_05 = list('world') 
list_05.index('o')				# 1 


# 反向列表
list_06 = list('python'.upper())
list_06.reverse() 
print(list_06)					# ['N', 'O', 'H', 'T', 'Y', 'P']
```

<br> 

> 感谢阅读，此博客为学习笔记，如有理解不对还望各位同学指正，本人邮箱：`Julian_cn@126.com`
