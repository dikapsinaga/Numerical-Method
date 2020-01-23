import numpy as np

A = np.array([[2,-12],[1,-5]], dtype=float)
eigenValue,eigenVector = np.linalg.eig(A)
print(eigenValue)
print(eigenVector)