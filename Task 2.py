import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

N = 100000

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

points_under_curve = np.sum(y_rand <= f(x_rand))

area_under_curve = (points_under_curve / N) * (b - a) * f(b)
integral_estimate = area_under_curve

result, error = spi.quad(f, a, b)

print("Інтеграл (Монте-Карло):", integral_estimate)
print("Інтеграл (quad):", result)
