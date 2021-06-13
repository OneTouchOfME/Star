import matplotlib.pyplot as plt
fig,a =  plt.subplots(2,2)
#fig=figure
#a=axes
import numpy as np
x = np.arange(0,10,0.1)
fig.suptitle("trial period subplots")
a[0][0].plot(x,x*x,'r')
a[0][0].set_title('square')
a[0][1].plot(x,np.sqrt(x),color="yellow")
a[0][1].set_title('square root')
a[1][0].plot(x,np.exp(x),color="brown")
a[1][0].set_title('exp')
a[1, 1].plot(x,np.log10(x),color="blue")
a[1, 1].set_title('log')
plt.show()