
# 朱李延 
`2019-10-14，地点上海浦东新区。只为能遇见更好的那个自己，其他的都交给时间。`


<br>

# Python_day02 Python数据类型和运算
- Python的数据类型
- Python运算符
<br>
# 一、Python的数据类型

## 说明：
变量没有类型，关联的对象有类型，可以通过`type()`函数，判断对象的类型；例如:

```python
'''type函数使用''' 

str_01 = '我是字符串'
num_01 = 100
list_01 = [10,20,30]

print(type(str_01))			# <type 'str'>
print(type(num_01))			# <type 'int'> 
print(type(list_01))		# <type 'list'> 
```
<br>

## 数据类型
|数据类型| 代表关键字 |
|--|--|
| 空 |None  |
|整型|int|
|浮点型|float|
|字符串|str|
|布尔|bool|
|负数|complex|
<br>
 
## 解释
1. 空：表示不存在的特殊对象，作用用来占位；例如：`var = None`

```python
'''数据类型None'''

num_01 = 100 
print(num_01)		# 100 

num_01 = None
print(num_01)		# 释放掉资源，解除绑定

num_02 = None  		# 用作占位
```

2.  整型：表示整数，包含整数，负数和0。

```python
'''数据类型int'''

# 十进制
print(1, 2, 3, 4, 5, 6) 		# (1, 2, 3, 4, 5, 6)

# 二进制表示：0b 逢二进一
print(0b0, 0b1, 0b10, 0b11)		# (0, 1, 2, 3)

# 八进制表示：0o 逢八进一
print(0o1, 0o4, 0o10, 0o14)		# (1, 4, 8, 12) 

# 十六进制表示：0x 逢十六进一，要注意的是10-16用英文字母a-f表示
print(0x1, 0x5, 0xa, 0xf, 0x11)	# (1, 5, 10, 15, 17)
```

3. 浮点型：表示小数，包含整数，负数和0.0。

```python 
'''数据类型float''' 

print(3.14)				# 3.14

print(3.14e2)			# 3.14 --> 314.0

print(3.14e-2)			# 3.14 --> 0.0314
```

4. 字符串：用来记录文本信息；例如：`str_01 = “今年是：2019年”`
```python
'''数据类型int''' 

# 单引号
str_01 = '学习Python' 
print(str_01)

# 双引号
str_02 = "我爱Python"
print(str_02)

# 三单引
str_03 = '''I love Python'''
print(str_03)

# 三双引号
str_04 = """I love China"""
print(str_03)
```
5. 布尔值：True表示真，False表示假。

```python
'''数据类型bool'''

print(True)		# True代表真，表示成立

print(False)	# False代表假，表示不成立
```

6. 负数：由实部和虚部组成的数字，虚部以 J 或 j 结尾；字面值：6j 或 5 +3J。`ps：负数前阶段用的非常少，在做大数据和人工智能的算法会用到，现在作为一个了解，所以不必深究。`

<br> 

## 数据类型转换

|转换数据类型  | 表示方法 |
|--|--|
| 转换为整型 |int(数据)  |
|转换为浮点型| float(数据)| 
|转换为字符串| str(数据)
|转换为bool|bool(数据) 

```python
'''数据类型转换'''

# 定义字符串变量
str_01 = "10"
print(type(str_01)) 		# <class 'str'> 

# 将字符串转换为整数
num_01 = int(str_01) 
print(type(num_01)) 		# <class 'int'> 


# 定义数字变量
num_02 = 100 
print(type(num_02)) 		# <class 'int'> 

# 将整数转换为浮点型
float_01 = float(num_01) 
print(type(float_01)) 		# <class 'float'> 


# 转换为bool值
str_02 = "hello" 
num_03 = 0 

print(bool(str_02)) 		# True 
print(bool(num_03)) 		# False 
```
`ps:bool()函数内的数据除：0，None，”“，0.0；都为True`

<br>


# 二、Python运算符
## 算数运算符：
|描述|运算符号|
|--|--|
|加| +| 
|减|-|
|乘|*|
|除|/|
|底板除|//|
|取余|%| 
|幂运算|**| 

```python
'''算数运算''' 

# 整数相加
num_01 = 10 
num_02 = 1 
num_03 = num_01 + num_02 
print(num_03) 					# 11 

# 字符串相加，也称为拼接
str_01 = "hello" 
str_02 = "world" 
print(str_01 + str_02) 			# helloworld 

# 整数相减
print(num_03 - num_02) 			# 10 

# 整数相乘
num_04 = 2 
print(num_03 * num_04) 			# 22 

# 整数相除，结果为float类型
num_05 = 5 
print(num_01 / num_05)			# 2.0 

# 整数底板除，保留整数位，余数
num_06 = 3 
print(num_01 // num_06) 		# 3 

# 整数取余运算，保留余数，用来判定 除数 能否被 被除数 整除
num_07 = 4 
num_08 = 5 
print(num_01 % num_07) 			# 2 
print(num_01 % num_08) 			# 0 
# 判断能否被整除，返回bool值
print(num_01 % num_08 == 0) 	# True 

# 整数幂运算
num_09 = 3 
print(num_01 ** num_09) 		# 10000
```

<br> 

## 增强运算符：
|描述|运算符号|
|--|--|
|加等|+=|
|减等|-=|
|乘等|*=|
|除等|/=| 
|底板除等|//=|
|取余等|%=|
|幂等|**=|


```python
'''增强运算''' 

# 加等于
num_01 = 1 
num_01 += 1 
print(num_01) 			# 2 

# 减等于
num_02 = 10 
num_02 -= num_01 
print(num_02) 			# 8 

# 乘等于
num_03 = 3 
num_03 *= 3 
print(num_03) 			# 9 

# 除等于
num_04 = 4 
num_04 /= 2 
print(num_04)			# 2.0 

# 底板除等于
num_05 = 10 
num_05 //= 3 
print(num_05) 			# 3 

# 取余等于
num_06 = 10 
num_06 %= 2 
print(num_06) 			# 0 

# 幂等于
num_07 = 7 
num_07 **= 3 
print(num_07) 			# 343 
```
<br> 


## 比较运算符：
|描述|运算符号  |
|--|--|
|  大于|>  |
|小于|<| 
|等于|==|
|大于等于|>=| 
|小于等于|<=| 
|不等|!=| 
`ps:用于比较两个整数，返回bool值，也可以比较字符串，感兴趣的同学自行百度，这个不在过多的演示。`

<br> 

## 逻辑运算符： 
|描述| 关键字 |
|--|--|
| 与 | and |
|或|or|
|取反|not|

```python
'''逻辑运算符''' 

# and表示并且；一假俱假 
result_01 = True and False 
result_02 = False and True 
result_03 = True and True 
result_04 = False and False 

print(result_01) 			# False 
print(result_02) 			# False 
print(result_03) 			# True 
print(result_04) 			# False 


# or表示或者；一真俱真
result_05 = True or False 
result_06 = False or True 
result_07 = True or True 
result_08 = False or False 

print(result_05) 			# True 
print(result_06) 			# True 
print(result_07) 			# True  
print(result_08) 			# False


# not表示取反
result_09 = True 
result_10 = not result_09 
print(result_10) 			# False 
```
`ps:比较两个bool值的关系；比如：限制飞机水平范围，如果到了最左边 and 还想向左移动 or 到了最右边 and 还想向右边移动`

<br> 


## 身份运算符： 
|描述| 关键字 |
|--|--|
| 是 | is |
|不是|is not| 

```python
'''身份运算符''' 

var_01 = 100 
var_02 = 200 
var_03 = var_01 

# id 函数返回变量所关联的对象地址 
print(id(var_01), id(var_02), id(var_03)) 	# 4304852448 4304855648 4304852448
print(var_01 is var_02) 					# False 
print(var_03 is not var_02)					# True 
print(var_03 is var_01) 					# True 


num_01 = 800 
num_02 = 800 
print(num_01 is num_02)  					# True 
```
<br>

## 运算优先级：


从高到低：算数运算符 - - - > 比较运算符 - - -> 增强运算符 - - - > 逻辑运算符
`ps：小括号内运算级别最高` 
<br> 




> 感谢阅读，此博客为学习笔记，如有理解不对还望各位同学指正，`Julian_cn@126.com`

