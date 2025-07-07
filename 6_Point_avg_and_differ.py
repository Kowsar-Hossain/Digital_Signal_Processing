import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) #noise reproducible every time
n = np.linspace(0,1,200)
x = np.sin(2*np.pi*5*n) + 0.5*np.random.rand(len(n))

#6-point averaging filter
def avg_filter(x):
    y = np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = (x[i] + x[i-1] + x[i-2] + x[i-3] + x[i-4] + x[i-5])/6
    return y

#6-point differencing filter
def differ_filter(x):
    y = np.zeros_like(x)
    for i in range(len(x)):
        y[i] = (x[i] - x[i-1] + x[i-2] - x[i-3] + x[i-4] - x[i-5])/6
    return y    

#Plotting function
def plot_signal(x,y,title,color='b'):
    plt.plot(x,y,color = color)
    plt.title(title)
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

#Apply filter
y_avg = avg_filter(x)
y_diff = differ_filter(x)

#plot result
plt.subplot(3, 1, 1)
plot_signal(n, x, 'Orginal Analog Signal', 'b')

plt.subplot(3, 1, 2)
plot_signal(n, y_avg, '6-point Averaging Filter', 'y')

plt.subplot(3, 1, 3)
plot_signal(n, y_diff, '6-point Differencing Signal', 'r')


plt.legend()
plt.tight_layout()
plt.show()
