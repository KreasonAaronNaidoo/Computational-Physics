import N_Body
import matplotlib.pyplot as plt
import random as ran



if __name__ == "__main__":



    system = N_Body.N_Body()

    system.populate_real_space_matrix()



    system.generate_density_matrix()

    system.generate_potential_matrix()

    system.update_particle_positions()

    for i in range(len(system.real_space_list)):

        #plt.plot(system.real_space_list[i].position_x,system.real_space_list[i].position_y, "o")

