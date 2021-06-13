import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0, 10, 0.1)
y1=np.sin(x)
y2=np.cos(x)



plt.plot(x, y, label='sine', linewidth=3)

plt.title("$y_1=sin(x)$")

plt.legend()

plt.show()

