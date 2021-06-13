import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#plt.subplot(1, 2, 1)
#plt.plot(x, y1, color="red")
plt.subplot(2, 1, 1)
plt.plot(x, y1, color="red")


#plt.subplot(1, 2, 2)
#plt.plot(x, y2, color="blue")
plt.subplot(2, 1, 2)
plt.plot(x, y2, color="red")

plt.show()
plt.title("subplot title")

# plt.legend()

# plt.show()

