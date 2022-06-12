import threading
import time

# 生成一个递归对象
Rlock = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_a()
        self.fun_b()

    def fun_a(self):
        Rlock.acquire()
        print('A加锁1', end='\t')
        Rlock.acquire()
        print('A加锁2', end='\t')
        time.sleep(2)
        Rlock.release()
        print('A释放1', end='\t')
        Rlock.release()
        print('A释放2')

    def fun_b(self):
        Rlock.acquire()
        print('B加锁1', end='\t')
        Rlock.acquire()
        print('B加锁2', end='\t')
        time.sleep(3)
        Rlock.release()
        print('B释放1', end='\t')
        Rlock.release()
        print('B释放2')


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
