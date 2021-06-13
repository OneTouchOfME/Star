import numpy as np
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(1, 2)
x = np.arange(0, 2 * np.pi, 0.01)  # Angle range 0-2*pi, divided into 1024 equal parts
y = 1-np.sin(x)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# plt.axes(polar=True)    # Turn on polar coordinate mode
# plt.plot(x, y, color="r")
# spiral r=theta
r = np.arange(0, 2, 0.01)  # you can increase 2 -> 6 and see numbers of circles
theta = 2 * np.pi * r


ax.plot(theta, r)
ax.set_rticks([])  # to remove label of concentrated circle
# plt.fill_between(x, y, color='r')
plt.grid(False)
plt.show()
