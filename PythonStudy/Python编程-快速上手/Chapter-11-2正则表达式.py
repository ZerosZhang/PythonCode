# strip()的正则表达式版本

import re


def strip_regex(_str, _re_str=None):
    if _re_str:
        # 将_re_str从_str中去除
        replace_regex = re.compile(_re_str)
        print(replace_regex.sub('', _str), end='.\n')
    else:
        # 从该字符串首尾去除空白字符
        replace_regex = re.compile(r'^(\s*)(.*?)(\s*)$')  # (.*?)表示非贪心模式的任意字符串
        print(replace_regex.sub(r'\2', _str), end='.\n')  # 这里的\2表示用(.*?)来代替所有字符串


strip_regex('   AAABBAA AAA   ')  # 输出结果"AAABBAA AAA."
strip_regex('   AAABBAA AAA')  # 输出结果"AAABBAA AAA."
strip_regex('AAABBAA AAA   ')  # 输出结果"AAABBAA AAA."
strip_regex('   BAACABBAA AABBBA   ', 'B')  # 输出结果"   AACAAA AAA   ."
