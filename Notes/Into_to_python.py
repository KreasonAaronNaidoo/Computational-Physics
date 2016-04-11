# this is my first project file.

print "hello world"

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
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot((0, 2*np.pi), (0, 0), '-k')
plt.plot(X, C)
plt.plot(X, S)

# this will show our numpy graph
#plt.show()


# if statments

for x in range (11):
    if (x%2 == 0):
        print x

# this would print only the even numbers from 0 to 10


# numpy arrays




