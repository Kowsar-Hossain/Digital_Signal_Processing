import numpy as np
import matplotlib.pyplot as plt

fs = 500
t = np.arange(0,1,1/fs)
x =  np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*50*t)

def convolution(x,h):
    len_x = len(x)
    len_h= len(h)
    len_y = len_x+len_h-1
    y = []
    for n in range(len_y):
         sum=0
         for k in range(len_h):
              if 0<=n-k<len_x:
                   sum+=h[k]*x[n-k]
         y.append(sum)
    return y
def hanning(N):
     n = np.arange(N)
     return 0.5-.05*np.cos(2*np.pi*n/N-1)

def lowpassfilter(N,fc,fs):
     n = np.arange(N)
     h = np.sinc(2*fc*(n-((N-1)/2))/fs)*hanning(N)
     h/=np.sum(h)
     return h
h = lowpassfilter(N=31,fc=10,fs=fs)
y = convolution(x,h)
t1 = np.arange(len(y))/fs

plt.plot(t,x,label="Noisy Signal",color='r')
plt.plot(t1,y,label="Filtered signal",color="g")
plt.title("FIR Filter")
plt.grid(True)
plt.legend()
plt.show()
