"""
剪贴板操作
"""

import pyperclip


"""
复制前：
运行这个程序
它将取代剪贴板上的文本
新的文本每一行都以星号开始
现在程序完成了
可以在剪贴板中复制一些文本
试着运行它
"""

text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]  # 在每句话的前面加个*号
text = '\n'.join(lines)
pyperclip.copy(text)  # 现在可以粘贴


"""
* 复制前：
* 运行这个程序
* 它将取代剪贴板上的文本
* 新的文本每一行都以星号开始
* 现在程序完成了
* 可以在剪贴板中复制一些文本
* 试着运行它
"""
