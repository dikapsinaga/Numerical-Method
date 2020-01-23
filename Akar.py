import math

nilai= 256
Es = 0.1
xk = 2
Er = 1000
i = 0
print("%s \t %s \t\t %s \t\t %s" %('i','xk','xb','Er'))
while Er>Es:
    xb = (xk + nilai/xk)/2
    Er= abs((xb-xk)) *100
    i+=1
    print("%d \t %f \t %f \t %f" %(i,xk,xb,Er))
    xk = xb

print('Nilai Math\t\t',math.sqrt(nilai))
print('Nilai Pendekatan',xk)
