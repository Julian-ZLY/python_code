# coding=utf-8
'''定义 Admin 类，继承 User 类'''

from class_User import User 

class Admin(User): 

    def __init__(self,first_name, last_name): 
        super().__init__(first_name, last_name)
        # super().__init__(last_name)

        # 定义权限列表
        self.privileges = ['can add post', 'can delete post', 'cat ban user'] 
        
    def show_privileges(self): 
        print("Hello Admin, Your privilege is :", self.privileges) 

print(__name__)
if __name__ == "__main__": 
    admin = Admin('tang','rong') 
    # admin.describe_user() 
    admin.show_privileges()

