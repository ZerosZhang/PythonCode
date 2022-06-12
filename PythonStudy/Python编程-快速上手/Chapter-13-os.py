"""
os.path.join() # 生成路径字符串
os.getcwd()  # 获取当前工作目录的绝对路径
os.chdir()   # 改变当前工作目录
os.makedirs() # 创建新文件夹，创建所有必要的中间文件夹
os.path.abspath(path) # 将返回参数的绝对路径的字符串
os.path.isabs(path)  # 判断传入参数是否为绝对路径
os.path.relpath(path, start) # 将返回从start路径到path的相对路径字符串，
                                如果没有提供start，就使用当前工作目录作为开始路径
                                这里的path和start都是绝对路径
os.path.dirname(path)
os.path.basename(path)
os.path.split(path)
path.split(os.path.sep)
"""

"""
os.path.getsize(path)
os.listdir(path)
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)
"""
