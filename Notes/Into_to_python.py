# this is my first project file.

import numpy as np

import Gauss_Example as ga

from  matplotlib import pyplot as plt

print "hello world"

''' python block comment

# integers.

x = 5

print x

print type(x)

print""

#floats.

y = 0.3

print y

print type(y)

print""

#addition of different types.

print x+y

print type(x+y)

print""


#lists (like java arrays, start at 0).

z = [x,y,(x+y)]

print z[1] #prints the secound entry in the list.

# -1 is the index of the final point in the array, -2 is the 2nd last ect
# len(z) returns the length of the array

print len(z)

print z[-1]
print z[-2]


#tuples
#like lists but you cant change them, like FINAL lists / arrays.

# For loops

aa = range(4,21) #will give a list of numbers from 0 to 9

# syntax for x in aa:
    #commands

# new style for loops
for i in aa:
    print i


#for a more traditional for loop (java / c++), I prefer this

for k in range(len(aa)):
    print k , aa[k]

# NB the print command leaves a line (like println in java)
# It's easier to use double quotes for strings (for the cases of words with apostropes)

# x**3 is x to the power 3

# maths in python using imported libraries

import math

for z in range(10):
    print math.sin(z)


# we can also import only the packages of the library that we need

from math import sin

for z in range(10):
    print math.sin(z)

# if we use from math import *, we don't need to have math. in front of sin

#numpy example
import numpy as np

a = np.array([1,2,3])

for d in range(len(a)):
    print a[d]


#matplotlib example
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 30, 256, endpoint=True) #determins the jumps in X, giving us a smooth curve
plt.plot((0, 30), (0, 0), '-k') #this is just a y axis

plt.plot(X, np.sin(X))
plt.plot(X, np.cos(X))

plt.ylabel("Y Values")
plt.xlabel("X Values")

#this will show our numpy graph
plt.show()


# if statments

#for x in range (11):
 #   if (x%2 == 0):
  #      print x

# this would print only the even numbers from 0 to 10


# numpy arrays

import numpy as np

x = np.arange(10) #an array with numbers 0 to 9


# Functions in python (methods)
# Gaussian std gen form  ae^(-(x-x0)^2/2sigma^2)


X = np.arange(-5,5,0.0001)
plt.plot(X, ga.gauss(X, -1, 1, 1))
plt.plot(X, ga.gauss(X,amp = 1, x0 = 1,sigma = 1))
plt.plot(X, ga.gauss(X))

plt.show()

'''

#Dictionaries : use a key and a value

wavelengths = {}

wavelengths["blue"] = 400

wavelengths["red"] = 700

wavelengths["yellow"] = 600

wavelengths["green"] = 500


print wavelengths["blue"]


#dictionaries can contain strings and numbers

print wavelengths.keys()


print
print


cubes = {}

for i in range(11):
    cubes[i] = i**3
    print i, " :  " ,cubes[i]