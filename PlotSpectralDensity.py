import numpy as np
from rtlsdr import RtlSdr
import matplotlib.pyplot as plt

# Configure the RTL-SDR dongle
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 97.1e6
sdr.gain = 'auto'

# Capture signal samples
num_samples = 1024 * 1024
samples = sdr.read_samples(num_samples)

# Clse the RTL-SDR dongle
sdr.close()

# Perform FFT
spectrum = np.fft.fft(samples)
frequencies = np.fft.fftfreq(len(spectrum), 1/sdr.sample_rate)

# Plot the spectrum
plt.figure()
plt.plot(frequencies, 10 * np.log10(np.abs(spectrum)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (dB)')
plt.grid()
plt.show()
