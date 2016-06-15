import numpy as np

#make an 2D array of ones

x = np.ones([5,5])

print x

#We cannot do matrix operations like multiplication directly on x

print x*x #this multiplies each array item but does not multiply the array like a martrix

# we can use .dot to treat the array like a martic for multiplication

print np.dot(x,x) #this gives us matrix multiplication

#better still we can convert the 2D array into a matrix

y = np.matrix(x) #this recasts our 2D array into a matrix

print y*y #now this will give us martix multiplication

#if we wanted to do standard element multiplication we could use nested for loops or use

print np.multiply(y,y) #this treates the matrix as an array


#we can reverse this process with
z = np.array(y)

