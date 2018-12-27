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
def puntos(W,xG,N,k):
    plt.title('x vs u(x,t)')
    for j in range(N+1):
        plt.plot(xG,W[j],'b--')
        plt.axis([0,1,-1,1])
        f='sin(pi*x)*'
        c=exp((-1)*(pi**2)*j*k)
        f+=str(c)
        x=arange(float(0),float(1),0.00001)
        f_x=eval(f)
        plt.plot(x,f_x,'r--')
    plt.show()
print 'METODO DE DIFERENCIAS PROGRESIVAS'
print 'k=0.01'
print 'h=0.1'
print 'r=1'
print ''
#DATOS
l=float(1)
alfa=float(1)
m=10
N=50
L=vector(m)
u=vector(m-1)
#paso 1
h=l/float(m)
k=0.01
lamb=(alfa**2)*k/(h**2)
#paso 2
w=matriz(m+1,N+1)
for i in range(m+1):
    w[i][0]=sin(pi*i*h)
for j in range(N):
    for i in range(1,m):
        w[i][j+1]=(1-2*(alfa**2)*k/(h**2))*w[i][j]+(alfa**2)*k/(h**2)*(w[i+1][j]+w[i-1][j])
W=matriz(N+1,m+1)
for i in range(m+1):
    for j in range(N+1):
        W[j][i]=w[i][j]
xG=[]
for i in range(m+1):
    xG.append(i*h)    
for j in range(N+1):
    if j==N:
        print ''
        t=j*k
        print 't=',t
        print 'xi'.rjust(30),'w(i,%f)'.rjust(30)%j,'u(xi,%f)'.rjust(30)%t,'|u(xi,t)-w(i,%f)|'.rjust(30)%t
        for i in range(0,m):
            print str(xG[i]).rjust(30),repr(W[j][i]).rjust(30),repr(exp((-1)*(pi**2)*(t))*sin(pi*xG[i])).rjust(30),repr(abs(exp((-1)*(pi**2)*(t))*sin(pi*xG[i])-W[j][i])).rjust(30)
        print str(xG[m]).rjust(30),repr(W[j][m]).rjust(30),'0'.rjust(30)
puntos(W,xG,N,k)
sleep(13)
