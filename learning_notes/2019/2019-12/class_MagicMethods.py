'''Python魔法方法''' 

# 继承 int 类，重写魔法方法 
class MagicMethods(int): 

    def __init__(self, num): 
        self.num = num 
    
    # 魔法方法返回字符串
    def __str__(self): 
        re_str = str(self.num)
        return re_str 
    
    __repr__ = __str__ 

    # 相加
    def __add__(self, other): 
        re_add = int(self.num) + int(other)
        return re_add 

     

t1 = MagicMethods(5)
t2 = MagicMethods(10) 

print(t1)
print(t2)

# del t1 
print(t1 + t2)