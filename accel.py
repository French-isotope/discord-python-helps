import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt

# Init vars
h = 3000 # meters
v = 0 # m/s
g = -9.81 # m/s^2
t = 0 # sec
tmax = 30 # sec
dt = 1 # sec

# Init lists
height = []
velocity = []
time = []

height.append(h)
velocity.append(v)
time.append(t)


def derivs(v, g):
    dhdt = v
    dvdt = g

    return dhdt, dvdt

while t<=tmax:
    dhdt, dvdt = derivs(v, g)

    # update height and velocity
    hnew = h + dhdt * dt
    vnew = v + dvdt * dt

    height.append(hnew)
    velocity.append(vnew)

    h = hnew
    v = vnew

    # increasing time
    t += dt

    time.append(t)


figure, axis = plt.subplots(1, 2)

# height vs time
axis[0,0].plot(time, height)
axis[0,0].grid()
axis[0,0].title('height vs time')
axis[0,0].xlabel('time')
axis[0,0].ylabel('height')

# velocity vs time
axis[0,1].plot(time, velocity)
axis[0,1].grid()
axis[0,1].title('velocity vs time')
axis[0,1].xlabel('time')
axis[0,1].ylabel('velocity')

plt.show()
