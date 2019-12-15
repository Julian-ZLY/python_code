
# name_list = ['admin', 'julian', 'tom'] 

# for name in name_list: 
#     if name == 'admin': 
#         print("Hello %s, would you like to see a status report?"%(name.title()))
#     else: 
#         print("Hello {}, thank you for logging in again".format(name.title())) 

class Student(): 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

info = Student('Julian', 24) 
print(info.name, info.age)