"""
自动获取当前的IP地址
"""
import socket


def get_ip():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 这里甚至都不需要连上
        _socket.connect(('10.255.255.255', 1))
        IP = _socket.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        _socket.close()
    return IP


if __name__ == '__main__':
    print(get_ip())
