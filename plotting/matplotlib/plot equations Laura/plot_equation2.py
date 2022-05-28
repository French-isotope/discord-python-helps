import copy
from re import X
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5, 6]
Y = [-0.9, 0, 2, 4.5, 8.3, 13, 18]

x_values = np.array([0, 1, 2, 3, 4, 5, 6])
y_values = np.array([-0.9, 0, 2, 4.5, 8.3, 13, 18])


def imprimirEcuaciones(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(str(a[i][j]), end=" ")
        print("| " + str(b[i]))


def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = copy.deepcopy(b)

    N = len(bAux)

    print("Las ecuaciones son: ")
    imprimirEcuaciones(aAux, bAux)
    print()

    for i in range(N):
        if aAux[i][i] == 0:
            for j in range(N):
                if aAux[j][i] != 0:
                    valor = aAux[i]
                    aAux[i] = aAux[j]
                    aAux[j] = valor

                    resultado = bAux[i]
                    bAux[i] = bAux[j]
                    bAux[j] = resultado

                    break

        divisor = aAux[i][i]
        for j in range(N):
            aAux[i][j] /= divisor

        bAux[i] /= divisor

        for j in range(N):
            if i != j:
                fact = -aAux[j][i] / aAux[i][i]

                for k in range(N):
                    aAux[j][k] += (aAux[i][k] * fact)

                bAux[j] += (bAux[i] * fact)

    return bAux


sumaX = 0
for i in X:
    sumaX += i

sumaY = 0
for i in Y:
    sumaY += i

sumaX2 = 0
for i in X:
    sumaX2 += i ** 2

sumaX3 = 0
for i in X:
    sumaX3 += i ** 3

sumaX4 = 0
for i in X:
    sumaX4 += i ** 4

multi = 0
for i in range(len(X)):
    multi += X[i] * Y[i]

multi2 = 0
for i in range(len(X)):
    multi2 += (X[i] ** 2) * Y[i]

a = [[len(X), sumaX, sumaX2], [sumaX, sumaX2, sumaX3], [sumaX2, sumaX3, sumaX4]]
b = [sumaY, multi, multi2]

matriz = gaussJordan(a, b)

for i in range(len(matriz)):
    print("x" + str(i + 1) + " = " + str(matriz[i]))
print()

ST = 0
for i in range(len(Y)):
    ST += (Y[i] - sumaY / len(Y)) ** 2

SR = 0
for i in range(len(X)):
    SR += (Y[i] - matriz[0] - matriz[1] * X[i] - matriz[2] * X[i] ** 2) ** 2

Desviacion = sqrt((ST) / (len(X) - 1))
Error = sqrt((SR) / (len(X) - 3))
Correlacion = sqrt((ST - SR) / (ST)) * 100

x_vals = list()
y_vals = list()

for x_val in range(-8, 9):
    x_vals.append(x_val)
    y_vals.append(matriz[0] + (matriz[1]) * x_val + matriz[2] * x_val ** 2)

print("Ecuación lineal: y = ", matriz[0], "+", matriz[1], "x  + ", matriz[2], "x^2")
print("Desviación Estándar tiene un valor de: " + str(Desviacion))
print("Error Estándar: " + str(Error))
print("Coeficiente de correlación: " + str(Correlacion) + "%")

plt.plot(x_values, y_values, 'o')
plt.xlim(-5, 5)
plt.ylim(-2, 5)
plt.plot(x_vals, y_vals)
plt.grid()
plt.show()
plt.ion()

