import threading
import time

# 商品
product = None
# 条件变量对象
con = threading.Condition()


# 生产方法
def produce():
    global product  # 全局变量产品
    if con.acquire():
        while True:
            print('---执行，produce--')
            if product is None:
                product = '袜子'
                print('---生产产品:%s---' % product)
                # 通知消费者，商品已经生产
                con.notify()  # 唤醒消费线程
            # 等待通知
            con.wait()
            time.sleep(2)


# 消费方法
def consume():
    global product
    if con.acquire():
        while True:
            print('***执行，consume***')
            if product is not None:
                print('***卖出产品:%s***' % product)
                product = None
                # 通知生产者，商品已经没了
                con.notify()
            # 等待通知
            con.wait()
            time.sleep(2)


if __name__ == '__main__':
    t1 = threading.Thread(target=consume)
    t1.start()
    t2 = threading.Thread(target=produce)
    t2.start()
