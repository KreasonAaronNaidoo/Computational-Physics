import numpy as np

def singleDFT(y, k, x):

    i = np.complex(0,1)
    N = y.size
    j = np.linspace(0,100, N)


    mydft = np.sum(y*np.exp(((2*np.pi*i)/N)*j*x))

    print mydft

    pred = np.fft.fft(y)

    print y[k]


if __name__ == "__main__":


    x = np.arange(0, 100, 0.1)

    y = np.exp(-x**2/2)

    singleDFT(y,4,x)
