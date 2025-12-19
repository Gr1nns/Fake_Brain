import numpy as np
import matplotlib.pyplot as plt
import random as rd

t = np.linspace(0, 1, 250)

def wave(freq, amp):
    return amp * np.sin(2 * np.pi * freq * t)

ampS = rd.uniform(0.5, 1.0) # Network Noise

# 1 = Hz,  2 = Amp
d1 = rd.uniform(0.5, 4.0)
d2 = rd.uniform(20.0, 200.0)

t1 = rd.uniform(4.0, 8.0)
t2 = rd.uniform(10.0, 100.0)

a1 = rd.uniform(8.0, 13.)
a2 = rd.uniform(5.0, 50.0)

m1 = rd.uniform(9.0, 12.0)
m2 = rd.uniform(5.0, 30.0)

s1 = rd.uniform(12.0, 16.0)
s2 = rd.uniform(5.0, 20.0)

b1 = rd.uniform(13.0, 30.0)
b2 = rd.uniform(1.0, 20.0)

g1 = rd.uniform(30.0, 60.0)
g2 = rd.uniform(0.5, 10.0)

hg1 = rd.uniform(60.0, 100.0)
hg2 = rd.uniform(0.1, 5.0)

banda = {
    "delta": (d1, d2),
    "theta": (t1, t2),
    "alpha": (a1, a2),
    "mu": (m1, m2),
    "sigma": (s1, s2),
    "beta": (b1, b2),
    "gamma": (g1, g2),
    "high_gamma": (hg1, hg2)
}

ondas = {}
for name, (freq, amp) in banda.items():
    ondas[name] = wave(freq, amp)

N1 = np.random.normal(0, 5, size=len(t)) # White Noise
N2 = np.sin(2 * np.pi * 60 * t) * ampS # Network Noise

EEG = sum(ondas.values())
EEG_real = EEG + N1 + N2

plt.plot(t, EEG_real)
plt.title("Bandas EEG") 
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
