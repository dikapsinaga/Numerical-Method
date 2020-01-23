import numpy as np


A = np.array([[2, -12],[1, 5]], dtype=float)
eigValue, eigVector = np.linalg.eig(A)
print(eigValue)
print(eigVector)

