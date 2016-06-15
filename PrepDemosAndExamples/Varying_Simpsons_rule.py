import numpy as np


def varSimp(arbx, func):

    #First step: silce arbx into left and right

    x_left = arbx[ :-1] #everything up to the secound last value
    x_right = arbx[1 : ] #everything from the secound value to the last value

    #Second step: compute the mid values

    x_mid = (x_left + x_right)*0.5

    #compute dx

    dx = x_right - x_left

    #compute the y values

    y_left = func(x_left)
    y_right = func(x_right)
    y_mid = func(x_mid)

    #now we sum according to simpsons rule

    integral = np.sum(dx*(y_left + 4*y_mid + y_right)/6.0)


    return integral

def myFunction(x):

    y = 1.0 / (1 + x**2)

    return y



# Set up the namespace

if __name__ == '__main__':

    #lets set up some set of points, these include the bin spacing

    x1 = np.linspace(-10,-2,9) # these go from -10 to -2 with a spacing of 1
    x2 = np.linspace(-1, 1, 21) # these go from -1 to 1 with a spacing of 0.1
    x3 = np.linspace(2,10,9) # these go from 2 to 10 with a spacing of 1

    # here we combine our three arrays into one
    x = np.append(x1, x2)
    x = np.append(x, x3)

    #now we evaluate our function

    answer = varSimp(x, myFunction)
    calcAnswer = np.arctan(10) - np.arctan(-10)

    print
    print
    print "Varying Simpson's rule answer: ", answer
    print
    print "Calculas answer: ", calcAnswer
    print
    print "Difference in answers: ", answer - calcAnswer









