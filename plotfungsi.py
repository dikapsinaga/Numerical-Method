import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi,10000)
y = np.sin(7*x) + np.cos(2*x)
dydx = 7*np.cos(7*x)+ -2*np.sin(2*x)

# plotting data
plt.plot(x,y, 'b-'), plt.xlabel('X'),plt.ylabel('y=sin(7x) + cos(2x)')
# plt.plot(x,dydx, 'g-')
plt.title('Grafik Persamaan')
plt.axhline(y=0, color ='r')

n = len (dydx)
for i in range (n):
    if abs(dydx[i]) < 0.1 :
        plt.plot(x[i], y[i], 'ro')

plt.show()
