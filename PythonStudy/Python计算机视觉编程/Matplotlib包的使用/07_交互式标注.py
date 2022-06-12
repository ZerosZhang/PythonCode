import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2 * x + 1

plt.plot(x, y)
"""
左键增加
右键删除
中键终止
"""

print("在图中点击三个点...")
click = plt.ginput(3)
print(f'点到了{click}')

plt.show()
