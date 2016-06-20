
import particle as PM
import numpy as np


class N_Body:


    def __init__(self):


        Number_of_particles = 100000  #Number of particles

        G = 6.67300 * 10 ** -11

        Grid_Size = 100 #The grid is this number on each side

        dt = 0.005

        #Create the grid with equal spacing

        real_space_matrix = [[[Grid_Size]]] # this is where the particles will live

        density_matrix = np.zeros((Grid_Size, Grid_Size)) # this stores the density matrix

        potential_matrix = np.zeros((Grid_Size, Grid_Size)) # this stores the potential matrix


    def populate_real_space_matrix(self):



        return 0

    def generate_density_matrix(self):



        return 0

    def generate_potential_matrix(self):



        return 0

    def update_particle_positions(self): #call solve force, velocity and position per particle



        return 0


















