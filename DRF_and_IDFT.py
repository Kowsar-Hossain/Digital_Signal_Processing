import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft  # safer import than numpy.fft

# 1. Sampling settings
fs = 8000                      # Sampling frequency
t = np.arange(0, 1, 1/fs)      # Time vector (1 second duration)

# 2. Signal: sum of two sinusoids
x = np.sin(2*np.pi*1000*t) + 0.5*np.sin(2*np.pi*2000*t + 4*np.pi)

# 3. Perform FFT (Discrete Fourier Transform)
X = fft(x)

# 4. Reconstruct using IFFT
x_rec = ifft(X)

# 5. Plotting
plt.figure(figsize=(10, 4))

# Plot magnitude spectrum (only positive frequencies)
plt.subplot(1, 2, 1)
plt.plot(np.linspace(0, fs/2, fs//2), np.abs(X[:fs//2]))
plt.title('DFT Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|X(f)|')

# Plot reconstructed signal (real part only)
plt.subplot(1, 2, 2)
plt.plot(t, x_rec.real)
plt.title('Reconstructed Signal via IFFT')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
