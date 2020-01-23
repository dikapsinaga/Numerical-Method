import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,0.5,1000)
fx =lambda x :  0.5 * x ** 3 - 4 * x ** 2 + 7 * x - 2


plt.plot(x,fx(x),'b-')
plt.xlabel('X')
plt.ylabel('0.5 * x ** 3 - 4 * x ** 2 + 7 * x - 2')
plt.axhline(y=0, color='red')
plt.show()