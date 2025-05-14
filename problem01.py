import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)

plt.figure(figsize=(12,10))

unit_step = np.where(n >= 0 , 1 , 0)
ramp = np.where(n >= 0, n, 0)                  # r[n] = n*u[n]
exponential = np.where(n >= 0, 0.8**n, 0)      # a^n*u[n], here a=0.8
sine = np.sin(0.2 * np.pi * n)                 # sin(0.2πn)
cosine = np.cos(0.2 * np.pi * n)

plt.subplot(3, 2, 1)
plt.stem(n,unit_step)
plt.title("Unit Step Sequence")
plt.grid(True)
plt.show()

plt.subplot(3, 2, 1)
plt.stem(n,ramp)
plt.title("Unit Step Sequence")
plt.grid(True)
plt.show()