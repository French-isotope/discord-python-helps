import autograd.numpy as np
import matplotlib.pyplot as plt


"""
Mouhssine — Hier à 23:50
Hi everyone, https://paste.pythondiscord.com/itarazizircould, im trying here to numerically compute the output of a 
5*12 jacobian matrix containing the derivatives of a 5 dimension function in respect of 12 parameters. 
Can annyone help me with fixing this error "<lambda>() missing 1 required positional argument: 'x' 

it's rare but does happen: error in the library
in that case upgrading or downgrading usually fixes it
[00:27]
or manually changing, but that's more risky

Zephyrite — Aujourd’hui à 00:28
like most ML libs, it's got no docs, no comments and hasn't been updated in years...

Mouhssine — Aujourd’hui à 00:42
I guess there is no fixing it
[00:42]
thanks for the attention given anyways

"""

def HCVModel(x,params):
    s=params["s"]
    d=params["d"]
    beta=params["beta"]
    a=params["a"]
    p=params["p"]
    k=params["k"]
    mu=params["mu"]
    q=params["q"]
    g=params["g"]
    c=params["c"]
    h=params["h"]
    b=params["b"]

    xdot=np.array([s-d*x[0]-beta*x[2]*x[0],beta*x[2]*x[0]-a*x[1]-p*x[1]*x[3],k*x[1]-mu*x[2]-q*x[2]*x[4],c*x[1]*x[3]-b*x[3],g*x[2]*x[4]-h*x[4]])

    return xdot

def RK4(f,x0,t0,tf,dt):
    t=np.arange(t0,tf,dt)
    nt=t.size
    nx=x0.size
    x=np.zeros((nx,nt))
    x[:,0]=x0
    for k in range(nt-1):
        k1=dt*f(t[k],x[:,k])
        k2=dt*f(t[k]+dt/2,x[:,k]+k1/2)
        k3=dt*f(t[k]+dt/2,x[:,k]+k2/2)
        k4=dt*f(t[k]+dt,x[:,k]+k3)
        dx=(k1+2*k2+2*k3+k4)/6
        x[:,k+1]=x[:,k]+dx
    return x,t

f = lambda t, x : HCVModel(x,params)
params={"s":10*10**4,"d":10*10**-1,"beta":0,"a":10*10**-3,"p":10*10**-3,"k":10*10**-3,"mu":10*10**-3,"q":10*10**-3,"g":0,"c":0,"h":10*10**-3,"b":10*10**-3}
x0=np.array([10000,2,3,1,1.5])
t0=0
tf=100
dt=10**-2

x, t = RK4(f,x0,t0,tf,dt)



from autograd.scipy.integrate import odeint
from autograd import jacobian

s=10*10**4
d=10*10**-1
beta=0
a=10*10**-3
p=10*10**-3
k=10*10**-3
mu=10*10**-3
q=10*10**-3
g=0
c=0
h=10*10**-3
b=10*10**-3

dCdteta=jacobian(f,0)

teta_sensitivity = dCdteta(np.array([s,d,beta,a,p,k,mu,q,g,c,h,b]))

s_sensitivity=teta_sensitivity[:0,0]
d_sensitivity=teta_sensitivity[:0,1]
beta_sensitivity=teta_sensitivity[:0,2]
a_sensitivity=teta_sensitivity[:0,3]
p_sensitivity=teta_sensitivity[:0,4]
k_sensitivity=teta_sensitivity[:0,5]
mu_sensitivity=teta_sensitivity[:0,6]
q_sensitivity=teta_sensitivity[:0,7]
g_sensitivity=teta_sensitivity[:0,8]
c_sensitivity=teta_sensitivity[:0,9]
h_sensitivity=teta_sensitivity[:0,10]
b_sensitivity=teta_sensitivity[:0,11]
plt.plot(tspan, np.abs(fds), label='fd dC/ds')
plt.plot(tspan, np.abs(fdd), label='fd dC/dd')
plt.plot(tspan, np.abs(fdd), label='fd dC/dd')
plt.plot(tspan, np.abs(fdbeta), label='fd dC/dbeta')
plt.plot(tspan, np.abs(fda), label='fd dC/da')
plt.plot(tspan, np.abs(fdp), label='fd dC/dp')
plt.plot(tspan, np.abs(fdk), label='fd dC/dk')
plt.plot(tspan, np.abs(fdmu), label='fd dC/dmu')
plt.plot(tspan, np.abs(fdq), label='fd dC/dq')
plt.plot(tspan, np.abs(fdg), label='fd dC/dg')
plt.plot(tspan, np.abs(fdc), label='fd dC/dc')
plt.plot(tspan, np.abs(fdh), label='fd dC/dh')
plt.plot(tspan, np.abs(fdb), label='fd dC/db')
plt.xlabel('t')
plt.ylabel('sensitivity')
plt.show()