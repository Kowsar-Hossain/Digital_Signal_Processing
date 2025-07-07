import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)

# unit step signal
unit_step = np.where(n >= 0, 1, 0)

# ramp signal
ramp = np.where(n >= 0, n, 0)

# exponential signal
alpha = -0.9
exponential = alpha ** n

# sine wave signal
pi = np.pi
A = 1
f = .1
fi = 0
sine_signal = A * np.sin(2 * pi * f * n + fi)

# cos wave signal
cosine_signal = A * np.cos(2 * pi * f * n + fi)

# Plot signals

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.stem(n, unit_step)
plt.title('Unit Step Signal')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(n, ramp)
plt.title('Ramp Signal')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.stem(n, exponential)
plt.title('Exponential Signal')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(n, sine_signal)
plt.title('Sine Wave Signal')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.stem(n, cosine_signal)
plt.title('Cosine Wave Signal') 
plt.grid(True)

plt.tight_layout()
plt.show()
