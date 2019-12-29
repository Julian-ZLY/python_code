# 寻找水仙花数。 


def get_number():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(low, '-->', mid, '-->', high, '==', num)

def var(n): 
    for i in range(n):
        yield i

for j in var(10): 
    print(j)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


 