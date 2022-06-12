"""
ljust和rjust：左对齐和右对齐
center，ljust，rjust分别是返回固定长度的居中，左对齐，右对齐字符串
默认填充符号为空格
"""


def printPicnic(itemsDict, leftWidth, rightWidth):
    # 打印：-------PICNIC ITEMS-------
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

"""
这里有一个问题，就是中文字符与英文字符不对齐的问题
"""
picnicItems = {'三明治': 4, '苹果': 12, '杯子': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
