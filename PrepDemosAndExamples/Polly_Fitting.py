import numpy as np

def get_poly_weights(order):

    x = np.linspace(-1, 1, order + 1)

    mat = np.zeros([order + 1, order + 1])

    mat[:, 0] = 1

    for i in range(order):
        mat[:, i + 1] = mat[:, i] * x

    #since our matrix is square and invertable , we can use p = a^-1 . d

    mat_inv = np.linalg.inv(mat) #this gets the inverse of our matrix

    #mat_inv is a set of weights for each data point , for each term in the polynomial

    #to find the area under the polynomial curve we use the fact that the area under the nth polynomial from -1 to 1 is 2/n+1 for even n and 0 for odd n


    area_weighted = mat_inv.copy() #creates a copy of our matrix

    for i in range(0, order + 1):

        if i%2 == 0:
            area_weighted[i, : ] *= (2.0/(i+1))

        else:
            area_weighted[i, :] = 0

    #the total area is the sum of the area under each polynomial

    weights = np.sum(area_weighted,axis = 0)

    #since our interval was from -1 to 1, if we want the average value we must devide by 2

    weights = weights / 2



    return weights


if __name__ == "__main__":

    for ord in np.arange(2,3,1):

        weights = get_poly_weights(ord)
        print
        print

        print "Weights for the order " + repr(ord), " are : " + repr (weights)
