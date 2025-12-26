import numpy as np

t = np.linspace(0, 1, 250)

def wave(freq, amp):
    return amp * np.sin(2 * np.pi * freq * t)

delta = wave(2, 100)
theta = wave(6, 50)
alpha = wave(10, 30)
mu = wave(11, 20)
sigma = wave(14, 15)
beta = wave(20, 10)
gamma = wave(40, 5)
high_gamma = wave(80, 2)

print(delta[:5])
print(theta[:5])
print(alpha[:5])
print(mu[:5])
print(sigma[:5])
print(beta[:5])
print(gamma[:5])
print(high_gamma[:5])
