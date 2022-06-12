import threading
import time


def func():
    global _number  # 全局变量
    lock.acquire()  # 获得锁，加锁，别的线程不可以使用_number
    _number1 = _number
    time.sleep(0.1)
    _number = _number1 - 1
    lock.release()  # 释放锁，解锁，别的线程可以使用_number了


if __name__ == '__main__':
    lock = threading.Lock()
    _number = 100
    list_thread = []

    for _ in range(100):  # 开启100个线程
        _thread = threading.Thread(target=func)
        _thread.start()
        list_thread.append(_thread)

    # 等待线程运行结束
    for _thread in list_thread:
        _thread.join()

    print(_number)
