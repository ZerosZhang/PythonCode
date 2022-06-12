"""
字典用于计数，列表为增加的项
将列表dragonLoot中的东西，放到字典inv中，自动增加计数
"""


def displayInventory(inventory: dict):
    print("存货清单:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("物品总数量: " + str(item_total))


def addToInventory(inventory: dict, addedItems: list):
    for _item in addedItems:
        inventory.setdefault(_item, 0)
        inventory[_item] += 1
    return inventory


inv = {'金币': 42, '绳子': 1}
# 新增加物品
dragonLoot = ['金币', '匕首', '金币', '金币', '垃圾']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

