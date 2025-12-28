import matplotlib.pyplot as plt
from brain import generate_EEG

freqs , mag = generate_EEG()

plt.plot(freqs, mag)
plt.title("FFT do EEG (4–40 Hz)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
