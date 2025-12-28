import numpy as np
import random as rd

# White Noise
def white_noise(t):
    return np.random.normal(0, 5, size=len(t))

def pink_noise(t):
    N = len(t)
    white = np.random.normal(0, 1, N)
    fft = np.fft.fft(white)

    freqs = np.fft.fftfreq(N)
    freqs[0] = 1.0
    fft = fft / np.sqrt(np.abs(freqs))


    pink = np.fft.ifft(fft).real
    pink = pink / np.std(pink)
    return pink

# Network Noise
def network_noise(t):
    amp = rd.uniform(0.5, 1.0)
    return amp * np.sin(2*np.pi*60*t + rd.uniform(0, 2*np.pi))

# Muscle Noise
def muscle_noise(t):
    A = rd.uniform(30, 150)
    emg_base = np.random.normal(0, A, size=len(t))

    gate = np.zeros(len(t))
    num_bursts = rd.randint(1, 4)

    for _ in range(num_bursts):
        start = rd.randint(0, len(t) - 1)
        duration = rd.randint(10, 75)
        end = min(start + duration, len(t))
        gate[start:end] = 1

    carrier = np.zeros(len(t))
    n_sines = 20

    for _ in range(n_sines):
        f = rd.uniform(40, 120)
        phase = rd.uniform(0, 2 * np.pi)
        carrier += np.sin(2 * np.pi * f * t + phase)

    carrier /= n_sines

    EMG = emg_base * carrier * gate
    return EMG

# EOG Noise
def eog_noise(t):
    A = rd.uniform(50, 300)
    freq = rd.uniform(0.2, 1.5)

    base = A * np.sin(2 * np.pi * freq * t)

    gate = (np.random.rand(len(t)) > 0.995).astype(float)
    gate = np.convolve(gate, np.ones(50)/50, mode='same')

    EOG = base * gate
    return EOG

# ECG Noise
def ecg_noise(t):
    hr = rd.uniform(60, 90)
    f = hr / 60
    A = rd.uniform(5, 20)

    phase = np.mod(t * f, 1)
    qrs = np.exp(-((phase - 0.05)**2)/0.0005)
    ECG = A * qrs
    return ECG

# Respiration Noise
def respiration_noise(t):
    A = rd.uniform(5, 30)
    freq = rd.uniform(0.2, 0.35)

    return A * np.sin(2 * np.pi * freq * t)
