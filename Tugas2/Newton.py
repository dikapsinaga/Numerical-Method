import numpy as np
import matplotlib.pyplot as plt

xi = np.array([1,2,3,4,5,6])
yi = np.array([64.5,100.4285714,134.8947368,153.8292683,166.125,170])

length = 0;

for i in range(1,xi.size):
    length += i

print(length)
b0 = [0]*(xi.size)
btemp = [0]
btempCopy = [0]
counter = 0

for i in range(1,xi.size+1):
    btempCopy = [0]*(i)
    for j in range(i):
        if(j==0):
            b0[i-1] = yi[i-1]
            btempCopy[j] = yi[i-1]
        else:
            dif = (i-1)
            if(xi[dif]-xi[dif-j] == 0):
                b0[i-1] = 0
            else:
                b0[i-1] = (b0[i-1] - btemp[j-1]) / (xi[dif] - xi[dif - j])
            btempCopy[j] = b0[i-1]
    btemp = btempCopy

eq = ''
for i in range(len(b0)):
    eq = eq + str(b0[i])
    for j in range(i):
        eq += '*(x-%d)' % xi[j]
    if(i!=len(b0)-1):
        eq += '+'

print(eq)
fx = lambda x: eval(eq)

xplot = np.arange(0, 8, 0.01)
yplot = fx
plt.plot(xi,yi,'o')
plt.plot(xplot,fx(xplot),'r-')
plt.xlabel('Usia Ikan (Dalam Tahun)')
plt.ylabel('Panjang Ikan (Dalam mm)')
plt.grid(True)
plt.show()