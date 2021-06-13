import matplotlib.pyplot as plt

x=[1,2,3]
y=[2,3,1]

plt.plot(x, y, 'r', label='line', linewidth=1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("the graph tutorial")
plt.legend()
plt.show()