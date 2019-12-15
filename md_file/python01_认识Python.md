# 朱李延

   `2019-10-13，地点上海，浦东图书馆。我走的很慢，但不会停止脚步。`
<b>
<br>
# Python_day01 认识Python 
 - python 简介
 - python 脚本构成

<b>
<br>

## 一、Python 简介
 ### 定义：
   是一个免费，开源，跨平台，动态，`面向对象`的编程语言。
    
     

>    这位同学的博客有`面向对象`笔记，感兴趣的同学可以去看看: [点击链接](https://www.cnblogs.com/besttr/) 


 ### Python执行方式：
 
__`交互式` : 在命令行输入指令，回车即可得到结果 。__
    
1. 打开终端
 2. 输入python
  3. 输入`print("hello world")`
   4. 输入`exit()`退出python交互式
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/2019101313222217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDgxNDY3Mg==,size_16,color_FFFFFF,t_70)
   
   ps: 你已经学会python的第一个程序，赶紧发个朋友圈庆祝一下?。
   
   <br> 
   
 __`文件式` : 将指令编写到.py文件中，可以重复运行程序。__
 1. 创建.py文件写入python代码
 2. 打开终端进入指定目录
3. 运行python程序
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20191013134144620.jpg)
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20191013134316688.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDgxNDY3Mg==,size_16,color_FFFFFF,t_70)
    
 ### 程序执行过程
 
 由源代码转换为机器码的过程，分为编译和解释。
 1. 编译：在程序执行之前，通过编译器将源代码转换为机器码。
		 -- 特点：运行时，计算机可以直接执行。例如：c语言
		 -- 优势：运行速度快。
		 -- 缺点：不能跨平台，开发效率低。

   2. 解释：在程序执行中，通过解释器将源代码转换为机器码。 
		-- 特点：运行时逐语句解释执行。
		-- 优点：可以跨平台，开发效率高。例如：JavaScript
        -- 缺点：运行效率低。

  3. python 执行过程
    源代码 - -编译- -> 字节码(特定python的表现形式.pyc) - - 解释 - -> 机器码
    
 ### Python 版本
   1. python2.7 (2020年停止维护）
   2. python3.6 (我当前使用)
         
 ### Python 解释器
   1. 定义:
刚才我们说到Python语言是编程语言，是计算机能看懂的语言；计算机的大脑是CPU，通常我们叫它中央处理器，但是仍然不能直接处理 Python 语言；CPU 只能看两个数字，那是一种由0和1 数字组成数据。所以，我们需要一个翻译， 把Python语言翻译成CPU 能看懂的机器指令，这样计算机才能按照我们书写的Python程序去做事。

   2. 常用的解释器类型： 
==CPython==:   C语言开发的使用最广的解释器。
==IPython==: 基于cpython之上的一个交互式计时器,交互方式增强,功能和cpython一样。
==JPython==: 运行在Java上的解释器,直接把python代码编译成Java字节码执行。
==IronPython==: 运行在微软 .NET 平台上的解释器，把python编译成. NET 的字节码。 

<br> 

## 二、Python 脚本构成

```python
#! /usr/local/bin/python3
#! -*- coding: utf-8 -*- 
""" This is a test module """

var = "values"

def run(): 
    print("variable var the values is ", var) 

if __name__ == "__main__": 
    run() 
```

### 说明
  `1` . 指定Python解释器路径
  `2` . 声明文件中的编码格式，在使用中文过程中，最好使用utf-8 
  `3` . 模块文档，文档字符串
  `5` . 变量
  `7` . 函数   
  `8` . 函数里的代码，代表一个功能
  `10` . 主程序

### 变量
1. 定义：关联一个对象的标识
2. 命名规则：
    -必须为字母数或下划线，后面跟着字母，数字，下划线。
    -不能使用保留关键字(python内特殊字符，比如：`True`
 3. 命名语法：字母小写，多个单词用下划线隔开。

```python
# 命名规则
变量名 = '表达式' 
变量名1 = 变量名2 = '表达式' 
变量名1, 变量名2 = '表达式1, 表达式2'

# 尽量做到见名知意
student_name = '学生姓名'
```

### 函数
1. 定义： 
表示一个功能，制作函数的人叫做函数定义者，使用函数的人叫做函数调用者。
2. Python内置函数，比如`print()`

```python
"""python内置函数"""

# 将括号里面的数据，显示到控制台中
print("I am a built-in function print")

# 将用户在控制台中输入的内容赋值给变量,括号内为提示信息
var = input("Prompt message:")
```
<br>

