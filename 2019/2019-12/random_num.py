'''Python标准库random''' 

import random 

random_number = random.randint(1,10)
print('随机数为: %d' % random_number) 

count = 0 

while True: 
    request_num = int(input("请输入 1~10 你认为对的随机数:"))
    count += 1  
    if request_num > random_number: 
        print('大了大了。。。') 
    elif request_num < random_number: 
        print('小了小了...') 
    else: 
        print('猜对了，共用 %d 次. ' % count)
        break 

