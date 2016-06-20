
import particle
import numpy as np
import random as rand
from matplotlib import pyplot as plt



class N_Body:


    def __init__(self):


        self.Number_of_particles = 100000  #Number of particles

        self.G = 6.67300 * 10 ** -11

        self.Grid_Size = 101 #The grid is this number on each side

        self.dt = 0.005

        #Create the grid with equal spacing

        self.real_space_list = [] # this is where the particles will live

        self.density_matrix = np.zeros(shape=(self.Grid_Size, self.Grid_Size))  # this stores the density matrix

        self.potential_matrix = np.zeros((self.Grid_Size, self.Grid_Size)) # this stores the potential matrix

        self.softening_potential = (-1*self.G)/ 2**(0.5)
        #The cut of radius before we use the softening potential is sqrt(2)

        self.periodic = False
        #Change this value to change to the system to periodic




    def populate_real_space_matrix(self):

        for x in range(0, self.Number_of_particles):
            temp_x = rand.uniform(0, 100)
            temp_y = rand.uniform(0, 100)

            temp_particle = particle.particle(1, temp_x, temp_y) # we are using the uniform mass of 1

            self.real_space_list.append(temp_particle)
            #adds the particle to the list of particles at that point in the real space matrix

    def print_test(self):

        print self.potential_matrix


    def generate_density_matrix(self):

         for i in range(len(self.real_space_list)):

            round_x = int(round(self.real_space_list[i].position_x))
            round_y = int(round(self.real_space_list[i].position_y))


            self.real_space_list[i].round_x = round_x
            self.real_space_list[i].round_y = round_y


            self.density_matrix[round_x][round_y] = self.density_matrix[round_x][round_y] + 1
            #This creates the density matrix




    def generate_potential_matrix(self):

        fft1 = np.fft.fft(self.density_matrix)

        self.potential_matrix = np.real(np.fft.ifft(fft1 * self.softening_potential))
        # we use the fact that the fft of a constant is the same value



    def update_particle_positions(self):

        for i in range(0, len(self.real_space_list)):

            # This sets up the force

            current_x = self.real_space_list[i].round_x
            current_y = self.real_space_list[i].round_y

            if(self.periodic == False):


                if(current_x == 0):
                  ux_left = 0
                else:
                   ux_left = self.potential_matrix[current_x - 1][current_y]


                if(current_x == self.Grid_Size -1):
                    ux_right = 0
                else:
                    ux_right = self.potential_matrix[current_x + 1][current_y]



                if (current_y == 0):
                    uy_up = 0
                else:
                    uy_up = self.potential_matrix[current_x][current_y - 1]


                if (current_y == self.Grid_Size - 1):
                    uy_down = 0
                else:
                    uy_down = self.potential_matrix[current_x][current_y + 1]



        if (self.periodic == True):


            if (current_x == 0):
                ux_left = self.potential_matrix[self.Grid_Size][current_y]
            else:
                ux_left = self.potential_matrix[current_x - 1][current_y]


            if (current_x == self.Grid_Size - 1):
                ux_right = self.potential_matrix[0][current_y]
            else:
                ux_right = self.potential_matrix[current_x + 1][current_y]



            if (current_y == 0):
                uy_up = self.potential_matrix[current_x][self.Grid_Size]
            else:
                uy_up = self.potential_matrix[current_x][current_y - 1]


            if (current_y == self.Grid_Size - 1):
                uy_down = self.potential_matrix[current_x][0]
            else:
                uy_down = self.potential_matrix[current_x][current_y + 1]




        self.real_space_list[i].solve_force(ux_left, ux_right, uy_up, uy_down)

        # This sets up the velocity

        self.real_space_list[i].solve_velocity(self.dt)

        # This sets up the position


        if (self.periodic == True):

            if(self.real_space_list[i].position_x < 0 ):
                self.real_space_list[i].position_x = self.Grid_Size - 0.1

            if (self.real_space_list[i].position_x > self.Grid_Size):
                self.real_space_list[i].position_x = 0.1

            if (self.real_space_list[i].position_y < 0):
                self.real_space_list[i].position_y = self.Grid_Size - 0.1

            if (self.real_space_list[i].position_y > self.Grid_Size):
                self.real_space_list[i].position_y = 0.1


        if (self.periodic == False):

            if (self.real_space_list[i].position_x < 0):
                del self.real_space_list[i]

            if (self.real_space_list[i].position_x > self.Grid_Size):
                del self.real_space_list[i]

            if (self.real_space_list[i].position_y < 0):
                del self.real_space_list[i]

            if (self.real_space_list[i].position_y > self.Grid_Size):
                del self.real_space_list[i]


        self.real_space_list[i].solve_position(self.dt)




