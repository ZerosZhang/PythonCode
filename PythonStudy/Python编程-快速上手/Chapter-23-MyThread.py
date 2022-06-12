from threading import Thread
from time import ctime, sleep


# 创建 Thread 的子类
class MyThread(Thread):
    def __init__(self, target, args, kwargs):
        """
        :param target: 可调用的对象
        :param args: 可调用对象的参数
        :param kwargs: 可调用对象的关键字参数
        """
        Thread.__init__(self)  # 不要忘记调用Thread的初始化方法
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def run(self):  # 重写父类的run方法
        self.result = self.target(*self.args, **self.kwargs)

    def get_result(self):
        self.join()
        return self.result


# 输出开始时间和结束时间
def func(name, sec=1):
    print(f'{name} ---开始--- : 当前时间 {ctime()}')
    sleep(sec)
    print(f'{name} ***结束*** : 当前时间 {ctime()}')
    return 'Hello World!'


_thread1 = MyThread(target=func, args=['线程1'], kwargs={'sec': 1})
_thread1.start()
print(_thread1.get_result())
