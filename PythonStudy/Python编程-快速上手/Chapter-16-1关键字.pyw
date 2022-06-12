"""
pyw表示Python运行该程序的时候，不会显示终端窗口
py Chapter-16-5.pyw save spam  剪贴板中当前的内容用关键字spam保存
py Chapter-16-5.pyw spam 将spam对应的内容重新加载到剪贴板中
py Chapter-16-5.pyw list 将所有的关键字列表复制到剪贴板中
py Chapter-16-5.pyw delete 删除所有关键字
py Chapter-16-5.pyw delete spam 删除spam关键字和值
"""

import shelve
import sys

import pyperclip

mcbShelf = shelve.open('mcb')
# 保存剪贴板内容
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        """
        参数为3个，且第二个参数为save时，将当前剪贴板的内容保存在第三个参数作为关键字的值中
        """
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        """
        参数为3个，且第二个参数为delete时，删除第三个参数的关键字
        """
        del mcbShelf[sys.argv[2]]
        print(f'删除{sys.argv[2]}')
elif len(sys.argv) == 2:
    # 列出关键词并加载内容
    if sys.argv[1].lower() == 'list':  # 如果只有一个命令行参数，首先检查是不是list
        """
        参数为2个，且第二个参数为list时，将所有的关键字作为列表显示出来/复制到当前剪贴板
        """
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        """
        参数为2个，且第二个参数为delete时，将删除所有关键字
        """
        mcbShelf.clear()
        print('删除所有关键字')
    elif sys.argv[1] in mcbShelf:
        """
        参数为2个，且第二个参数不是list，同时第二个参数在关键字列表中
        返回第二个参数作为关键字的值
        """
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(mcbShelf[sys.argv[1]])

mcbShelf.close()
