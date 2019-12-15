
# 上海
`2019-11-10，地点：上海浦东图书馆。那些未曾尝试的为什么就说不能做到？？？`

<br> 


# Python_day05 Python语句

  * 语句
  * if 语句
  * 循环语句
  * 跳转语句  
 
 <br> 
 

# 一、语句

  1. 物理行：  
程序员编写代码时显示的行。

  2. 逻辑行：  
指源代码经过预编译后，代码所在的那一行。

  3. 隐式换行：  
所有括号中的内容都可以换行。

    
```python    
'''隐式换行''' 

sum_01 = 1 + (2 + 3 
		 + 4) 

print(sum_01)			# 10 
```
    
    

  4. 显示换行：  
通过折行符号 ‘\’ 换行。

    
```python    
'''显示换行''' 

sum_02 = 1 + 2 + 3 \
         + 4

print(sum_02) 			# 10 
```
    
    

  5. 缩进：  
在 Python中，对于类定义、函数定义、流程控制语句、异常处理语句等，行尾的冒号和下一行的缩进，表示下一个代码块的开始，而缩进的结束则表示此代码块的结束。通常情况下都是采用4 个空格长度作为一个缩进量（默认情况下，一个 Tab 键就表示 4 个空格）  
  
<br> 

# 二、if 语句

## 作用：

编程是经常需要检查一系列条件，并根据此决定采取什么措施。在Python中，if 语句让你能过检查程序的当前状态，并根据此采取相应的措施。  
  

## 条件测试：

每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件表达式。Python根据条件的是的值为 True 还是 False来决定是否执行 if 语句中的代码。如果条件测试的值为 True，Python就执行紧跟在 if 语句后面的代码；如果为 False，Python就忽略这些代码。

    
```python     
'''条件测试''' 

# 检查单个条件
car = 'BMW' 
car == 'BMW'						# True 
car == 'BYD'						# False 

if car == 'BMW':					# 注意：if 语句行结束后接冒号
    print("My car is a :", car) 	# My car is a BMW


if car == 'BYD':					# 此语句条件表达式结果为 False
    print("My car is a :", car) 	# 不执行此行 


# 检查多个条件
age_01 = 20 
age_02 = 23 

age_01 >= 20 and age_02 > 20 		# True 
age_01 >= 25 or  age_02 == 23 		# True 
age_01 >= 25 and age_02 == 23		# False 
```
 
`ps: 如果大小写很重要，这种行为有其优点。但是如果大小写无关紧要，而只想检查变量的值，可将变量的值转换为小写，再进行比较。可使用 lower()
函数进行转换。示例：str.lower()`  
  

## if语句语法：

**`1. if - else 语句`**  
  
**说明：**  
经常需要在条件测试通过时执行的一个操作，并在没有通过时执行另一个操作；在这种情况下，可以 if - else 语句；if - else 类似于简单的 if
语句，但其中的 else 语句让你能够指定条件测试未通过时要执行的操作。  
  
**语法：**

    
```python    
'''if-else语法规则'''

"""
if conditional_test: 
    do something_01
else: 
    do something_02
""" 

age = 23 
if age >= 25: 					# 条件表达式结果为 False 
    print("You are under 25")
else:
    print("Your age is :", age)
```

**`2. if - elif - else 语句`**  
  
**说明：**  
经常需要检查超过两个条件的情形，为此可以使用 if-elif-else结构。Python执行代码块时，它依次检查每个条件测试，知道遇到通过了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。  

**语法：**

    
```python   
'''if-elif-else语法规则'''

"""
if conditional_test_01: 
    do something_01
elif conditional_test_02: 
    do something_02
else: 
    do something_03
""" 

age = 12 

if age < 4: 
    print("Your admission cost is $0.") 
elif age < 18: 
    print("Your admission cost is $5.")
else: 
    print("Your admission cost is $10.")  
```
    

`ps: 在 if 条件判断中，elif 语句可以有 0 个或者多个；else 语句最多只能有 1 个，只能放在条件判断的最后执行。`

  
<br> 

# 三、循环语句

## for 循环
1. 作用
用来遍历可迭代对象的元素。
`ps: 用来遍历可迭代对象的元素;例如：str('潘石屹学python')`
2. 语法
```python
'''for 循环'''

'''
for 变量列表 in 可迭代对象:
	循环体
else:
	循环过后执行的语句
'''

# 迭代字符串
for i in str('潘石屹学python'):
    print(i)
    
> 潘
> 石
> 屹
> 学
> p
> y
> t
> h
> o
> n   

# range()函数
for i in range(5): 
    print(1)
    
> 0 
> 1 
> 2
> 3
> 4

# 迭代列表
for i in ['hello', 'world']: 
    print(i) 

> hello 
> world 


for i in range(3): 
    print(i) 
    print('循环体%d'%i)
else: 
    print('循环过后执行的语句块%d'%i) 

> 0
> 循环体0
> 1
> 循环体1
> 2
> 循环体2
> 循环过后执行的语句块2
```
`ps:`
- `range()函数：`可以生成一系列整数的可迭代对象。
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。

- 当对元组，列表，字典，集合，字符串使用for循环语句的时候，可以依次拿到里面的数据，这样的过程称为遍历，也叫迭代。

<br> 


## while 循环
1. 作用
满足条件，重复执行语句。
`ps: 当我们知道循环次数时，可是用for循环；否则推荐使用while循环。`
2. 语法
```python
'''while循环语句'''

'''
while 真值表达式: 
    条件满足循环体
else: 
    条件不满足循环体
'''

num = 0 
while num < 4: 
    print('while循环第%d次'%num)
    num += 1 
else: 
    print('条件不满足循环体第%d次'%num)

> while循环第0次
> while循环第1次
> while循环第2次
> while循环第3次
> 条件不满足循环体第4次
```
`ps: while 循环语句后接真值表达式；真值表达式返回结果为True时，开始执行循环体语句；我们定义变量 num = 0，执行循环体中让变量 num 自增长加 1；直到 num < 4 时，循环体结束。`
<br> 

# 四、跳转语句
1. 作用
    跳出循环体
    - continue跳出本次循环，继续执行下次循环。
    - break 跳出循环，不再执行 break 之后的语句。

2. 语法
```python
'''跳转语句'''

# continue
list_name = ['潘石屹', '马云', '马化腾'] 
for name in list_name: 
    if name == '马云':
        print('%s被跳转了'%name) 
        continue
    else: 
        print(name)

> 潘石屹
> 马云被跳转了
> 马化腾


# break跳转
num = 0 
while num < 10: 		# 死循环
    num += 1
    for number in range(1,10): 
        if number == 2: 
            print(number)
            break        # 跳出内层循环 for 
        else: 
            print('内层循环的数字为%d'%number)
    if num == 2: 
        break            # 跳出外层循环 while
else: 
    print('我不会执行！')
    
> 内层循环的数字为1
> 2
> 内层循环的数字为1
> 2
```
> 感谢阅读，此博客为学习笔记，如有理解不对的地方还望各位同学指正，本人邮箱：`Julian_cn@126.com`

