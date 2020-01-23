
import numpy as np
import matplotlib.pyplot as plt

x0 = np.array([1,2,3,4,5,6])
y0 = np.array([64.5,100.4285714,134.8947368,153.8292683,166.125,170])

n = x0.size
print(n)

x = np.arange(0, 10, 0.01)
L = 0
prediction = 3.7
result =0
for i in range(0,n):
    pi = 1
    pires=1
    for j in range(0,n):
        if(i!=j):
            pi = pi * (x - (x0[j])) /(x0[i] -x0[j])
            pires = pires * (prediction - (x0[j])) /(x0[i] -x0[j])
    L = L + (pi*y0[i])
    result = result + (pires*y0[i])

# plt.plot(x0,y0,'o')
plt.plot(x,L,'r-')
# plt.plot(prediction,result,'ro')
plt.xlabel('Usia Ikan (Dalam Tahun)')
plt.ylabel('Panjang Ikan (Dalam mm)')

plt.grid(True)
plt.show()


# from scipy.interpolate import lagrange
#
# xx = np.array([1,2,3,4,5,6])
# yy = np.array([62,100.4285714,134.8947368,153.8292683,166.125,170])
#
# poly= lagrange(xx,yy)
#
# from numpy.polynomial.polynomial import Polynomial
#
# pol = 0
#
# print(Polynomial(poly).coef)
#
# f= interpolate.lagrange(xx,yy)
# y=f(x)
#
# plt.plot(xx,yy,'o')
# plt.plot(x,y,'r-')
# plt.grid(True)
# plt.show()
