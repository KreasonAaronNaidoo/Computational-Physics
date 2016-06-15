import numpy as np
from matplotlib import pyplot as plt

class conv:

    def convolve (self, f, g):

        ans = np.fft.ifft(np.fft.fft(f)*np.fft.fft(g))

        return np.real(ans)


x = np.arange(-10, 20, 0.1)

f = np.exp(-0.5*(x+3)**2/ 0.5**2)
f = f/f.sum()
g = 0*x; g[(x > 0) & (x < 5)] =1
g = g/g.sum()

con = conv()

h = con.convolve(f,g)

plt.plot(x,f,"r")
plt.plot(x,g,"b")
plt.plot(x,h,"k")

plt.show()