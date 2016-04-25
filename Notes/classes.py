#class blueprint
import numpy as np

class complex: #only things indented into the classes block is part of the class

    def __init__(self, r, i): #we "declare" our varibles for the class in the constructior, and pass values to them if we like.

        self.real = r
        self.img = i



# to create an instance of the class

#import the class : import classes


#                              filename.classname(args)
#create instance : mynumber  = classes.complex(args)


    def abs(self):

        return np.sqrt(self.real**2 +self.img**2)


    def copy(self):

        return complex(self.real, self.img) #we return a new object with the same values

    def __add__(self, a): #python will search to find the plus symbol and pair ot to the __add__ function

        newA = a.copy() #a is an object

        newA.real += self.real
        newA.img += self.img
        return newA


mynum = complex(1,2)
nu = complex(23,7)

print (mynum+nu).real, "+i", (mynum+nu).img

print (mynum+nu).abs()

#overloading (overiding the standard function of a class with our own class definition



#try and except


try:

    #blah code

except:

    #when blah fails and cannot run

