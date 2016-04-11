import numpy as np

def gauss(x, x0 = 0, amp = 1, sigma = 1):

    print __name__
    return  (  amp*(np.exp( ( -(x-x0)**2)  /( (2*(sigma**2) ) ) ) ) )