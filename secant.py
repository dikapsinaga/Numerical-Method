def secant(fungsi,x0,x1,threshold):# parameter fungsi berupa string, sedangkan x0,x1, dan threshold berupa bilangan
    fa = lambda x: eval(fungsi)
    error = 100.0
    n=0
    print("Iterasi\tx0\t\t\tx1\t\t\tfa(x1)\t\tfa(x0)\t\t\txn\t\t\terror")
    while abs(error) >= threshold:
        xn = x1 - ((fa(x1)*(x1-x0)) / (fa(x1)-fa(x0)))
        error = ((xn-x1)/xn) * 100
        print("%d\t\t%f\t%f\t%f\t%f\t%f\t%f" % (n,x0,x1,fa(x1),fa(x0),xn,error))
        x0=x1
        x1=xn
        n+=1;

        # print(xn)
        # print(error)
    return xn

hasil = secant('x**2 - 5',2,3,0.001)

print(hasil)