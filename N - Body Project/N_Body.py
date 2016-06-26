
import particle
import numpy as np
import random as rand



class N_Body:


    def __init__(self, GS,  mode = 1):


        self.Number_of_particles = 100  #Number of particles

        self.Grid_Size = GS #The grid is this number on each side

        self.dt = 0.05

        self.real_space_list = [] # this is where the particles will live

        self.density_matrix = np.zeros((self.Grid_Size, self.Grid_Size))  # this stores the density matrix

        self.potential_matrix = np.zeros((self.Grid_Size, self.Grid_Size)) # this stores the potential matrix

        self.softened_potential_matrix = np.zeros((self.Grid_Size, self.Grid_Size)) # this stores the S potential matrix

        self.periodic = False
        #Change this value to change to the system to periodic

        self.mode = mode
        #mode == 1 : single stationary particle
        #mode == 2 : 2 stationary particles
        #mode == 3 : Full N-Body simulation





    def populate_real_space_list(self):


        if(self.mode == 1):
            self.real_space_list.append(particle.particle(1, self.Grid_Size/2.0, self.Grid_Size/2.0))

        if(self.mode == 2):
            self.real_space_list.append(particle.particle(1, self.Grid_Size / 3.0 , self.Grid_Size / 2.0))
            self.real_space_list.append(particle.particle(1, self.Grid_Size - self.Grid_Size / 3.0, self.Grid_Size / 2.0))

        if(self.mode == 3):

            for x in range(0, self.Number_of_particles):
                temp_x = rand.uniform(0, self.Grid_Size - 1)
                temp_y = rand.uniform(0, self.Grid_Size - 1)

                temp_particle = particle.particle(1, temp_x, temp_y) # we are using the uniform mass of 1

                self.real_space_list.append(temp_particle)
                #adds the particle to the list of particles at that point in the real space matrix






    def generate_density_matrix(self):


        for i in range(len(self.real_space_list)):

            round_x = int(round(self.real_space_list[i].position_x))
            round_y = int(round(self.real_space_list[i].position_y))

            self.real_space_list[i].round_x = round_x
            self.real_space_list[i].round_y = round_y

            if (round_x > self.Grid_Size - 1):
                round_x = self.Grid_Size - 2
            if (round_y >  self.Grid_Size - 1):
                round_y = self.Grid_Size - 2


            self.density_matrix[round_x][round_y] = self.density_matrix[round_x][round_y] + 1
            #This creates the density matrix
        #print self.real_space_list[1].position_x



    def generate_softened_potential_matrix(self):

        for i in range(0,self.Grid_Size / 2):
            for j in range(0, self.Grid_Size / 2):

                if(i == 0 and j == 0):
                    self.softened_potential_matrix[0][0] = 1

                else:

                    r1 = np.sqrt(i**2 + j**2)

                    self.softened_potential_matrix[i][j] = 1.0 / r1


                    j_prime = -1*(j+1)
                    i_prime = -1 * (i + 1)

                    r2 = np.sqrt(i**2 + j_prime**2)

                    self.softened_potential_matrix[i][self.Grid_Size + j_prime] = 1.0 / r2

                    r3 = np.sqrt(i_prime**2 + j**2)

                    self.softened_potential_matrix[self.Grid_Size + i_prime][j] = 1.0 / r3

                    r4 = np.sqrt(i_prime ** 2 + j_prime ** 2)

                    self.softened_potential_matrix[self.Grid_Size + i_prime][self.Grid_Size + j_prime] = 1.0 / r4

        self.softened_potential_matrix[self.Grid_Size - 1][self.Grid_Size - 1] = 1.0 / np.sqrt(2)
        self.softened_potential_matrix[0][self.Grid_Size - 1] = 1
        self.softened_potential_matrix[self.Grid_Size - 1][0] = 1


        #print self.softened_potential_matrix[0][0] , self.softened_potential_matrix[0][self.Grid_Size - 1]

        #print self.softened_potential_matrix[self.Grid_Size - 1][0], self.softened_potential_matrix[self.Grid_Size - 1][self.Grid_Size - 1]

    def generate_potential_matrix(self):


        fft1 = np.fft.fft(self.density_matrix)

        fft2 = np.fft.fft(self.softened_potential_matrix)


        self.potential_matrix = np.real(np.fft.ifft(fft1 * fft2))
        # we use the fact that the fft of a constant is the same value

        #print self.potential_matrix

    def update_particle_positions(self):

        # print self.density_matrix
        # print self.potential_matrix

        i = 0
        while (i < len(self.real_space_list) - 1):
            deleted = False
            j = i
            for i in range(j, len(self.real_space_list)):

                n = len(self.real_space_list)
                # print i, n, self.real_space_list[i].position_x
                # self.real_space_list[i].print_info();


                # This sets up the force

                current_x = self.real_space_list[i].position_x
                current_y = self.real_space_list[i].position_y

                if (self.periodic == False):

                    if ((current_x - 1 < 0) and (current_y - 1 < 0)):

                        ux_left = 0
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = 0
                        uy_down = self.potential_matrix[current_x][current_y + 1]


                    elif ((current_x - 1 < 0) and (current_y + 1 > self.Grid_Size)):

                        ux_left = 0
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = 0

                    elif ((current_x + 1 > self.Grid_Size) and (current_y - 1 < 0)):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = 0
                        uy_up = 0
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                    elif ((current_x + 1 > self.Grid_Size) and ((current_y + 1 > self.Grid_Size))):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = 0
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = 0


                    elif ((current_y - 1 < 0) and (0 <= current_x <= self.Grid_Size)):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = 0
                        uy_down = self.potential_matrix[current_x][current_y + 1]



                    elif ((current_y + 1 > self.Grid_Size) and (0 <= current_x <= self.Grid_Size)):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = 0



                    elif ((0 <= current_y <= self.Grid_Size) and ((current_x - 1 < 0))):

                        ux_left = 0
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                    elif ((0 <= current_y <= self.Grid_Size) and ((current_x + 1 > self.Grid_Size))):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = 0
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                    else:

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                if (self.periodic == True):

                    if ((current_x - 1 < 0) and (current_y - 1 < 0)):

                        ux_left = self.potential_matrix[self.Grid_Size - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][self.Grid_Size - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]


                    elif ((current_x - 1 < 0) and (current_y + 1 > self.Grid_Size)):

                        ux_left = self.potential_matrix[self.Grid_Size - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][0]

                    elif ((current_x + 1 > self.Grid_Size) and (current_y - 1 < 0)):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[0][current_y]
                        uy_up = self.potential_matrix[current_x][self.Grid_Size - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                    elif ((current_x + 1 > self.Grid_Size) and ((current_y + 1 > self.Grid_Size))):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[0][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][0]


                    elif ((current_y - 1 < 0) and (0 <= current_x <= self.Grid_Size)):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][self.Grid_Size - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]



                    elif ((current_y + 1 > self.Grid_Size) and (0 <= current_x <= self.Grid_Size)):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][0]



                    elif ((0 <= current_y <= self.Grid_Size) and ((current_x - 1 < 0))):

                        ux_left = self.potential_matrix[self.Grid_Size - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                    elif ((0 <= current_y <= self.Grid_Size) and ((current_x + 1 > self.Grid_Size))):

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[0][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                    else:

                        ux_left = self.potential_matrix[current_x - 1][current_y]
                        ux_right = self.potential_matrix[current_x + 1][current_y]
                        uy_up = self.potential_matrix[current_x][current_y - 1]
                        uy_down = self.potential_matrix[current_x][current_y + 1]

                self.real_space_list[i].solve_force(ux_left, ux_right, uy_up, uy_down)

                # This sets up the velocity

                self.real_space_list[i].solve_velocity(self.dt)

                # This sets up the position

                self.real_space_list[i].solve_position(self.dt)

                if (self.periodic == True):

                    while (self.real_space_list[i].position_x <= 0):  # put in =
                        self.real_space_list[i].position_x = self.Grid_Size + self.real_space_list[i].position_x

                    while (self.real_space_list[i].position_x >= self.Grid_Size):
                        self.real_space_list[i].position_x = self.real_space_list[i].position_x - self.Grid_Size

                    while (self.real_space_list[i].position_y <= 0):  # put in =
                        self.real_space_list[i].position_y = self.Grid_Size + self.real_space_list[i].position_y

                    while (self.real_space_list[i].position_y >= self.Grid_Size):
                        self.real_space_list[i].position_y = self.real_space_list[i].position_y - self.Grid_Size

                if (self.periodic == False):

                    while (self.real_space_list[i].position_x <= 0):
                        del self.real_space_list[i]
                        n = n - 1
                        i = i-1
                        deleted = True
                        break

                    while (self.real_space_list[i].position_x >= self.Grid_Size):
                        del self.real_space_list[i]
                        n = n - 1
                        i = i - 1
                        deleted = True
                        break
                    while (self.real_space_list[i].position_y <= 0):
                        del self.real_space_list[i]
                        n = n - 1
                        i = i - 1
                        deleted = True
                        break
                    while (self.real_space_list[i].position_y >= self.Grid_Size):
                        del self.real_space_list[i]
                        n = n - 1
                        i = i - 1
                        deleted = True
                        break
                    if deleted:
                        print "del"
                        break






