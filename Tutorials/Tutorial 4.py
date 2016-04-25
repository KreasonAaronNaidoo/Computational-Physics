import numpy as np

class complex:

    def __init__(self, r, i): #we "declare" our varibles for the class in the constructior, and pass values to them if we like.

        self.real = r
        self.img = i



    def abs(self):

        return np.sqrt(self.real**2 +self.img**2)


    def copy(self):

        return complex(self.real, self.img) #we return a new object with the same values

    def __add__(self, val): #python will search to find the plus symbol and pair it to the __add__ function

        ans = self.copy()

        ans.real += val.real
        ans.img += val.img


        return ans




    def __sub__(self, val):

        ans = self.copy()

        ans.real -= val.real
        ans.img -= val.img

        return ans


    def __mul__(self, val):

        ans = self.copy()
        sr = 0
        si = 0


        sr += ans.real*val.real
        si += ans.real*val.img
        si += val.real*ans.img
        sr += ans.img*val.img

        ans.real = sr
        ans.img = si

        return ans

    def __div__(self, val): #ans/val
        ans = self.copy()

        conjval = complex(val.real, val.img*-1)

        num = ans.__mul__(conjval)
        den = val.__mul__(conjval) # we know this will be real

        ans.real = num.real / den.real
        ans.img = num.img / den.img

        return ans



a = complex (3,4)
b = complex(5,8)

print "a = ",a.real,"+i",a.img
print "b = ",b.real,"+i",b.img


print
print
print "b + a : ", (b + a).real, "+i",(b + a).img
print
print "b - a : ", (b - a).real, "+i",(b - a).img
print
print "a * b : ", (b * a).real, "+i",(b * a).img
print
print "b / a : ", (b / a).real, "+i",(b / a).img
