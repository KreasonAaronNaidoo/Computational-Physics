import N_Body
import matplotlib.pyplot as plt
import matplotlib.animation as animation



if __name__ == "__main__":



    system = N_Body.N_Body()  # pass in the mode and GS

    system.populate_real_space_list()

    system.generate_softened_potential_matrix()

    x = [None]*len(system.real_space_list)
    y = [None]*len(system.real_space_list)



    def convert_positions_to_list():

        for i in range(len(system.real_space_list)):

            x[i] = system.real_space_list[i].position_x
            y[i] = system.real_space_list[i].position_y



    def drawB():


        plt.imshow(system.density_matrix)

        axes = plt.gca()
        axes.set_xlim([0, 8])
        axes.set_ylim([0, 8])

        plt.pause(.1)


    def update_system():

        system.generate_density_matrix()

        system.generate_potential_matrix()

        system.update_particle_positions()

        convert_positions_to_list()


    def drawA(i):

        update_system()

        ax.clear()
        ax.scatter(x, y, marker="o")
        ax.set_xlim([0, 8])
        ax.set_ylim([0, 8])
        ax.set_title('N - Body Simulation')


    fig, ax = plt.subplots(subplot_kw={'xlim': [0, 8], 'ylim': [0, 8]})
    ax.set_title('N - Body Simulation')


    ani = animation.FuncAnimation(fig, drawA, interval=16)

    plt.show()







