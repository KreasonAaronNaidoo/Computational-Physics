import numpy as np
from matplotlib import pyplot as plt

import Gauss_Example as ga


#Tutorial 3

#Question 1

print "Question 1"
print
print

def conv (array, shift):


    if1 = np.fft.fft(ga.gauss(array,x0 = len(array)/2 + shift))

    if2 = np.fft.fft(array)

    mul = if1*if2

    plt.plot(x,mul)
    plt.show()

    return np.fft.ifft(mul)


x = np.arange(-100,100, 1)
conv(x, 0)

#Question 2

def cor (array1, array2):

    ift

    return 0
