"""
将列表写入Python文件中
之所以用pprint，是因为他会对字典进行排序
"""

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
with open('myCats.py', 'w+') as fileObj:
    fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
