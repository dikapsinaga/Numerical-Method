fx = lambda x: x**3-2*x**2+6*x-4
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
cpendekatan = b
er = 100.0
n = 1
print("Iterasi\ta\t\t\tb\t\t\tc\t\t\tfx\t\t\ter")
while abs(er) > 0.001:
        c = b - ((fx(b)*(b-a))/(fx(b)-fx(a)))
        csejati = c
        er = ((csejati - cpendekatan)/csejati)*100
        print("%d\t\t%f\t%f\t%f\t%f\t%f" % (n,a,b,c,fx(c),abs(er)))
        cpendekatan = csejati; n+=1
        a = b; b = c
# print("Akar persamaan adalah %f" % (b))

print(b)