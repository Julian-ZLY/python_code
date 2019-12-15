# 朱李延 
`2019-10-27，地点：上海浦东图书馆。渴望而不可及，还需努力。`
<br> 

# Python_day04 容器
- 元组
- 字典
- 集合

<br> 
<br> 

# 一、元组
## 定义： 
由一些列变量组成不可变的序列容器。Python的元组与列表类似，不同之处在于元组的元素不能修改。
<br> 

## 定义元组： 
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。


```python
'''定义元组''' 

# 创建空元组
tuple_01 = () 
tuple_02 = tuple() 
print(tuple_01)					# () 
print(tuple_02) 				# () 

# 创建元组
tuple_03 = (1,) 				# 创建单个元素的元组需在元素后加逗号
tuple_04 = 'A', 'B', 'C' 
print(tuple_03) 				# (1,) 
print(tuple_04) 				# ('A', 'B', 'C') 

# 使用可迭代对象创建元组
tuple_05 = tuple('HELLO')
print(tuple_05)					# ('H', 'E', 'L', 'L', 'O') 
```
<br> 

## 元组操作：
1. 元组的运算：与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

```python
'''元组的运算''' 

# 元组相加
tuple_01 = 1, 2, 
tuple_02 = ('A', 'B') 
tuple_03 = tuple_01 + tuple_02 
print(tuple_03) 				# (1, 2, 'A', 'B') 


# 元组相乘
tuple_04 = ('hello',) 
tuple_05 = tuple_04 * 3 
print(tuple_05)					# ('hello', 'hello', 'hello')
```

2. 元组的截取：因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素。

```python
'''元组的截取''' 

# 元组索引
tuple_06 = tuple('python'.upper())
print(tuple_06[0])				# P 
print(tuple_06[:]) 				# ('P', 'Y', 'T', 'H', 'O', 'N')
```

3. 删除元组：元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组。 

```python
'''删除元组''' 

tuple_07 = tuple('ABC') 
print(tuple_07)				# ('A', 'B', 'C') 

del tuple_07 
print(tuple_07) 			# NameError: name 'tuple_07' is not defined
```

<br> 

# 二、字典
## 定义： 
字典是另一种可变容器模型，且可存储任意类型对象。

## 定义字典： 
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中。

```python
'''定义字典''' 

# 定义空字典
dict_01 = dict() 
print(dict_01)			# {} 


dict_02 = {'name': 'Julian', 'age': '23', 'sex': 'man'}
print(dict_02)			# {'name': 'Julian', 'age': '23', 'sex': 'man'}


dict_03 = {'list_01': [1,2,3], 'tuple_01': ('a', 'b')}
print(dict_03) 			# {'list_01': [1, 2, 3], 'tuple_01': ('a', 'b')}
```
`ps : 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。`


## 字典操作：
1. 访问字典里的值

```python
'''访问字典中的值''' 

dict_04 = {'L': ['P', 'Y', 'T', 'H', 'O', 'N'], 'T': ('H', 'E', 'L', 'L', 'O'), 'D': {'D1': 'value_01'}}
print(dict_04) 				# {'L': ['P', 'Y', 'T', 'H', 'O', 'N'], 'T': ('H', 'E', 'L', 'L', 'O'), 'D': {'D1': 'value_01'}}

print(dict_04['T'])			# ('H', 'E', 'L', 'L', 'O')
print(dict_04['L'][0])		# P 
print(dict_04['D']) 		# {'D1': 'value_01'}
# 获取字典中，字典值
print(dict_04['D']['D1'])	# value_01

# 如字典中没有对应的键，则会报错
print(dict_04['A'])			# KeyError : 'A' 
```
2. 修改字典

```python
'''修改字典''' 

dict_05 = {'A':'hello', 'B': 'world'}
print(dict_05)				# {'A':'hello', 'B': 'world'}

# 修改字典中该键的值
dict_05['A'] = 'HELLO'	
print(dict_05)				# {'A':'HELLO', 'B':'world'}

# 增加键值
dict_05['C'] = ['I', 'Love', 'Python']
print(dict_05)				# {'A': 'HELLO', 'B': 'world', 'C': ['I', 'Love', 'Python']}
```
3. 删除操作
```python 
'''字典删除操作''' 

dict_06 = {'a':'你好', 'b':'世界', 'c':'要被删除了'}

# 删除键值
del dict_06['c']
print(dict_06)			# {'a':'你好', 'b':'世界'} 

# 清空字典中的数据
dict_06.clear()
print(dict_06)			# {} 

# 删除字典
del dict_06
print(dict_06)			# NameError: name 'dict_06' is not defined
```
 
<br> 

# 三、集合
## 定义： 
集合（set）是一个无序的不重复元素序列。

## 定义集合： 
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

```python
'''集合创建'''

# 创建空集合
set_01 = set() 
print(set_01) 			# set() 

set_02 = set('hello')
print(set_02) 			# {'h', 'o', 'l', 'e'}

set_03 = {'a', 1, 2} 
print(set_03)			# {1, 2, 'a'}
```
`ps : 集合内的元素不可重复。`

## 集合操作
1. 添加元素

```python
'''删除集合元素''' 

set_04 = set('ABCD')
print(set_04) 			# {'B', 'A', 'D', 'C'}

# 删除指定元素，如元素不存在则报错
set_04.remove('B')		
print(set_04)			# {'A', 'D', 'C'} 

# 删除指定元素，如果元素不存在也不会报错
set_04.discard('B')
print(set_04)			# {'A', 'D', 'C'} 

# 随机删除集合内元素，返回被删除元素
set_04.pop() 			# 'A'
print(set_04)			# {'C', 'D'}
```

2. 添加元素
```python
'''添加集合元素''' 

set_05 = set('ABC')
print(set_05)			# {'A', 'B', 'C'}

# 添加单个元素
set_05.add('D')
print(set_05)			# {'B', 'A', 'D', 'C'}

# 添加多个元素
set_05.update({1,2})
print(set_05)			# {'D', 'C', 'A', 1, 2, 'B'}
```

3. 集合运算

|描述| 相关符号|
|--|--|
| 交集| set_01 & set_02|
| 并集| set_01 \| set_02| 
|差集| set_01 - set_02
|对称| set_01 ^ set_02| 

```python
'''集合运算''' 

list_01 = ['a', 'b', 'C']
list_02 = ['A', 'B', 'C']
set_06 = set(list_01)
set_07 = set(list_02)

# 集合交集
set_06 & set_07 			# {'C'}

# 集合并集
set_06 | set_07 			# {'A', 'B', 'C', 'a', 'b'}

# 集合差集
set_06 - set_07 			# {'a', 'b'}
set_07 - set_06				# {'A', 'B'}

# 集合对称运算
set_06 ^ set_07 			# {'B', 'A', 'b', 'a'}
```
> 感谢阅读，此博客为学习笔记，如有理解不对的地方还望各位同学指正，本人邮箱：`Julian_cn@126.com`





