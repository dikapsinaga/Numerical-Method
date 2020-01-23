import numpy as np
import matplotlib.pyplot as plt

x0 = np.array([1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,4,4,4,5,2,2,4,3,4,3,4,4,4,4,3,3,3,4,4,3,4,5,4,5,4,4,3,5,5,4,5,3,4,3,4,6,4,5,4,4])
y0 = np.array([67,62,109,83,91,88,137,131,122,122,118,115,131,143,142,123,122,138,135,146,146,145,145,144,140,150,152,157,155,153,154,158,162,161,162,165,171,171,162,169,167,188,100,109,150,140,170,150,140,140,150,150,140,150,150,150,160,140,150,170,150,150,150,150,150,150,160,140,160,130,160,130,170,170,160,180,160,170])

sigmax = 0
sigmay = 0
sigmaxiyi  = 0
sigmaxikuadrat = 0
sigmae = 0

size = x0.size

for i in range(x0.size) :
    sigmax = sigmax + (x0[i])
    sigmay = sigmay + (y0[i])
    sigmaxiyi = sigmaxiyi + x0[i]*y0[i]
    sigmaxikuadrat = sigmaxikuadrat + np.power(x0[i],2)

print("sigma x : ",sigmax)
print("sigma y : ",sigmay)
print("sigma xi * yi : ",sigmaxiyi)
print("sigma xikuadrat : ",sigmaxikuadrat)

# # menghitung a0 dan a1 menggunakan rumus
# ratax = sigmax/size
# ratay = sigmay/size
#
# a1 = (size * sigmaxiyi - sigmax*sigmay)/ (size*sigmaxikuadrat - np.power(sigmax,2))
# a0 = ratay - a1 * ratax
# print("a0 : ",a1)
# print("a1 : ",a0)
#
# print("")
#
# Jika menggunakan error Sr dan Sy/x
# for i in range(x0.size):
#     sigmae = sigmae + np.power((y0[i] - a0 - (a1*x0[i])),2)
# print("Sr : ",sigmae)
# print("Sy/x :",np.sqrt(sigmae/(size-2)))
#
#
#
# # Untuk plotingan persamaan regresi dan titik
# x = np.arange(0, 6, 0.01)
# y = a0 + a1 * x
# plt.plot(x0,y0,'o')
# plt.plot(x,y,'r-')
# plt.grid(True)
# plt.show()


# Mencari a0 dan a1 menggunakan metode Eliminasi Gauss dan Subtitusi Mundur
a = np.array([[size, sigmax,sigmay],
              [sigmax, sigmaxikuadrat,sigmaxiyi]])

np.array(a)
matrix = a.astype(float)

if matrix[0,0] == 0.0:
    raise Exception("Cannot be zero!")

n, m = matrix.shape

# Eliminasi Gauss
for i in range(0, n):
    for j in range(i + 1, n):
        if matrix[j, i] != 0.0:
            multiplier = matrix[j, i] / matrix[i, i]
            matrix[j, i:m] = matrix[j, i:m] - multiplier * matrix[i, i:m]


# Subtitusi munndur
var = []
substractor = 0.0

for i in range(n - 1, -1, -1):  # row
    for j in range(0, n - i):  # column
        if j == 0:
            substractor = 0
        else:
            substractor = substractor + matrix[i, m - j - 1] * var[j - 1]

    var.append((matrix[i, m - 1] - substractor) / matrix[i, i])

print("menggunakan metode Gauss")
print("var",var)

# Jika menggunakan error Sr dan Sy/x
for i in range(x0.size):
    # sigmae = sigmae + np.power((y0[i] - var[np.size(var)-1] - var[(np.size(var))-2]* x0[i]-var[(np.size(var))-3]*np.power(x0[i],2)),2)
    sigmae = sigmae + np.power((y0[i] - var[np.size(var)-1] - var[(np.size(var))-2]* x0[i]),2)
print("Sr : ",sigmae)
print("Sy/x :",np.sqrt(sigmae/(size-2)))

print(np.sqrt(sigmae))
x = np.arange(0, 6, 0.01)
y = var[np.size(var)-1] + var[(np.size(var))-2]* x

prediction=3.7
result= var[np.size(var)-1] + var[(np.size(var))-2]* prediction

plt.plot(x0,y0,'o')
plt.plot(prediction,result,'ro')
plt.plot(x,y,'r-')

plt.xlabel('Usia Ikan (Dalam Tahun)')
plt.ylabel('y=62.6489835431 + 22.3122942885 * x')
plt.grid(True)
plt.show()
