'''Privileges类''' 

from class_Admin import Admin 

class Privileges(Admin): 

    def __init__(self): 
        self.privileges = Admin('zhu', 'liyan') 

if __name__ == "__main__":
    pri = Privileges() 
    # 创建实例对象，调用当前类 privileges 属性，通过类属性调用 Admin 类方法 
    pri.privileges.show_privileges()    