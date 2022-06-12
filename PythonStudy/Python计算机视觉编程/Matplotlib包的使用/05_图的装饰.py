import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1, 1, 50)
y1 = 2 * x

plt.figure()
plt.plot(x, y1, 'r--')

plt.xlabel('x value')
plt.ylabel('y value')

plt.axis([-1, 2, -2, 3])
# 设置可视区域也可以使用下面的表达
# plt.xlim((-1, 2))
# plt.ylim((-2, 3))

plt.show()
