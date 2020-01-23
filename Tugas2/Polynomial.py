import numpy as np
import matplotlib.pyplot as plt

x0 = np.array([1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,4,4,4,5,2,2,4,3,4,3,4,4,4,4,3,3,3,4,4,3,4,5,4,5,4,4,3,5,5,4,5,3,4,3,4,6,4,5,4,4])
y0 = np.array([67,62,109,83,91,88,137,131,122,122,118,115,131,143,142,123,122,138,135,146,146,145,145,144,140,150,152,157,155,153,154,158,162,161,162,165,171,171,162,169,167,188,100,109,150,140,170,150,140,140,150,150,140,150,150,150,160,140,150,170,150,150,150,150,150,150,160,140,160,130,160,130,170,170,160,180,160,170])

sigmax = 0
sigmay = 0
sigmaxiyi  = 0
sigmaxikuadrat = 0
sigmaxipangkat3 = 0
sigmaxipangkat4 = 0
sigmaxikuadratyi = 0
sigmae = 0

size = x0.size

for i in range(x0.size) :
    sigmax = sigmax + (x0[i])
    sigmay = sigmay + (y0[i])
    sigmaxiyi = sigmaxiyi + x0[i]*y0[i]
    sigmaxikuadrat = sigmaxikuadrat + np.power(x0[i],2)
    sigmaxipangkat3 = sigmaxipangkat3 + np.power(x0[i],3)
    sigmaxipangkat4 = sigmaxipangkat4 + np.power(x0[i],4)
    sigmaxikuadratyi = sigmaxikuadratyi+ np.power(x0[i],2)*y0[i]


print("sigma x : ",sigmax)
print("sigma y : ",sigmay)
print("sigma xi * yi : ",sigmaxiyi)
print("sigma xikuadrat : ",sigmaxikuadrat)
print("sigma xipangkat3 : ",sigmaxipangkat3)
print("sigma xipangkat4 : ",sigmaxipangkat4)
print("sigma xikuadrat * yi : ",sigmaxikuadratyi)


# Menghitung a0,a1 dan a2 menggunakan metode Eliminasi Gauss dan Subtitusi Mundur
a = np.array([[size, sigmax, sigmaxikuadrat, sigmay],
              [sigmax, sigmaxikuadrat, sigmaxipangkat3, sigmaxiyi],
              [sigmaxikuadrat, sigmaxipangkat3, sigmaxipangkat4, sigmaxikuadratyi]]
             )
np.array(a)
matrix = a.astype(float)

if matrix[0,0] == 0.0:
    raise Exception("Cannot be zero!")

n, m = matrix.shape

#Eliminasi Gauss
for i in range(0, n):  # row
    for j in range(i + 1, n):
        if matrix[j, i] != 0.0:
            multiplier = matrix[j, i] / matrix[i, i]
            matrix[j, i:m] = matrix[j, i:m] - multiplier * matrix[i, i:m]

# Subtitusi mundur
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
print(np.size(var))

# menghitung error Sr dan Sy/x
for i in range(x0.size):
    sigmae = sigmae + np.power((y0[i] - var[np.size(var)-1] - var[(np.size(var))-2]* x0[i]-var[(np.size(var))-3]*np.power(x0[i],2)),2)
print("Sr : ",sigmae)
print("Sy/x :",np.sqrt(sigmae/(size-2)))

# print(var[np.size()])
# untuk plotingan persamaan regresi dan titik
x = np.arange(0, 6, 0.01)
y = var[np.size(var)-1] + var[(np.size(var))-2]* x + var[(np.size(var))-3]*np.power(x,2)

prediction = 3.7
result = var[np.size(var)-1] + var[(np.size(var))-2]* prediction + var[(np.size(var))-3]*np.power(prediction,2)

plt.plot(x0,y0,'o')
plt.plot(x,y,'r-')
plt.plot(prediction,result,'ro')
plt.xlabel('Usia Ikan (Dalam Tahun)')
plt.ylabel('y=13.6223761618 + 54.0493119133 * x -4.7186647869*x^2 ')

plt.grid(True)
plt.show()
