
import PointMass as PM
import numpy as np
import scipy as sci

class N_Body:


    def __init__(self):

        self.options = {} #dictionary of constants

        self.options["N"] = 0
        self.options["G"] = 6.67300 * 10 ** -11

        self.part = [] #list of all particals


    def add(self, m, x, y):

        self.part.append(PM.PointMass(m, x, y)) #could be written to accept point mass objects instead of raw data on the points
        self.options["N"] = self.options["N"] + 1




    def pot_energy(self, a, b): # potential energy between interacting particles

        Rba = ( ((b.x - a.x)**2) + ((b.y - a.y)**2) )**0.5 #distance formula

        if Rba == 0:

            return 0;

        else:

            return (self.options["G"] * a.m * b.m) / Rba



    def tot_pot_energy(self):

        sum = 0

        #these for loops do a "round robin" calculation of potential energy
        #They also assume the particles are in a vacume and are the only masses around
        # i.e no gravitational effect due to the earth


        for i in range(len(self.part)):
            for j in range(len(self.part)):

                if (i != j): #if i==j, they are the same particle and therefore cannot have a potential energy due to itself

                    sum = sum + self.pot_energy(self.part[i],self.part[j])

                    sum = sum/2


        return sum


    def forcex(self, a, b):

        R2 = (((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))

        f = self.options["G"] * a.m * b.m / R2

        dirx = (b.x - a.x) / (R2**0.5)

        return f*dirx #the x component of the force


    def forcey(self, a, b):

        R2 = (((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))

        f = self.options["G"] * a.m * b.m / R2

        diry = (b.y - a.y) / (R2 ** 0.5)

        return f * diry  # the y component of the force



    def setTotalForce(self):

        for i in range(len(self.part)):

            self.part[i].fx = 0
            self.part[i].fy = 0

            for j in range(len(self.part)):

                if (i != j):

                    self.part[i].fx = self.part[i].fx + self.forcex(self.part[i], self.part[j])
                    self.part[i].fy = self.part[i].fy + self.forcey(self.part[i], self.part[j])

        return



    def setA(self):


        for i in range(len(self.part)):

            self.part[i].ax = 0
            self.part[i].ay = 0

            self.part[i].ax = self.part[i].ax + (self.part[i].fx / self.part[i].m)
            self.part[i].ay = self.part[i].ay + (self.part[i].fy / self.part[i].m)

        return

    def setV(self): # needs to be written

        for i in range(len(self.part)):

            self.part[i].vx = 0
            self.part[i].vy = 0


        return


    def setx(self):

        for i in range(len(self.part)):

            self.part[i].vx = 0
            self.part[i].vy = 0

            #assuming the time nterval per call of setx is one second

            self.part[i].x = self.part[i].x + self.part[i].vx
            self.part[i].y = self.part[i].y + self.part[i].vy
        return





