import numpy as np

def fourier(signal, fs):
    FFT = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=1/fs)
    magnitude = np.abs(FFT)

    mask = (freqs >= 4) & (freqs <= 40)

    return freqs[mask], magnitude[mask]
