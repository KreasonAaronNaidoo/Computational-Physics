import numpy as np

def myFFT(vec):

    n = vec.size

    #if n == 1, then the ftt is the value of the vec

    if n ==1 :
        return vec

    #we want to split the vec into even and odd parts

    myEvenVec = vec[0::2]
    myOddVec = vec[1::2]

    #the new length of the even / off vecs is nn = n/2 (half the original)
    nn = n/2

    #we need to define unity in complec numbers (i)

    i = np.complex(0,1)

    #we need to generate the phase factor that results from the seperation of the vec

    fph = np.exp(-2*np.pi*i*np.arange(0,nn)/n)

    #now we get the FT of the odd and even parts
    #this is done recursivly

    dftOdd = myFFT(myOddVec)
    dftEven = myFFT(myEvenVec)

    #now that we have the partial pieces of the dft of the vec ans the phase factor, we stitch it all together

    myAns = np.concatenate((dftEven + fph*dftOdd, dftEven - fph*dftOdd))

    return myAns



x = np.random.randn(32)

myAnswer = myFFT(x)

betterAnswer = np.fft.fft(x)

print "My accuracy is " , np.sum(np.abs(myAnswer-betterAnswer))

