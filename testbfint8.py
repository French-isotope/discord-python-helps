import numpy as np
from scipy.optimize import curve_fit
import scipy.fftpack
from scipy.fftpack import fftfreq
from scipy.fft import fft

from scipy.signal import blackman, flattop, boxcar
import matplotlib.pyplot as plt
import random

N = 50 # Number of samples
T = 1000/N # 400 ns
time = np.linspace(0, T, int(N * T), endpoint=False)
print(time.shape)

w0 = 0.0101 # in gigahertz Ramsey or Free Induction frequency
#omega_lst = np.linspace(w0, w0+100*spacing, 1)

def I_test(t, omega):
    omega = omega + 0.001*random.gauss(0.1,3)
    y = np.cos((2 * np.pi) * t*omega) + 0.3*np.random.randn(len(time))
    return y

buff = 100
fig1, ax = plt.subplots()
plt.plot(time[:buff], I_test(time, w0)[:buff], label=f"w0 : {w0}")
plt.title('Time space')
plt.ylabel('Intensity', fontsize = 20)
plt.xlabel('time', fontsize = 20)

print(f"w0:{w0}")
Ilist = I_test(time, w0)

a,_ = curve_fit(I_test, time, np.array(Ilist))
print(a)
plt.plot(time[:buff], I_test(time, a[0])[:buff],label=f"w0 : {a[0]}")
plt.legend()
fig2, ax = plt.subplots()
fft_pts = int(N*T)
buff = 100

xf = fftfreq(fft_pts, 1/N)
yf = fft(I_test(time, w0))
plt.plot(xf[:fft_pts//2][:buff], np.abs(yf[:fft_pts//2])[:buff], label=f"w0 = {w0}")

xf = fftfreq(fft_pts, 1/N)
yf = fft(I_test(time, a[0]))
plt.plot(xf[:fft_pts//2][:buff], np.abs(yf[:fft_pts//2])[:buff], label=f"w0 = {a[0]}")

plt.legend()
plt.ylabel('|$\hat{y}_n$|', fontsize = 20)
plt.xlabel('$freq_n$', fontsize = 20)
plt.show()
