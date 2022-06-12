import threading

event = threading.Event()


def func():
    print('等待服务响应...')
    event.wait()  # 等待事件发生
    print('连接到服务')


def connect():
    print('成功启动服务')
    event.set()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=connect)

t1.start()
t2.start()
