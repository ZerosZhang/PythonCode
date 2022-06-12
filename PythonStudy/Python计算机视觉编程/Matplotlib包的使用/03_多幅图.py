import matplotlib.pyplot as plt

plt.figure()

# 第一个axes
plt.subplot(2, 2, 1)  # 可以简写为 plt.subplot(221),不喜欢这种写法
plt.plot([0, 1], [0, 1])

# 第二个axes
plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])

# 第三个axes
plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 3])

# 第四个axes
plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 4])

plt.show()
