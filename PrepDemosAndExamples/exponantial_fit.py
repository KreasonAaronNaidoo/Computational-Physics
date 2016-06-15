import numpy as np

def exp_fit(x, order):

    # make a matrix filled with x^-n

    mat = np.zeros([x.size, order + 1])

    mat[:, 0] = 1
    for i in range(0, order):
        mat[:, i + 1] = mat[:, i] / x

    # make the y points because we don't have them passed in

    y = np.exp(x)

    # do the usual least-squared fits

    lhs = np.dot(mat.transpose(), mat)
    rhs = np.dot(mat.transpose(), y)

    mat_inv = np.linalg.inv(lhs)

    fitp = np.dot(mat_inv, rhs)

    pred = np.dot(mat, fitp)

    return fitp, pred


if __name__ == "__main__":

    x = np.linspace(1,5,1000)

    y = np.exp(x)

    fitp, pred = exp_fit(x, 5)

    print "Mean error for first fit is: ", np.mean(np.abs(pred - y)), " with mean value : ", np.mean(y)

