#! /usr/bin/env nix-shell
#! nix-shell default.nix -i python

import numpy as np
import matplotlib.pyplot as plt
import math

x_values = np.array([1,2,3,4,5,6])
y_values = np.array([2.25,3,4.5,6,8.5,12])

x_pow2 = []
xlny = []
lny = []

for n in x_values:
    x_pow2.append(n**2)

for n in y_values:
    lny.append(math.log(n))

for n in range(len(x_values)):
    xlny.append(x_values[n]*lny[n])

x_pow2_sum = 0
lny_sum = 0
xlny_sum = 0

for n in x_pow2:
    x_pow2_sum+=n

for n in lny:
    lny_sum+=n

for n in xlny:
    xlny_sum+=n

x_sum = 0
x_mean = 0
lny_sum = 0
lny_mean = 0

for n in x_values:
    x_sum+=n

for n in lny:
    lny_sum+=n

x_mean = x_sum/len(x_values)
lny_mean = lny_sum/len(lny)

a1 = (len(x_values)*xlny_sum-x_sum*lny_sum)/(len(x_values)*x_pow2_sum-(x_sum**2))
a0 = (lny_mean-a1*x_mean)

alpha = math.exp(a0)
beta = a1

x_vals = list()
y_vals = list()

for x_val in range(-8, 9):
    x_vals.append(x_val)
    y_vals.append(-0.9428 + 0.5642 * x_val + 0.4357 * x_val**2)
#    y_vals.append(alpha * (math.e ** (beta * x_val)))

x_vals2 = list()
y_vals2 = list()

for x_val2 in range(-8, 9):
    x_vals2.append(x_val2)
    y_vals2.append(alpha * (math.e ** (beta * x_val2)))


print(beta)
print(alpha)
print(f'La ecuación hallada es: y = {alpha}e^{beta}x')

plt.plot(x_values, y_values, 'o', label='first plot')
plt.plot(x_values, a0 + a1*x_values, label='second plot')
plt.plot(x_values, alpha * math.e ** (beta * x_values), label='alpha * (math.e ** (beta * x_val)) little', linewidth=4)
plt.plot(x_vals, y_vals, label='-0.9428 + 0.5642 * x_val + 0.4357 * x_val**2')
plt.plot(x_vals2, y_vals2, label='alpha * (math.e ** (beta * x_val)) large')
plt.title('Test big title for Laura')
plt.xlabel('yes')
plt.ylabel('nono')
plt.grid(axis = 'y')

plt.legend(loc='center')
plt.legend(loc='upper center')

plt.show()
