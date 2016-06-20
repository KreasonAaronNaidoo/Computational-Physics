import N_Body
import matplotlib.pyplot as plt
import random as ran



if __name__ == "__main__":



    system = N_Body.N_Body(3) #pass in the mode

    system.populate_real_space_matrix()

    n = 0

    while(True): #This is the main loop

        system.generate_density_matrix()

        system.generate_potential_matrix()

        system.update_particle_positions()

        n = n + 1

        print n


        #plt.plot(system.real_space_list[i].position_x,system.real_space_list[i].position_y, "o")