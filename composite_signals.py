# Problem statement: 
# Consider the analog signal: xa(t)=3cos(200πt)+5sin(600πt)+10cos(1200πt). 
# Show the effect of sampling rate.  

import numpy as np
import matplotlib.pyplot as plt

n = n1 = np.arange(0, 0.01, 800)

#input signal
input_signal = 3*np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,1)
plt.plot(n1, input_signal, label='Input Signal')
plt.grid(True)

#sampled at 800Hz
n = np.arange(0, 0.01, 1/800)
low_sampled = 3*np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,2)
plt.plot(n1, input_signal, label='Input Signal')
plt.stem(n, low_sampled, 'y', label='Sampled 800hz')
plt.grid(True)

#sampled at 1200Hz
n = np.arange(0, 0.01, 1/1200)
correct_sampled = 3*np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,3)
plt.plot(n1, input_signal, label='Input Signal')
plt.stem(n, correct_sampled, 'b', label='Sampled 1200hz')
plt.grid(True)

#sampled at 2000Hz
n = np.arange(0, 0.01, 1/2000)
higher_sampled = 3*np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,4)
plt.plot(n1, input_signal, label='Input Signal')
plt.stem(n, higher_sampled, 'b', label='Sampled 2000hz')
plt.grid(True)

plt.tight_layout()
plt.legend()
plt.show()

