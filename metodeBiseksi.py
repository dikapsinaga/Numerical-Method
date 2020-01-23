fx = lambda x : x**5 - 10
a = float(input("Masukan a : "))
b = float(input("Masukan b : "))
if(fx(a)*fx(b)) < 0:
    while abs(fx(a)*fx(b)) > 0.000001:
        c = (a+b)/2
        if fx(a)*fx(c) < 0.0:
            b=c
        else:
            a = c
    print('Akar Persamaan adalah %f' % (c))
else:
        print("Penentuan a dan b salah")