import numpy as np
import matplotlib.pyplot as plt

fx = lambda x : x**3 -2*(x**2) + 6*x -4.0
# x = np.linspace(3.0,6.0,100)

# y = np.sin(10*x) + np.cos(3*x)

a = float(input("Masukan a : "))
b = float(input("Masukan b : "))

Er = 10000
cp = a

counter = 0
if(fx(a)*fx(b)) < 0:
    print('Iterasi \t a \t\t b \t\t c \t\t fx \t Err')
    while abs(Er) > 0.5:
        c = b- (fx(b)*(a-b))/(fx(a)-fx(b))
        cc = c
        Er = ((cc-cp)/cc)*100
        print("%d\t%f %f %f %f %f"%(counter,a,b,c,fx(c),abs(Er)))
        cp=cc
        counter=counter+1
        if fx(a)*fx(c) < 0.0:
            b=c
        else:
            a = c
            # print('Akar Persamaan adalah %f' % (c))
else:
    print("Penentuan a dan b salah")
