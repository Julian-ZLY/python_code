# python_code

## python中适用于class BIF 

1. issubclass(class, classinfo) 
> 测试是否是父子类

2. isinstance(object, classinfo) 
> 测试实例对象是否属于该类

3. hasattr(object, name) 
> 测试示例对象中是否有该属性
 
4. getattr(object, name[, default]) 
> 返回该实例对象中的属性值 

5. setattr(object, name, value) 
> 添加实例对象中的属性，自定义 

6. delattr(object, name) 
> 删除实例对象中的属性，如果不存在则 Error 

7. property(fget=None, fset=None, fdel=None, doc=None) 
> 


## 魔法方法  面向对象的python 构造和解析 
1. __init__(self, ...)
> 初始化

2. __new__(cls[, ...])
> 重写

3. __del__(self) 
> 当做垃圾回收机制，当对象生成之后，所有对ta的引用都被 del 时，__del__ 方法被调用； 



## 工厂函数 算数运算
1. __add__ 
> 

2. 