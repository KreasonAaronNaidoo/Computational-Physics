import numpy as np
from matplotlib import pyplot as plt

import Gauss_Example as ga


#Tutorial 3

#Question 1

#the number of passes for an fft is the log base 2 of the number of data elements

print "Question 1"
print
print

def conv (array, shift):


    if1 = np.fft.fft(ga.gauss(array,x0 = len(array)/2 + shift))

    if2 = np.fft.fft(array)

    mul = if1*if2



    return np.real(np.fft.ifft(mul))


x = np.arange(-100,100, 1)

plt.plot(x,conv(x, 0))
plt.show()

#Question 2

def cor (array1, array2):

    if1 = np.fft.fft(array1)
    if2 = np.fft.fft(array2)

    return np.fft.ifft(if1*np.conjugate(if2))

x1 = ga.gauss(np.arange(-100,100, 1))

plt.plot(cor(x1, x1))
plt.show()


#Question 3

func = cor(conv (x1, 2),conv (x1, 2)) #here the arb shift is 2

plt.plot(func)
plt.show()




