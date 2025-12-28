import config as cf
import noise
import wave as w
from analysis import fourier

def generate_EEG():
    t = cf.time_vec()
    wn = noise.white_noise(t)
    pn = noise.pink_noise(t)
    nn = noise.network_noise(t)
    EMG = noise.muscle_noise(t)
    EOG = noise.eog_noise(t)
    ECG = noise.ecg_noise(t)
    Resp = noise. respiration_noise(t)
    fs=250

    banda = {
        "delta": w.delta,
        "theta": w.theta,
        "alpha": w.alpha,
        "mu": w.mu,
        "sigma": w.sigma,
        "beta": w.beta,
        "gamma": w.gamma,
        "high_gamma": w.high_gamma
    }

    ondas = {}
    for name, band_func in banda.items():
        freq, amp = band_func()
        ondas[name] = cf.sine_wave(t, freq, amp)

    EEG = sum(ondas.values())
    EEG_real = EEG + wn + pn + nn + EMG + EOG + ECG + Resp

    freqs, mag = fourier(EEG_real, fs)

    return freqs, mag
