import numpy as np
import matplotlib.pyplot as plt
def convolve(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1
    y = [0] * len_y

    for i in range(len_y):
        for k in range(len_x):
            if(i - k >= 0 and i - k < len_h):
                y[i] += x[k] * h[i - k]
    
    return y
x = [1, 2, 3, 1]
h = [1, 2, 1, -1]

plt.figure(figsize=(7, 5))

plt.subplot(2, 2, 1)
plt.stem(x)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('x(n)')

plt.subplot(2, 2, 2)
plt.stem(h)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('h(n)')

# Convolution
y = convolve(x, h)

plt.subplot(2, 2, 3)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('y(n) = x(n) * h(n)')

# Crosscorrelation
y = convolve(x, h[::-1])

plt.subplot(2, 2, 4)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('y(n) = x(n) . h(n)')

plt.tight_layout()
plt.show()
