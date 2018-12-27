from math import *
from time import sleep
from Tkinter import *
from numpy import *
import matplotlib.pyplot as plt
def matriz(n,m):#DEFINA LA MATRIZ
    M=[]
    for i in range(n):
        M.append([float(0)]*m)
    return M
def vector(n): #DEFINE EL VECTOR
    v=[]
    for i in range(n):
        v.append(float(0))
    return v
def puntos(xG,uG,N,k):
    plt.title('x vs u(x,t)')
    for j in range(N+1):
        plt.plot(xG,uG[j],'b--')
        plt.axis([0,1,-1,1])
        #f='sin(pi*x)*'
        #c=exp((-1)*(pi**2)*j*k)
        #f+=str(c)
        #x=arange(float(0),float(1),0.00001)
        #f_x=eval(f)
        #plt.plot(x,f_x,'r--')
    plt.show()
print 'Metodo de Crank-Nicolson'
print ''
print 'k=0.001, h=0,1'
print 'r=0.1'
#DATOS
l=float(1)
alfa=float(1)
m=10
N=50
w=vector(m+1)
L=vector(m)
u=vector(m-1)
#paso 1
h=l/float(m)
k=0.001
lamb=(alfa**2)*k/(h**2)
w[m]=0
#paso 2
for i in range(1,m):
    w[i]=sin(pi*i*h)   #w[i]=f(i*h)

#paso 3
L[1]=1+lamb
u[1]=(-1)*lamb/(2*L[1])

#paso 4
for i in range(2,m-1):
    L[i]=1+lamb+lamb*u[i-1]/2
    u[i]=(-1)*lamb/(2*L[i])
#paso 5
L[m-1]=1+lamb+lamb*u[m-2]/2

#paso 6
xG=[]
for i in range(m+1):
    xG.append(i*h)
uG=matriz(N+1,m+1)
for i in range(m+1):
    uG[0][i]=sin(pi*xG[i])
for j in range(1,N+1):
    #paso 7
    t=j*k
    z=vector(m)
    z[1]=((1-lamb)*w[1]+(lamb/2)*w[2])/L[1]
    #paso 8
    for i in range(2,m):
        z[i]=((1-lamb)*w[i]+(lamb/2)*(w[i+1]+w[i-1]+z[i-1]))/L[i]
    #paso 9
    w[m-1]=z[m-1]
    #paso 10
    i=m-2
    while i>=1:
        w[i]=z[i]-u[i]*w[i+1]
        i=i-1
    #paso 11
    #print 'xi                    wi---> u(xi,t)'
    #print '0             0'
    for i in range(1,m):
        uG[j][i]=w[i]
    uG[j][m]=0
    #for i in range(1,m):
    #    x=i*h
    
        #print x,'        ',w[i]
    #print '0             0'

for j in range(N+1):
    if j==N:
        print ''
        t=j*k
        print 'xi'.rjust(30),'w(i,%f)'.rjust(30)%t,'u(xi,t)'.rjust(30),'|u(xi,t)-w(i,%f)|'.rjust(30)%t
        for i in range(0,m):
            print str(xG[i]).rjust(30),repr(uG[j][i]).rjust(30),repr(exp((-1)*(pi**2)*(t))*sin(pi*xG[i])).rjust(30),repr(abs(exp((-1)*(pi**2)*(t))*sin(pi*xG[i])-uG[j][i])).rjust(30)
        print str(xG[m]).rjust(30),repr(uG[j][m]).rjust(30),'0'.rjust(30)
puntos(xG,uG,N,k)
sleep(13)
