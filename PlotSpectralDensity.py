import numpy as np
from rtlsdr import RtlSdr
import matplotlib.pyplot as plt

sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 97.1e6
sdr.gain = 'auto'

num_samples = 1024 * 1024
samples = sdr.read_samples(num_samples)

sdr.close()

spectrum = np.fft.fft(samples)
frequencies = np.fft.fftfreq(len(spectrum), 1/sdr.sample_rate)

plt.figure()
plt.plot(frequencies, 10 * np.log10(np.abs(spectrum)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (dB)')
plt.grid()
plt.show()
