try:
    # 正常程序
    print('I am sure no exception is going to occur!')
except Exception:
    # 这里的代码会在try语句里发生异常时运行
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    # 这里的代码不管有没有异常，都会执行
    print('This would be printed in every case.')


# raise Exception("Invalid level!")


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return ''.join(self.args)


try:
    raise Networkerror("Bad hostname")
except Networkerror as  e:
    print(e)
