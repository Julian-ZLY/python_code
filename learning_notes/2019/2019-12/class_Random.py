'''随机色子''' 

import random 


class Die(): 

    def __init__(self, sides=6): 
        self.sides = sides

    def roll_die(self): 
        ''' 
        打印1和骰子面数之间的随机数 
        ''' 
        num_list = [] 
        for _ in range(self.sides): 
            random_num = random.randint(1, self.sides) 
            num_list.append(random_num) 
        return num_list
        

if __name__ == '__main__': 
    die_01 = Die() 
    result = die_01.roll_die() 
    print(result)

    die_02 = Die(10) 
    result = die_02.roll_die() 
    print(result)

    die_03 = Die(20)  
    result = die_03.roll_die() 
    print(result)