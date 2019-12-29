'''定义用户类''' 

class User(): 
    
    def __init__(self, first_name, last_name): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.login_attempts = 0 

    def describe_user(self): 
        print("Hello ! My name is %s" % (self.first_name + self.last_name)) 
 
    def greet_user(self): 
        user_name = self.first_name + self.last_name   
        print("%s 好怪哦! 怪可爱的" % (user_name.title())) 

    def increment_login_attempts(self): 
        self.login_attempts += 1 
        print("当前登录人数为: %d" % self.login_attempts) 
    
    def reset_login_attempts(self): 
        print("登录人数要被重置咯....") 
        self.login_attempts = 0 
        print("当前登录人数为: %d" % self.login_attempts) 

if __name__ == "__main__": 
    user_01 = User("Julian", "-zly") 
    user_01.describe_user() 
    user_01.greet_user() 
    user_01.increment_login_attempts() 
    user_01.increment_login_attempts() 
    user_01.increment_login_attempts()

    print(user_01.login_attempts) 
    # 重置登录人数 
    user_01.reset_login_attempts() 
    print(user_01.login_attempts) 


    # user_02 = User("tang", "rong") 
    # user_02.describe_user() 
    # user_02.greet_user() 
