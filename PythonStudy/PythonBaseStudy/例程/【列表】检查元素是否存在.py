"""
检查列表中是否存在某个值
"""

example = ['red', 'yellow', 7]
print(f"7 in list_a : {7 in example}")

"""
检查字典中是否存在某个键
"""
spam = {'name': 'Bob', 'age': 7}
print('name' in spam)  # 简写版本，等于['name' in spam.keys()]
print('color' in spam.keys())
print('Bob' in spam.values())
