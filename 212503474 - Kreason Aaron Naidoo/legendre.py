import numpy as np

def gen_polynomials(n, x):




    if n == 0:
      return 1
    if n == 1:
       return x

    p = (((2*(n-1) + 1)*x*gen_polynomials(n-1, x)) / n ) - (((n-1)*gen_polynomials(n-2, x)) / n )
    #This will recursivly find the polynomials we want




    return p



if __name__== "__main__":

    x = np.linspace(-1, 1, 1000)
    N = 10 #order

    mat = np.zeros([x.size, N + 1])

    mat[:, 0] = 1

    for i in range(0, N):
        mat[:, i+1] = mat[:, i] * gen_polynomials(i, x)



    y = np.exp(x)

    lhs = np.dot(mat.transpose(), mat)
    rhs = np.dot(mat.transpose(), y)

    mat_inv = np.linalg.inv(lhs)

    fit = np.dot(mat_inv, rhs)

    pre = np.dot(mat, fit)

    print "Average absolute error for the fit is: ", np.mean(np.abs(pre - y)),

