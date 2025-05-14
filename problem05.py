import numpy as np
import matplotlib.pylab as plt

def analog_functon(t):
    return 3*np.cos(200*np.pi*t) + 5*np.sin(600*np.pi*t) + 10*np.cos(1200*np.pi*t)

t_cont = np.linspace(0, 0.01, 1000)
x_cont = analog_functon(t_cont)

sampling_rate = [2500,800,1000]
colors = ['b', 'r', 'g']

plt.figure(figsize=(10,6))

plt.plot(t_cont, x_cont, 'k', label="Orginal Analog signal", alpha = 0.7)

for i, fs in enumerate(sampling_rate):
    t_sampled = np.arange(0, 0.01, 1/fs)
    x_sampled = analog_functon(t_sampled)

    plt.stem(t_sampled, x_sampled, linefmt=colors[i]+'-', markerfmt=colors[i]+'o', label=f"Sampled at {fs} Hz")

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Analog and Discrete signal Representation")
plt.grid()
plt.legend()
plt.show()
