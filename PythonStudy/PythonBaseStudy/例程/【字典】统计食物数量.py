import pprint

"""
统计所有的食物的个数

1. setdefault函数
2. get函数
3. pprint
"""


def totalBrought(guests):
    count = {}
    for k, v in guests.items():
        for _k, _v in v.items():
            count.setdefault(_k, 0)
            count[_k] = count[_k] + v.get(_k, 0)
    return count


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

print('Number of things being brought:')
pprint.pprint(totalBrought(allGuests))
