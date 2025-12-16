import numpy as np

t = np.linspace(0, 1, 250)

def wave():
    return np.sin(2 * np.pi * t)

delta = wave() * 2
theta = wave() * 6
alpha = wave * 10
mu = wave() * 11
sigma = wave() * 14
beta = wave * 20
gamma = wave() * 40
high_gamma = wave() * 80

print(delta[:5])
print(theta[:5])
print(alpha[:5])
print(mu[:5])
print(sigma[:5])
print(beta[:5])
print(gamma[:5])
print(high_gamma[:5])