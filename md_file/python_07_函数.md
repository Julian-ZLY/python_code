# Python07 函数

@(python学习笔记) 

> Julian：当你的才华撑不起你的野心时，你需要静下心来学习。

# Python_day07 函数
- 函数
- 定义函数
- 函数传参
- 作用域
- 内嵌函数
- 匿名函数

<br> 

# 函数 
1. 定义
用于封装一个特定的功能，表示一个功能，可以重复调用执行的语句块。你已经知道Python提供了许多内建函数，比如`print()`。但你也可以自己创建函数，这被叫做用户自定义函数。 
2. 作用
提高程序的复用性，可维护性，代码层次更清晰。 
3. 特点 
函数三大特点: 功能，参数，返回值。 
功能：表示该函数能实现什么样的功能。 
参数：调用函数所需要的参数。 
返回值：返回函数计算的结果，默认返回`None`。
4. 个人建议
- 编写函数时，需要牢记几个细节；应该给函数指定描述性名称，且只在其中使用小写字母和下划线。 
- 描述性名称可以帮助你和别人明白代码想做什么，给模块命名时也应遵循上述约定。 （后面会写到）
- 每个函数都应该包含简要的阐述其中功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。

<br> 

# 定义函数 
1. 语法
```python 
'''函数定义''' 

def fun_01(): 
    '''
    我是第一个函数，我的名字是fun_01
    '''
    str_01 = 'fun_01'
    print('我是%s函数'%(str_01))

fun_01()                # 我是fun_01函数
type(fun_01)            # <class 'function'>
# 查看函数属性 
fun_01.__doc__ 			# '\n    我是第一个函数，我的名字是fun_01\n    ' 
# 查看函数帮助文档
help(fun_01)   
```
![Alt text](./1575771432162.png)

2. 说明 
- 函数第一行语句可以选择性的使用文档字符串存储和函数与参数的说明； 
- `def`关键字，全称`define`，意为'定义'，def关键字后接函数名； 
- 函数名：建议使用动词，对函数体中语句的描述；
- 函数体：完成功能的语句，建议语句不要太多。 

3. 调用函数
函数名(实参列表)；根据形参传递内容。

<br> 

# 函数传参
- 形参：定义函数是所需要的参数视为`函数的形参`，只是一种形式的存在，就像数学中的`x`一样，没有实际的值，通过别人赋值后才有意义，可视为变量。 
- 实参：调用函数所需要传递的参数视为`函数的实参`， 实参是一个实际存在的值，可以是：字符串，列表，字典等等。 

<br> 

1. 实参传递 argument 
```python 
'''函数参数传递'''

# 定义函数 
def fun_02(a, b, c):
    print("a ->", a)
    print("b ->", b)
    print("c ->", c)
```
- 位置传参 
```python
'''位置传参''' 

# 实参与形参的位置依次对应。
fun_02(1,2,3)  

# out: 
a -> 1
b -> 2
c -> 3 
``` 
- 序列传参
```python 
'''序列传参''' 

# 实参用*将序列拆解后与形参的位置依次对应，元组，列表，集合等。 
fun_02(*['I','Love','Python'])

# out: 
a -> I
b -> Love
c -> Python
``` 
- 关键字传参 
```python
'''关键字传参''' 

# 实参根据形参的名字进行对应
fun_02(a = 'Hello', c = 'Hai', b = 'Shang')

# out: 
a -> Hello
b -> Shang
c -> Hai 
```
- 字典传参 
```python 
'''字典传参''' 

# 实参用**将字典拆解与形参的名字进行对应；字典中的键要与函数中的形参对应 
fun_02(**{'a':'hello','b':'world','c':'!'})

# out: 
a -> hello
b -> world
c -> !
```
<br> 

2. 形参传递 parament
```python  
 # 此行为了排版使用，不用理会，看下面哈
```
- 默认（缺省）参数 
```python
'''默认参数''' 

# 定义函数时，给与形参默认参数
def fun_03(a = 0, b = 0, c = 0): 
    print("a ->", a)
    print("b ->", b)
    print("c ->", c)

fun_03() 

# out: 
a -> 0
b -> 0
c -> 0


fun_03('hello')

# out: 
a -> hello
b -> 0
c -> 0
```
- 位置形参
```python
'''位置形参''' 

# 定义函数时，给形参一个实际的位置 
def fun_04(a, b, c): 
    print("a ->", a)
    print("b ->", b)
    print("c ->", c)

fun_04(1,2,3)

# out: 
a -> 1
b -> 2
c -> 3 
``` 
- 星号元组形参 
```python 
'''星号元组形参''' 

# 收集多余位置形参，形参名可自定义，约定俗成为 args 
def fun_05(*args): 
    print('参数长度为:', len(args)) 
    print('实参数据为:', args)  

fun_05('aaa') 
fun_05(*['hello','world'])
```
- 命名关键字形参
```python 
'''命名关键字形参''' 

# A.命名关键字形参:强制实参使用关键字传递 
def fun_06(*, a, b): 
    print('a ->', a) 
    print('b ->', b) 

# 调用_01 
fun_06(1, 2) 			# Error: TypeError


# 调用_02 
fun_06(a = 'hello', b = 'world') 

# out: 
a -> hello
b -> world


# 调用_03 
fun_06(**{'a': '你好', 'b': '上海'})

# out: 
a -> 你好
b -> 上海 


# B.a、b 是位置传参，c、d 必须是关键字传参 
def fun_07(a, b, *, c, d): 
    print('a ->', a) 
    print('b ->', b) 
    print('c ->', c) 
    print('d ->', d) 

# 调用_01 
fun_07(1, 2, 3, 4) 			# Error: TypeError  


# 调用_02 
fun_07(*['A', 'B'], c = 'C', d = 'D') 

# out: 
a -> A
b -> B
c -> C
d -> D 


# C. 星号元组形参后的，位置形参是命名关键字形参  
def fun_08(*args, a, b): 
    print('参数长度为:', len(args)) 
    print('实参数据为:', args)  
    print('a -> %s'%(a))  
    print('b -> %s'%(b))

# 调用_01 
fun_08(1,2,3,4, a = 'hello', b = 'world')

# out: 
参数长度为: 4
实参数据为: (1, 2, 3, 4)
a -> hello
b -> world 
``` 
- 双星号字典形参 
```python 
'''双星号字典形参''' 

# A. 可以收集多余的字典关键字实参，一般命名为 kwargs 
def fun_09(**kwargs): 
	print(kwargs) 

# 对于函数内部: kwargs就是字典，调用使用关键字传参 
fun_09(name = 'Julian', arg = 23, sex = 'Man')

# out: 
{'name': 'Julian', 'arg': 23, 'sex': 'Man'} 


# B. 星号元组形参和双星号字典形参 
def fun_10(*args, **kwargs): 
    print('星号元组形参的值为:', args) 
    print('双星号字典形参的值为:', kwargs) 

# 调用_01 
fun_10() 

# out: 
星号元组形参的值为: ()
双星号字典形参的值为: {} 


# 调用_02 
fun_10(1, 2, 3, time = '2019-12-08', city = 'ShangHai')

# out: 
星号元组形参的值为: (1, 2, 3)
双星号字典形参的值为: {'time': '2019-12-08', 'city': 'ShangHai'} 
```
3. 说明 
```python 
'''函数的形参定义''' 

def fun_x(a, b, *args, c, d, **kwargs): 
    print('a -> %s' %(a)) 
    print('b -> %s' %(b)) 
    print('星号元组形参的值为:', args) 
    print('c -> %s' %(c)) 
    print('d -> %s' %(d)) 
    print('双星号字典形参的值为:', kwargs) 

fun_x(*['我是位置传参A', '我是位置传参B'],'星号元组传参', c = '关键字_01', d = '关键字_02', e = '我可不是关键字', f = '你猜我是什么传参') 

# out: 
a -> 我是位置传参A
b -> 我是位置传参B
星号元组形参的值为: ('星号元组传参',)
c -> 关键字_01
d -> 关键字_02
双星号字典形参的值为: {'e': '我可不是关键字', 'f': '你猜我是什么传参'}
```
- 函数的形参列表，是调用者需要提供的信息；  
- 函数中形参的定义顺序：参数自左至右的顺序； 
- 位置形参 --> 星号元组形参 --> 命名关键字形参 --> 双星号字典形参  
- 星号元组形参一般命名为：`*args`，形参列表一般只能有一个； 
- 双星号字典形参一般命名为：`**kwargs`，形参列表一般只能有一个； 
- 星号元组形参后的参数，强制使用关键字传参方式传递；

<br> 

4. 可变参数传递和不可变参数传递
- 不可变类型：字符串、元组、固定集合、整数、浮点数、复数
- 可变类型：列表、字典、集合
- 不可变类型的数据传参时，函数内部不会改变原数据的值。
- 可变类型的数据传参时，函数内部可能改变原数据的值。

<br> 

# 作用域 LEGB 
1. 定义 
程序设计概念，通常来说，一段程序代码中所用到的名字并不总是有效/可用的，而限定这个名字的可用性的代码范围就是这个名字的[作用域](https://baike.baidu.com/item/%E4%BD%9C%E7%94%A8%E5%9F%9F/10944767?fr=aladdin)。--baidu 
2. 说明： 
- Local 局部作用域：函数内部。
- Encolsing 外部嵌套作用域：函数嵌套（请看下一个知识点函数嵌套）。 
- Global 全局作用域：py文件内部。
- Builtins内建模块作用域：比如`print()`等。 
3. 全局和局部变量 
```python 
'''全局和局部变量''' 

# 我是全局变量
num_01 = 10 

def fun_x(num_01): 
    # 重新定义变量，和外边 num_01 没有任何关系 
    num_01 = 20 
    return num_01 

result = fun_x(num_01) 
print(result) 				# 20 

print(num_01)				# 10 


# 修改全局变量：错误例子
num_02 = 100 

def change_var01(): 
    print(num_02)
	num_02 += 1 
    return num_02 

change_var01() 			# Error: UnboundLocalError


# 修改全局变量：使用 global 关键字
num_03 = 300 

def change_var02(): 
    # print(num_03)    # 修改全局变量前不能再使用，否则会报错，不信，你试试 ！  
    global num_03      # 使用 global 关键字声明一下 
    num_03 = 250 
    return num_03 

change_var02()  
print(num_03)
``` 
4. 内存图 
![Alt text](./1575959243563.png)
`ps：变量名查找规则，由内到外；L ---> E  --->  G   ---> B` 

<br> 

# 内嵌函数
1. 定义 
顾名思义，在函数内定义另一个函数，称之为内嵌函数。 
2. 定义内嵌函数 
```python
'''定义内嵌函数''' 

def MyFun(): 
    print("I'm is MyFun !") 
    def YouFun(): 
        print("I'm is YouFun !") 
    YouFun() 

MyFun() 

# out: 
I'm is MyFun !
I'm is YouFun ! 
```
3. 闭包
[闭包](https://baike.baidu.com/item/%E9%97%AD%E5%8C%85/10908873?fr=aladdin)就是能够读取其他函数内部变量的函数；在本质上，闭包是将函数内部和函数外部连接起来的桥梁。--baidu 
```python 
'''闭包''' 

# 计算乘积
def fun_x(num_01): 
    # 函数嵌套
    def fun_y(num_02): 
        return num_01 * num_02 
    return fun_y 

re_fun = fun_x(10)				# 返回函数对象 fun_y 
re_fun(10)						# 调用内层函数计算结果	100 
```
3. 内嵌函数作用域
```python 
'''内嵌函数作用域''' 

num_01 = 1000 					# 全局变量

def fun_01():
    num_01 = 5                  # 局部变量 
    def fun_02(): 
        nonlocal num_01         # 使用 nonlocal 关键字修改外层作用域变量
	    num_01 = 10             # 修改外部作用域变量，只能向外一层
        return num_01 
    print(num_01)               # 还未调用内层函数，所以值为 5 
    
    fun_02()
    print(num_01)               # 值已经被嵌套函数内修改


fun_01()

# out: 
5
10 
``` 
说明： 
- 函数嵌套：内部函数整个作用域都在外部函数之内； 
- 函数嵌套：嵌套中的函数只能依靠外层函数调用，无其他方式； 
- 变量作用域：修改外层作用域变量之前，将不能再次调用，否则会出现：`SyntaxError: name 'xxx' is used prior to global declartion. `

<br> 

# 匿名函数
1. 定义 
顾名思义就是没有名字的函数，解决简单的问题，使用完成就释放。 

2. lambda 表达式 
```python 
'''匿名函数''' 

# 计算两个数的乘积 
def product(num_01, num_02): 
    return num_01 * num_02 

product(5, 5) 

# out: 
25 


# 使用匿名函数
result = lambda num_01, num_02 : num_01 * num_02 
result(3, 5)

# out: 
15 
``` 
3. 说明 
- 匿名函数默认不用`retrun`语句，默认返回计算结果； 
- 关键字`lambda`表示匿名函数，冒号左边是定义的形参； 
- 匿名函数冒号后面的表达式有且只能有一个，注意：是表达式，而不是语句； 
- 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突； 

<br> 

> 感谢阅读，此博客为学习笔记，如有理解不对的地方还望各位同学指正，本人邮箱：`Julian_cn@126.com`

