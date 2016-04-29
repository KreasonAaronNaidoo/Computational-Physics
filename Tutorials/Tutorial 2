import numpy as np

# Question 1

print
print "Question 1 has no output"
print
print

'''used in old method
x1 = np.arange(0,0.5*(np.pi),(0.5*(np.pi))/10) # x is a range of numbers from 0 to half pi, 10 points
x2 = np.arange(0,0.5*(np.pi),(0.5*(np.pi))/30) # x is a range of numbers from 0 to half pi, 30 points
x3 = np.arange(0,0.5*(np.pi),(0.5*(np.pi))/100) # x is a range of numbers from 0 to half pi, 100 points
x4 = np.arange(0,0.5*(np.pi),(0.5*(np.pi))/300) # x is a range of numbers from 0 to half pi, 300 points
x5 = np.arange(0,0.5*(np.pi),(0.5*(np.pi))/1000) # x is a range of numbers from 0 to half pi, 1000 points
x6 = np.arange(0,0.5*(np.pi),(0.5*(np.pi))/1000000) # x is a range of numbers from 0 to half pi, 1000000 points


# Question 2

def integrate_old (ran):

    width = ran[1] - ran[2]

    sum = 0

    for i in range(len(ran)):
        sum = sum + (np.cos(ran[i])*width)

    return sum

'''

def integrate(low, high, points, function):

    step = (high - low) / points

    x = np.arange(low, high, step)


    sum = 0

    for i in range(len(x)):
        sum = sum + (function(x[i])) * step

    return sum




print "Question 2"
print
print

print "The actual value of the integral of cos(x) between 0 and pi/2 is 1"
print
print

print "The value of the integral of cos(x) between 0 and pi/2 for 10 points is: ", integrate(0, 0.5 * (np.pi), 10, np.cos)
print

print "The value of the integral of cos(x) between 0 and pi/2 for 30 points is: ", integrate(0, 0.5 * (np.pi), 30, np.cos)
print

print "The value of the integrall of cos(x) between 0 and pi/2 for 100 points is: ", integrate(0, 0.5 * (np.pi), 100, np.cos)
print

print "The value of the integrall of cos(x) between 0 and pi/2 for 300 points is: ", integrate(0, 0.5 * (np.pi), 300, np.cos)
print

print "The value of the integrall of cos(x) between 0 and pi/2 for 1000 points is: ", integrate(0, 0.5 * (np.pi), 1000, np.cos)
print

print "The value of the integrall of cos(x) between 0 and pi/2 for 1000000 points is: ", integrate(0, 0.5 * (np.pi), 1000000, np.cos)
print

print

print "As is evident, a higher number of points correlates to a higher accuracy in the calculation "

print
print
print

print "Question 3"

# Question 3
# We wil assume an ordered array starting at 0

# Taking all odd numbers from an array

a = np.arange(101)
print
print
print a[1:-1:2] # -1 denotes the end of the array,
print
print

# Taking all even numbers, skipping the first and last ones
print
print
print a[4:-2:2]
print
print



