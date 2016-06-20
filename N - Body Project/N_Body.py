
import particle
import numpy as np
import random as rand


class N_Body:


    def __init__(self):


        self.Number_of_particles = 100000  #Number of particles

        self.G = 6.67300 * 10 ** -11

        self.Grid_Size = 101 #The grid is this number on each side

        self.dt = 0.005

        #Create the grid with equal spacing

        self.real_space_matrix = [] # this is where the particles will live

        self.density_matrix = np.zeros(shape=(self.Grid_Size, self.Grid_Size))  # this stores the density matrix

        self.potential_matrix = np.zeros((self.Grid_Size, self.Grid_Size)) # this stores the potential matrix

        self.softening_potential = (-1*self.G)/ 2**(0.5)
        #The cut of radius before we use the softening potential is sqrt(2)


    def populate_real_space_matrix(self):

        for x in range(0, self.Number_of_particles):
            temp_x = rand.uniform(0, 100)
            temp_y = rand.uniform(0, 100)

            temp_particle = particle.particle(1, temp_x, temp_y) # we are using the uniform mass of 1



            self.real_space_matrix.append(temp_particle)
            #adds the particle to the list of particles at that point in the real space matrix

    def print_test(self):

        print self.potential_matrix


    def generate_density_matrix(self):

         for i in range(len(self.real_space_matrix)):

            round_x = int(round(self.real_space_matrix[i].position_x))
            round_y = int(round(self.real_space_matrix[i].position_y))

            self.density_matrix[round_x][round_y] = self.density_matrix[round_x][round_y] + 1
            #This creates the density matrix




    def generate_potential_matrix(self):

        fft1 = np.fft.fft(self.density_matrix)

        self.potential_matrix = np.real(np.fft.ifft(fft1 * self.softening_potential))
        # we use the fact that the fft of a constant is the same value


    def update_particle_positions(self):
        #call solve force, velocity and position per particle



        return 0


















