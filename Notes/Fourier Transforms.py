# Definition of a FT as a computer carries it out

# Given f(x)

#f(k) = sum: f(x)sub j exp(ik2pij / N) from 0 to N

# Discrete FT (DFT)

# go read the FT slides


import numpy as np

I = np.complex(0,1) #declarring out complex i

f = np.random.randn(10) # generates a set of ten random numbers
k1 = np.sum(f*np.exp(1 * 2 * np.pi * I /10))

np.fft.fft(f)[0] #short hand
np.fft.fft(f)[1]



# the flip of a forrier transform is the complex conjugate of the original
# np.conj(FT)
# reverse FT is no.fft.ifft(FT)



#shifting



#convolution expmple

