import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.7, 0.8, 0.01)
y = x**3 -2*(x**2) + 6*x -4
plt.plot(x,y,'-')
plt.xlabel('X');
plt.ylabel('Y');
plt.grid(True)
plt.show()