import math
import numpy as np
import matplotlib.pyplot as plt

a = int(input("Masukan angka : "))


def faktorial(x):
    if(x<=1):
        return 1
    else :
        return x * faktorial(x-1)

hasil = faktorial(a)
print(hasil)

x = int(input("x : "))
n = int(input("n : "))


def eksponensial(x,n):
        if(n==0):
            return 1
        else:
            return math.pow(x,n) / faktorial(n) + eksponensial(x,n-1)

hasil = eksponensial(x,n)
print(hasil)

hasil_analitik = math.exp(2)
hasil_numerik1 = eksponensial(2,3)#orde 3
hasil_numerik2 = eksponensial(2,10)#orde 25
hasil_numerik3 = eksponensial(2,25)#Orde 100


#hitung error absolut dan relatif
error_absolut1 = math.fabs(hasil_analitik-hasil_numerik1)
error_relatif1= error_absolut1/hasil_analitik * 100

error_absolut2 = math.fabs(hasil_analitik-hasil_numerik2)
error_relatif2= error_absolut2/hasil_analitik * 100

error_absolut3 = math.fabs(hasil_analitik-hasil_numerik3)
error_relatif3= error_absolut3/hasil_analitik * 100

print("E1")
print(error_absolut1)
# print(error_relatif1)

print("E2")
print(error_absolut2)
# print(error_relatif2)

print("E3")
print(error_absolut3)
# print(error_relatif3)

x1 = np.arange(1,100,0.01)
y1= [item for item in (eksponensial(x1,100) for x1 in x1)]

print("SS")
print(y1)

plt.plot(x1,y1,'g-',label="fungsi")
plt.xlabel('Nilai x')
plt.ylabel('Eksponensial x')
plt.title('Kurva Eksponensial')
plt.legend(loc=4)
plt.show()
