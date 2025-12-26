import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 250)

def wave(freq, amp):
    return amp * np.sin(2 * np.pi * freq * t)

banda = {
    "delta": (2, 100),
    "theta": (6, 50),
    "alpha": (10, 30),
    "mu": (11, 20),
    "sigma": (14, 15),
    "beta": (20, 10),
    "gamma": (40, 5),
    "high_gamma": (80, 2)
}
ondas = {}
for name, (freq, amp) in banda.items():
    ondas[name] = wave(freq, amp)

EEG = sum(ondas.values())
plt.plot(t, EEG)
plt.title("Bandas EEG")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
