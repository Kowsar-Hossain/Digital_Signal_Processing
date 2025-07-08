import numpy as np
import matplotlib.pyplot as plt

N = 64
n = np.arange(N)
fs = 8000
t = n/fs

def xa(t):
    return np.sin(2000*np.pi*t)+0.5*np.sin(4000*np.pi*t+4*np.pi)
def hanning(N):
     return 0.5*(1-np.cos(2*np.pi*np.arange(N)/N-1))

def dft(x):
    N = len(x)
    X = np.zeros(N,dtype=complex)
    for k in range(N):
         for n in range(N):
              X[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
    return X 

def idft(X):
    N = len(X)
    x = np.zeros(N,dtype=complex)
    for n in range (N):
          for k in range(N):
               x[n]+=X[k]*np.exp(2j*np.pi*k*n/N)
          x[n] /= N
    return x

freq = np.arange(N)*fs/N
x = xa(t)

x_hanning = hanning(N)
hanning_x = x*x_hanning

x_dft = dft(x)
x_hanning_dft = dft(hanning_x)

x_idft = idft(x_dft)
x_idft_hanning = idft(x_hanning_dft)

plt.subplot(3,2,1)
plt.plot(t,x,label="original",color="g")
plt.plot(t,hanning_x,label="Hanning",color="r")
# plt.title("Before DFT")
plt.grid(True)
plt.legend()

plt.subplot(3,2,2)
plt.stem(freq,x_hanning,label="Hanning Window")
# plt.title("Hanning Window")
plt.grid(True)
plt.legend()

plt.subplot(3,2,3)
plt.stem(freq,abs(x_dft),label="Frequency Spectrum")
# plt.title("After DFT")
plt.grid(True)
plt.legend()

plt.subplot(3,2,4)
plt.stem(freq,np.angle(x_hanning_dft,deg=True),label="Hanning Phase Spectrum",linefmt="r",basefmt="r",markerfmt="r")
# plt.title("After DFT")
plt.grid(True)
plt.legend()

plt.subplot(3,2,5)
plt.plot(t,x_idft,label="After IDFT",color="g")
plt.plot(t,x_idft_hanning,label="Hanning",color="r")
# plt.title("Before DFT")
plt.grid(True)
plt.legend()

plt.show()
plt.tight_layout()
