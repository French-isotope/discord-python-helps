import numpy as np
from scipy.optimize import curve_fit

import scipy.fftpack
from scipy.fftpack import fftfreq
from scipy.fft import fft

from scipy.signal import blackman, flattop, boxcar
import matplotlib.pyplot as plt
import random

N = 100  # Number of samples
T = 400  # 400 ns
time = np.linspace(0, T, N)
dt = np.diff(time)[0]

nano = 1e-9
spacing = 0.0001  # spacing
w0 = 0.0101  # in gigahertz Ramsey or Free Induction frequency
omega = np.linspace(w0, w0 + 100 * spacing, 1)
omega_noise = omega + 0.001 * random.gauss(0.1, 3)


def I_noise(omega, t):  # this  gives the Intensity of the given omegas
    I = np.cos(2 * np.pi * omega * t) + 0.3 * np.random.randn(len(time))
    return I


# plt.plot(time,I_noise(w0,time))
Ilist = []
for om in omega_noise:
    Ilist.append(I_noise(om, time))

# Int = Ilist[0] # each component is an ensemble of NV centers

for i in Ilist:
    plt.plot(time, i)
# fig, ax = plt.subplots()
plt.title('Time space')
plt.ylabel('Intensity', fontsize=20)
plt.xlabel('time', fontsize=20)


def I(t, w):  # this function sets omega as a parameter to estimate what the, w, of the noisy data is
    I = np.cos(2 * np.pi * w * t)
    return I


a, _ = curve_fit(I, time, np.array(Ilist[0]), p0=[0.01])
plt.plot(time, I(time, a))

fig, ax = plt.subplots()
print(a[0])

for i in Ilist:
    f = fftfreq(len(time), np.diff(time)[0])
    yf = fft(i)
    plt.plot(f[:N // 2], np.abs(yf[:N // 2]))
    yff = fft(I(time, a[0]))
    plt.plot(f[:N // 2], np.abs(yff[:N // 2]))

plt.ylabel('|$\hat{y}_n$|', fontsize=20)
plt.xlabel('$freq_n$', fontsize=20)
plt.show()

