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


figure, (axis1, axis2) = plt.subplots(2)

figure.suptitle("test")
# height vs time
axis1.plot(time, height)
axis1.grid()
axis1.set_title('height vs time')
#axis1.xlabel('time')
#axis1.ylabel('height')

# velocity vs time
axis2.plot(time, velocity)
axis2.grid()
axis2.set_title('velocity vs time')
#axis2.xlabel('time')
#axis2.ylabel('velocity')

figure.tight_layout() # better separate each plots

plt.show()
