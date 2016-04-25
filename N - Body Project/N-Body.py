import numpy as np
from  matplotlib import pyplot as plt
import PointMass as PM

class NBody:


    def __init__(self, N = 0):

        self.N = N
        self.options = {} #dictionary of constants

        self.options["N"] = self.N
        self.options["G"] = 6.67300 * 10 ** -11

        self.part = [] #list of all particals


    def add(self, m, x, y):

        self.part.append(PM(m, x, y)) #could be written to accept point mass objects instead of raw data on the points
        self.options["N"] = self.options["N"] + 1




    def pot_energy(self, a, b): # potential energy between interacting particles

        Rba = ( ((b.x - a.x)**2) + ((b.y - a.y)**2) )**0.5 #distance formula

        return (self.options["G"] * a.m * b.m) / Rba



    def tot_pot_energy(self):

        sum = 0

        #these for loops do a "round robin" calculation of potential energy
        #They also assume the particles are in a vacume and are the only masses around
        # i.e no gravitational effect due to the earth


        for i in range(len(self.part)):
            for j in range(len(self.part)):

                if (i != j): #if i==j, they are the same particle and therefore cannot have a potential energy due to itself

                    sum = sum + self.pot_energy(i, j)


        return sum
















