# shelve
"""
这个类是将Python的基础变量，以字典的形式，保存在二进制文件中

"""

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(shelfFile['cats'])
shelfFile.close()
