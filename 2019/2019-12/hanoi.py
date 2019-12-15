def hanoi(n, x, y, z): 
    if n == 1: 
        print(x, '-->', z) 
    else: 
        # 将 x 上的 n-1 个盘子移动到 y 
        hanoi(n - 1, x, z, y)
        # 将 x 移动到 z 
        print(x, '-->', z)
        # 将 y 上的 n-1 个盘子移动到 x  
        hanoi(n - 1, y, z, x)

number = int(input("请输入汉诺塔层数:")) 
if number > 1: 
    hanoi(number, 'x', 'y', 'z') 