import numpy as np

t = np.linspace(0, 1, 250)
delta = np.sin(2 * np.pi * 2 * t)
theta = np.sin(2 * np.pi * 6 * t)
alpha = np.sin(2 * np.pi * 10 * t)
mu = np.sin(2 * np.pi * 11 * t)
sigma = np.sin(2 * np.pi * 14 * t)
beta = np.sin(2 * np.pi * 20 * t)
gamma = np.sin(2*np.pi * 40 * t)
high_gamma = np.sin(2 * np.pi * 80 * t)


print(delta[:5])
print(theta[:5])
print(alpha[:5])
print(mu[:5])
print(sigma[:5])
print(beta[:5])
print(gamma[:5])
print(high_gamma[:5])
