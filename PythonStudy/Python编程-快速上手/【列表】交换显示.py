"""
这里比较有用的是列表交换行列的代码
"""


def printTable(_list: list):
    # colWidths用于存_list中列表项最大长度
    """
    [0] * len(_list) 是列表的复制操作，比如这里len(_list)为3，则colWidth = [0, 0, 0]
    =============================================================================
    _item是一个列表
    map(len,_item) 用于对每个_item列表中的项，计算长度，并返回一个迭代器
    list()将这个迭代器转换为列表，max()用于计算这个列表中的最大值
    =============================================================================
    这里的最终输出如下：
    [['apples', 'oranges', 'cherries', 'banana'],   # 这个列表中单词的最大长度为8
     ['Alice', 'Bob', 'Carol', 'David'],            # 这个列表中单词的最大长度为5
     ['dogs', 'cats', 'moose', 'goose']]            # 这个列表中单词的最大长度为5
    因此colWidths = [8, 5, 5]
    """
    colWidths = [0] * len(_list)
    for _index, _item in enumerate(_list):
        colWidths[_index] = max(list(map(len, _item)))

    # 交换列表行列，并循环给字符串进行对齐
    """
    [['apples', 'oranges', 'cherries', 'banana'],
     ['Alice', 'Bob', 'Carol', 'David'],
     ['dogs', 'cats', 'moose', 'goose']]
    ==============================================================================
    *_list是一个解包的操作，即将上面的这一个二维列表，解包为3个一维列表如下：
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
    ==============================================================================
    zip()操作是将这三个列表对应的项进行纵向组合，才成为一个新的列表
    1. 将apples，Alice，dogs进行组合('apples', 'Alice', 'dogs')
    2. 将oranges，Bob，cats进行组合('oranges', 'Bob', 'cats'),
    以此类推
    ==============================================================================
    enumerate(_item)是同时获得对应的下标和项
    目的是为了进行字符串对齐，比如['apples', 'oranges', 'cherries', 'banana']
    这几个单词进行纵向表示的时候，比较好看的方式是对齐最大长度的单词，如下所示
      apples
     oranges
    cherries
      banana
    ==============================================================================
    print()是为了显示一个回车
    """
    _list_zip = list(zip(*_list))
    for _item in _list_zip:
        for _index, _str in enumerate(_item):
            print(_str.rjust(colWidths[_index]), end=' || ')
        print()


"""
这是一个二维列表
"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
