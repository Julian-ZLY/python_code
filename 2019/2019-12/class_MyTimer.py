"""python计时器"""

import time as time 


class MyTimer(object):

    def __init__(self): 
        # 定义开始属性
        self.prompt = "未开始计时!" 
        
        # 定义初始时间 
        self.begin = 0 
        self.end = 0
        self.result = 0

    # 重写 __str__ 函数 
    def __str__(self): 
        return self.prompt 

    # 开始计时
    def start(self): 
        begin_time = time.time() 
        # 修改属性 
        self.begin = begin_time 
        # self.prompt = ("开始计时时间为:" + str(self.begin))
        # self.prompt = "ps: 请调用 stop() 方法后再次查看结果！"
        print("开始计时...") 

    # 停止计时
    def stop(self): 
        # 定义规则 
        if self.begin: 
            end_time = time.time() 
            # 修改属性
            self.end = end_time 
            # 修改提示信息
            # self.prompt = ("计时时间为:" + str(int(self.end - self.begin)))
            print("计时结束 !")
            self._calc()
        else: 
            print("请先调用 start() 方法!")

    # 定义内部方法
    def _calc(self):
        self.prompt = "总共运行了: "
        self.prompt += str(int(self.end - self.begin))
        self.result = int(self.end - self.begin)

    def __add__(self, other):
        result = self.result + other.result
        return "总共运行: " + str(result) + "秒"


if __name__ == "__main__":
    t1 = MyTimer()
    t1.start()
    # print(t1)
    time.sleep(3)
    t1.stop()
    print(t1)
    print(t1.result)

    print("-" * 20)

    t2 = MyTimer()
    t2.start()
    time.sleep(5)
    t2.stop()
    print(t2)

    print(t1 + t2)

    print("-" * 20)
    t3 = MyTimer()
    t3.start()
    time.sleep(2)
    t3.stop()
    print(t3)

    print(t3 + t1)

    print("-" * 20)
    print(t2 + t3)
    # print(t1)
    # t1.start()
    # print(t1)
    # time.sleep(2)
    # t1.stop()
    # print(t1)
    # re_time = time.localtime()

    # print(re_time)
    # print(dir(time))
    # print(time.time())
    # start_time = int(time.time())
    # time.sleep(7)
    # end_time = int(time.time())
    # print(time.time())

    # print(end_time - start_time)
