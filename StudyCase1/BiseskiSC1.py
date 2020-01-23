import numpy as np
x = np.linspace(0,3,100)
fx = lambda x : x ** 5 - 2 * x ** 3 + 10 * x - 5
a = float(input("Masukan a : "))
b = float(input("Masukan b : "))

Er = 1000
cp = a

counter = 0
if(fx(a)*fx(b)) < 0:
    print('n\t\ta\t\tb\t\tc\t\tfx\t\tErr')
    while abs(Er) > 0.01:
        c = (a+b)/2
        cc = c
        Er = ((cc-cp)/cc)*100
        print("%d\t%f %f %f %f %f" % (counter, a, b, c, fx(c), abs(Er)))
        cp=cc
        counter=counter+1
        if fx(a)*fx(c) < 0.0:
            b=c
        else:
            a = c
    print('Akar Persamaan adalah %f' % (c))
else:
    print("Penentuan a dan b salah")
