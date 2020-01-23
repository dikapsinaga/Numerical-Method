import numpy as np
# x = np.linspace(0.9,1.2,100)
fx = lambda x : x**3 -2*(x**2) + 6*x -4.0


a = float(input("Masukan a : "))
b = float(input("Masukan b : "))

Er = 1000
cp = a

counter = 0
if(fx(a)*fx(b)) < 0:
    # print('n\t\ta\t\tb\t\tc\t\tfx\t\tErr')
    print('Iterasi \t a \t\t b \t\tNilai Tengah\tfx(a)\tfx(b)\t\tfx(c)\t\tfac \t\t Err')

    while abs(Er) > 0.001:
        c = b - (fx(b) * (a - b)) / (fx(a) - fx(b))
        cc = c
        Er = ((cc-cp)/cc)*100
        # print("%d\t%f %f %f %f %f %f %f" % (counter, a, b, c, fx(c), abs(Er),fx(a),fx(b)))
        print("%2d\t%10.2f\t%10.2f\t%10.8f\t%10.8f\t%10.8f\t%10.8f\t%10.8f\t%f"%(counter,a,b,c,fx(a),fx(b),fx(c),fx(a)*fx(c),abs(Er)))

        cp = cc
        counter=counter+1
        if fx(a)*fx(c) < 0.0:
            b=c
        else:
            a = c
    print('Akar Persamaan adalah %f' % (c))
else:
    print("Penentuan a dan b salah")
