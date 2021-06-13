import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
plt.title('Heart', fontsize=24)

y = np.sqrt(1-np.power(x, 2))+np.power(np.square(x), 1/3)
y1 = -np.sqrt(1-np.power(x, 2))+np.power(np.square(x), 1/3)
plt.plot(x, y, 'b')
plt.plot(x, y1, 'b')

# this is your text; first argument is x-coordinate, second argument y-coordinate
plt.text(0, 0.4, "P_square", fontsize=24, color="k", va="center", ha="center", backgroundcolor="w")

my_x_ticks = np.arange(-2, 2.5, 0.5)
my_y_ticks = np.arange(-2, 2.5, 0.5)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.fill_between(x, y, y1, hatch="..", facecolor="red", edgecolor="blue", alpha=0.9)
plt.grid(False)
plt.savefig('love_with_dots.png')
plt.show()