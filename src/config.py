import numpy as np

def time_vec(fs=250,duration=1):
    return np.linspace(0, duration, fs)

def sine_wave(t, freq, amp):
    return amp * np.sin(2 * np.pi * freq * t)
