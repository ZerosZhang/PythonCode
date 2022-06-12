import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y1 = 2 * x + 10
y2 = x ** 2

plt.plot(x, y1, 'r--')
plt.plot(x, y2, linewidth=5)
plt.show()
