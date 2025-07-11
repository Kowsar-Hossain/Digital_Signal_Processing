import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin

fs = 500
n = np.arange(0,1,1/fs)

clean_signal = np.sin(2*np.pi*10*n)
noise_signal = np.sin(2*np.pi*100*n)
x = clean_signal + noise_signal

cutoff = 0.1
h = firwin(31, cutoff)

def convolution(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len(x) + len(h) - 1
    y = []
    for i in range(len_y):
        sum = 0
        for k in range(len_h):
            if i-k >= 0 and i-k < len_x:
                sum += h[k] * x[i-k]
        y.append(sum)
    return y     

filtered_signal = convolution(x,h)

start = (len(h) - 1) // 2
filtered_signal = filtered_signal[start:start + len(x)]

#plot
plt.figure(figsize=(10,4))
plt.plot(n, x, 'r', label='Noise Signal')
plt.plot(n, clean_signal, 'white', label='Clean Signal')
plt.plot(n, filtered_signal,'b', label='Filtered Signal')
plt.legend()
plt.title('Low pass filter Output')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()
