'''定义餐馆类''' 


class Restaurant():  

    # 实例变量
    def __init__(self, restaurant_name, cuisine_type): 
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type 
        # 定义就餐人数
        self.number_served = 0

    # 实例方法 
    def describe_restaurant(self): 
        print("餐馆名字是: %s, 菜品是: %s 。" % (self.restaurant_name, self.cuisine_type)) 
    
    def open_restaurant(self): 
        print("餐馆正在营业") 
    
    def get_number_served(self): 
        print("当前就餐人数为 %d 人。" %(self.number_served))

    # 添加 set_number_served() 方法
    def set_number_served(self, number_served): 
        self.number_served = number_served 
        # self.get_number_served() 
    
    # 定义递增人数 
    def increment_number_served(self, number_served): 
        self.number_served += number_served 
        # self.get_number_served()  


    
if __name__ == "__main__":

    # 创建实例对象
    restaurant = Restaurant("海参炒面", "东北菜") 
    # 修改就餐人数
    # restaurant.number_served = 20 
    # 显示当前餐馆信息
    restaurant.describe_restaurant()  
    # restaurant.open_restaurant() 
    # 得到餐馆就餐人数 
    # restaurant.get_number_served() 
    # restaurant.set_number_served(40)

    # 递增餐馆人数 
    restaurant.set_number_served(10) 
    restaurant.get_number_served() 

    restaurant.increment_number_served(40)
    restaurant.get_number_served() 

    restaurant.increment_number_served(100) 
    restaurant.get_number_served() 
    