import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1, 1, 50)
y1 = 2 * x

plt.figure()
plt.plot(x, y1, 'r--')

plt.xlim((-1, 2))
plt.ylim((-2, 3))

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

# 这里额外使用了latex语法
plt.yticks([2 * _ for _ in new_ticks],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$perfect$'])

plt.show()
