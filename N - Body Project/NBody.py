
import PointMass as PM


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

        Rba =  (((b.x - a.x)**2) + ((b.y - a.y)**2))**0.5 #distance formula

        if Rba == 0:

            return 0

        else:

            return (self.options["G"] * a.m * b.m) / Rba



    def tot_pot_energy(self):

        sum2 = 0

        for m in range(0,self.options["N"]):
            for n in range(m+1, self.options["N"]):

                    sum2 = sum2 + self.pot_energy(self.part[m], self.part[n])

        return sum2


