"""
统计一段字符串中所有字符的个数，不包括标点与空格

包含的知识点：
1. 字符串转化为小写
2. 判断字符是不是字母
3. setdefault函数：判断键是否在字典中，如果不在，则设置为默认值
4. 对字典进行排序
5. 访问字典
6. get函数：读取键对应的值，如果键不存在，则为默认值
"""

import pprint

message = 'It was a bright cold day in April, ' \
          'and the clocks were striking thirteen.'
message_lower = message.lower()  # 转化为小写

count = {}  # 初始化字典
for character in message_lower:
    if character.isalpha():  # 判断是否为字母
        count.setdefault(character, 0)
        count[character] += 1

count_sort = sorted(count.items())  # 对字典进行排序
for key, value in count_sort:
    print(f"{key} : {value}")

print(f"字母A共有 {count.get('a')} 个")
print(f"字母Z共有 {count.get('z')} 个")  # 默认值为None
print(f"字母Z共有 {count.get('z', 0)} 个")

# 另一种显示字典的方法，比较优雅
pprint.pprint(count)
