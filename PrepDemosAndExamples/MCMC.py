import numpy as np

from matplotlib import pyplot as plt

samps = np.loadtxt("example_chain.txt")

myfft = np.abs(np.fft.fft(samps[:, 0]))

plt.clf()

freq = np.arange(1, myfft.size)
#we dont take the zeroth frequency as its the mean of the params

plt.plot(freq, myfft[1:], ".")

ax = plt.gca()

ax.set_yscale("log")
ax.set_xscale("log")

plt._show()

