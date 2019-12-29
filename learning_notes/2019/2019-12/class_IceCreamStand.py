'''冰淇淋类''' 

from class_Restaurant import Restaurant  

class IceCreamStand(Restaurant): 
    
    def __init__(self,restaurant_name, cuisine_type): 
        super().__init__(restaurant_name, cuisine_type) 
        self.flavors = ['草莓', '巧克力', '香蕉'] 
    
    def desIceFlavors(self): 
        print("冰淇淋的口味有:", self.flavors) 

if __name__ == "__main__":
    user_01 = IceCreamStand('小伙计', '冰淇淋') 
    # user_01.restaurant_name() 
    user_01.describe_restaurant() 
    user_01.desIceFlavors() 
