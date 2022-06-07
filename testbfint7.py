import numpy as np
from scipy.optimize import curve_fit
import scipy.fftpack
from scipy.fftpack import fftfreq
from scipy.fft import fft

from scipy.signal import blackman, flattop, boxcar
import matplotlib.pyplot as plt
import random

N = 44100 # Number of samples
T = 250/N # 400 ns
#time = np.linspace(0, T, N)
time = np.linspace(0, T, int(N * T), endpoint=False)
print(time.shape)
dt = np.diff(time)[0]

nano = 1e-9
spacing = 0.0001 #spacing
w0 = 0.0101 # in gigahertz Ramsey or Free Induction frequency
omega = np.linspace(w0, w0+100*spacing, 1)
omega_noise = omega + 0.001*random.gauss(0.1,3)


def I_test(omega, t):
    y = np.cos((2 * np.pi) * t*omega)
    return y

w0 = np.linspace(1, 10000, 3)
print(w0)
fig1, ax = plt.subplots()
for w in w0:
    plt.plot(time, I_test(w, time))

plt.title('Time space')
plt.ylabel('Intensity', fontsize = 20)
plt.xlabel('time', fontsize = 20)

fig2, ax = plt.subplots()
fft_pts = int(N*T)
buff = -1
for w in w0:
    xf = fftfreq(fft_pts, 1/N)
    yf = fft(I_test(w, time))
    plt.plot(xf[:fft_pts//2][:buff], np.abs(yf[:fft_pts//2])[:buff], label=f"wo = {w}")

plt.legend()
plt.ylabel('|$\hat{y}_n$|', fontsize = 20)
plt.xlabel('$freq_n$', fontsize = 20)
plt.show()
