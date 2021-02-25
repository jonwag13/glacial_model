import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

#####################################
#variables
#####################################

b_0 = 0
s =  10    #constant slope
xmin = b_0
xmax = 21000
x =  np.arange(xmin,xmax,1)    #x position
beta = 1    #constant balance gradient
h = np.arange(-100,0,1)     #height
E = -5000      #equilibrium line altitude
rho = 900
g = 10
H_m = 250
#####################################
#Equations
#####################################

#2.1.1
def b_x(b_0,s,x):
    return (b_0 - s * x)


#2.1.2
b_dot = beta*(h - E)

#2.1.3
#this = 0

#2.1.4
def L(H_m,b_0,E,s):
    return 2*(H_m + b_0 - E)/s


#2.1.5
#H_m = (1/L) * integrate(H,0,L)

#2.1.6
#tao_0 = p*g*s*H_m

#2.1.7
#L = (2/s)(10*(1/s)+b_0 - E)



#####################################
#Plot
#####################################
s = .05
E = -255
H_m = 255

s2 = .10
E2 = -255
H_m2 = 255

s3 = .20
E3 = -255
H_m3 = 255

print(L(H_m,b_0,E,s)/1000)
plt.plot(x,b_x(b_0,s,x),c='b')
plt.plot(x,b_x(b_0,s,x)+H_m,c='b')
plt.hlines(E,xmin,xmax,colors='blue')
plt.scatter(L(H_m,b_0,E,s),b_x(b_0,s,L(H_m,b_0,E,s)),c='b')

print(L(H_m2,b_0,E2,s2)/1000)
plt.plot(x,b_x(b_0,s2,x),c='red')
plt.plot(x,b_x(b_0,s2,x)+H_m2,c='red')
plt.hlines(E2,xmin,xmax,colors='red')
plt.scatter(L(H_m2,b_0,E2,s2),b_x(b_0,s2,L(H_m2,b_0,E2,s2)),c='red')

print(L(H_m3,b_0,E3,s3)/1000)
plt.plot(x,b_x(b_0,s3,x),c='green')
plt.plot(x,b_x(b_0,s3,x)+H_m3,c='green')
plt.hlines(E3,xmin,xmax,colors='green')
plt.scatter(L(H_m3,b_0,E3,s3),b_x(b_0,s3,L(H_m3,b_0,E3,s3)),c='green')

plt.show()
