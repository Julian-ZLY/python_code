"""菲波拉契数""" 

class FiboracciNumber(object): 

    def __init__(self, n=20): 
        self.num_a = 0 
        self.num_b = 1 
        self.n = n
    
    def __iter__(self): 
        return self 

    def __next__(self): 
        self.num_a, self.num_b = (self.num_a + self.num_b), self.num_a 
        # 当菲波拉契数 大于指定值 抛出Error 
        if self.num_a > self.n: 
            raise StopIteration 
        return self.num_a 

        
if __name__ == "__main__":
    t1 = FiboracciNumber(100) 
    for each in t1: 
        print(each)
