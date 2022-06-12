import matplotlib.pyplot as plt

plt.figure()

# 注意subplot中的参数
plt.subplot(2, 1, 1)  # 分成两行，第一行分1列，然后占用的是1,2,3
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)  # 分两行，第二行分3列，然后是第二行起始为4
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])

plt.show()
