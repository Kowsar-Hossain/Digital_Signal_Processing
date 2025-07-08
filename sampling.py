import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 0.04, 1000)

y = 3 * np.cos(100*np.pi*n)
plt.plot(n, y, label='input signal')

#Sampling at 75Hz
n = np.arange(0, 0.04, 1/75)
y = 3*np.cos(100*np.pi*n)
plt.stem(n, y, 'g', label='Sample 75')

#Sampling at 200Hz
n = np.arange(0, 0.04, 1/200)
y = 3*np.cos(100*np.pi*n)
plt.stem(n, y, 'b', label='Sample 200')

plt.xlabel('time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
