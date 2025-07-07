import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin  # 💡 Import added

# Sampling setup
fs = 500  # Sampling frequency
n = np.arange(0, 1, 1/fs)  # Time vector: 1 second duration

# Noisy signal: 10 Hz desired + 100 Hz noise
clean_signal = np.sin(2 * np.pi * 10 * n)
noise = 0.5 * np.sin(2 * np.pi * 100 * n)
signal = clean_signal + noise

# Design Low-Pass Filter
cutoff = 0.1  # Normalized cutoff = (desired cutoff frequency) / (Nyquist = fs/2)
h = firwin(31, cutoff)  # FIR filter with 31 taps

# Apply the filter
filtered_signal = np.convolve(signal, h, mode='same')

# Plot results
plt.figure(figsize=(10, 4))
plt.plot(n, signal, 'gray', label='Noisy Signal')
plt.plot(n, filtered_signal, 'red', label='Filtered Signal')
plt.plot(n, clean_signal, 'blue', label='Clean_signal')
plt.legend()
plt.title('Low-pass FIR Filter Output')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()
