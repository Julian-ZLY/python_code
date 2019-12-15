 
# python06 小结

@(python学习笔记)


# Julian

`地点：上海浦东图书馆。给你们讲一个秘密，我好像有点喜欢ta。`

# Python06 小结
- 变量：内存概念，内存地址，内存图
- 列表：列表推导式，内存图，列表拷贝
- 元组：内存图，概念，生成器推导式
- 字典：内存图，字典推导式
- 集合：内存图，集合运算

<br> 

# 变量
1. 内存概念
![Alt text](./1573976717631.png)
内存是计算机中重要的部件之一，它是外存与CPU进行沟通的桥梁。计算机中所有程序的运行都是在内存中进行的，因此内存的性能对计算机的影响非常大。内存(Memory)也被称为`内存储器`和[主存储器](https://baike.baidu.com/item/%E5%86%85%E5%AD%98/103614?fromtitle=%E4%B8%BB%E5%AD%98&fromid=5688989)。
`举个栗子：现在是秋天，树上的柿子熟了，我需要爬上树上摘柿子；如果我每上一次树仅摘下一个柿子，第二次也是一样，这样效率极低，并且很傻；后来我拿一个篮子上树，篮子的容量大小取决于我上树一次性能摘取多少柿子，这样大大的提高了工作效率；而篮子作为一个中间介质就可以比作计算机中的内存。`

2. 内存地址
说明：
- 
从硬件角度来看，内存就是一个内存条。 
- 从软件角度来看，每一个程序运行后，操作系统会分配一块空间给该程序；也就是正在运行程序的数据，一般操作系统会将这些数据存储在内存中。
- 为了能够让CPU精确操作每一处内存，所有的内存都有编号；而这些编号就称为`内存地址。`

<br> 

3. 内存图
![Alt text](./1573982267944.png)
- 变量值 ‘Julian' 在内存中绑定的内存地址为 0x901 ；变量名 name 在内存中绑定的内存地址为 0x101；变量 name 指向的是变量值 ’Julian‘ 绑定的内存地址。
- 变量名 cp_name 则是指向 name 绑定的内存地址。
- 变量名 name 指向 None，解除绑定；None 可以理解为什么也没有。

<br> 

# 列表
1. 列表 vs 字符串
```python
'''字符串转换为列表''' 

# 字符串转换为列表 split() 函数
str_01 = 'I love Python' 
new_str_01 = str_01.split() 
print(str_01) 				# I love Python			
print(new_str_01) 			# ['I', 'love', 'Python'] 

# 字符串为特殊路径传入关键字
str_02 = '/home/ubuntu/data' 
print(str_02.split('/'))	# ['', 'home', 'ubuntu', 'data'] 


# 列表转换为字符串 join() 函数
list_01 = ['I', 'am', 'Julian'] 
str_03 = ' '.join(list_01)
print(str_03) 				# I am Julian 

# 指定关键字转换
list_02 = ['', 'home', 'ubuntu', 'data'] 
str_04 = '/'.join(list_02) 
print(str_04) 				# /home/ubuntu/data 
```
说明： 
- `split()`函数使用对象为`字符串`，返回的是一个新的对象，不改变原有的值； 
- `split()`函数默认`空字符`转换；比如：`'\n'`,`'\t'`等；
- 如需其他特殊字符直接传入函数中即可；`str.split('关键字')`。 
<br> 
-  `join()`函数使用对象为`列表`，返回对象是一个新的对象，不改变原有的值； 
-  `join()`函数使用方式为：`'关键字'.join(list)`； 

<br>  


2. 列表推导式
```python
'''列表推导式''' 

# 获取 1 ~ 10 之间的奇数 
list_odd_num = []
for i in range(11): 
    if i % 2 == 1: 
        list_odd_num.append(i)
        
print(list_odd_num)			# [1, 3, 5, 7, 9] 

# 列表推导式 
odd_num = [ i for i in range(11) if i % 2 == 1] 
print(odd_num)				# [1, 3, 5, 7, 9]   
```
3. 列表拷贝内存图
```python  
'''列表拷贝''' 

list_name = ['Tom', 'Jerry', 'Julian', 'Jobs'] 
copy_list = list_name[:]  
new_list_name = list_name  

# 修改原列表的元素 
list_name[2] = '小伙计' 
print(list_name) 			# ['Tom', 'Jerry', '小伙计', 'Jobs']
print(copy_list)  			# ['Tom', 'Jerry', 'Julian', 'Jobs']
print(new_list_name) 		# ['Tom', 'Jerry', '小伙计', 'Jobs']

# 使用 id() 函数返回对象的内存地址
print(id(list_name)) 		# 4344439944 
print(id(copy_list)) 		# 4344439560 	
print(id(new_list_name))	# 4344439944 
```
![Alt text](./1575186423747.png)
内存图说明： 
- 定义列表则是在内存中开辟一个空间； 
- `copy_list = list_name[:]`；拷贝一份列表绑定到新的变量，和原列表无关； 
- `new_list_name = list_name`；新列表指向原列表绑定的内存地址； 
- `list_name[2] = '小伙计'`；修改列表中的元素，原列表数据改变则该内存地址指向的元素也发生改变； 
- 可以使用`id()`函数打印对象的内存地址；`id(list_name)`一定等于`id(new_list_name)`。 

<br> 

# 元组
1. 内存图

![Alt text](./1575212624016.png)
```python 
'''元组 vs 列表''' 

list_01 = [1, 2, 3, 4] 
tuple_01 = (1, 2, 3, 4) 

# 显示占用内存使用量
print(list_01.__sizeof__()) 		# 72 
print(tuple_01.__sizeof__())  		# 56 
```
说明： 
- 元组和列表不同，元组存储时会有预留空间； 
- 由一系列不重复的，不可变类型变量组成的可变，散列，容器； 
- 元组比列表占用资源要小。

<br> 
 
2. 生成器推导式
```python
'''生成器推导式''' 

tuple_num = (x for x in range(10) if x % 2 == 0) 
type(tuple_num)						# <class 'generator'>
list(tuple_num)						# [0, 2, 4, 6, 8] 
list(tuple_num)						# [] 


tuple_num = (x for x in range(10) if x % 2 == 1) 
print(next(tuple_num)) 				# 1 
print(next(tuple_num)) 				# 3 
print(tuple_num.__next__()) 		# 5 
print(tuple_num.__next__()) 		# 7
print(tuple_num.__nest__())			# 9 
print(tuple_num.__next__()) 		# Error 
```
说明： 
- 生成器推导式，返回的是一个可迭代对象；
- 实现延迟计算，省内存，惰性机制，需要使用时才返回数据； 
- 不能反复，只能向下执行，是一次性取值； 
- 生成器可使用`next()`和`__next_()`调用其中元素，直至到最后返回迭代停止。 

<br> 

# 字典
1. 内存图
![Alt text](./1575215221849.png)
说明： 
- 由一系列键值对组成的可变散列容器；
- 存储结构和元组类似，每条数据存储无先后顺序，会有预留空间； 
- 键必须惟一且不可变，值没有限制；
- 优点：查找速度块；缺点：占用内存多。

<br> 
 
2. 字典推导式
```python
'''字典推导式''' 

name = ['Tom', 'Jerry', 'Julian'] 
sign = ['白羊座', '双鱼座', '处女座']

dict_info = {n : s for n , s in zip(name, sign)} 
print(dict_info)		# {'Tom': '白羊座', 'Jerry': '双鱼座', 'Julian': '处女座'}
```
<br> 

# 集合
1. 内存图
![Alt text](./1575216872795.png)
说明： 
- 集合内存的值为不可变元素，无序存储，同元组和字典一样，会有预留空间。 

<br> 

2. 集合运算
运算：定义 `set_01` 和 `set_02` 
- 
并集：计算两个集合的并集，同时属于二者元素的集合。 
- 交集：是所有同时属于两个集合的元素集合。
- 差集：是所有属于`set_01`但不属于`set_02`的元素集合。
- 对称集：是所有属于两个集合但不属于二者共有部分的集合。 

<br> 

3. 集合推导式   
```python
'''集合推导式''' 

str_list = ['SQL', 'PYTHON', 'SQL', 'python'] 

set_01 = {x for x in str_list} 
print(set_01)		# {'python', 'PYTHON', 'SQL'} 
```

> 感谢阅读，此博客为学习笔记，如有理解不对的地方还望各位同学指正，本人邮箱：`Julian_cn@126.com`
