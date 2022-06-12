import logging

# 禁用等级低于或等于INFO的所有日志
logging.disable(logging.INFO)
"""
日志等级：
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

# 设置日志格式，显示等级高于或等于DEBUG的所有日志
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')


# 输入filename参数可以将日志保存到文件中去
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s', filename='test.txt')


def factorial(n):
    logging.debug('Start of factorial(%s)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % n)
    return total


if __name__ == '__main__':
    logging.debug('这是debug')
    logging.info('这是info')
    logging.warning('这是warning')
    logging.error('这是error')
    logging.critical('这是critical')
