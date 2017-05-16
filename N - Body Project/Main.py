import N_Body
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import time



if __name__ == "__main__":

    print
    print
    print("Simulations modes:")
    print
    print("Mode 1: Single particla starting at rest ")
    print("Mode 2: Two particles starting rest ")
    print("Mode 3: Three particles starting rest ")
    print("Mode 4: Four particles starting rest ")
    print("Mode 5: Full N-body simulation")
    print
    user1 = input("Please input the simulation mode:  ")

    print

    mode1 = int(user1)

    print
    print "Output modes:"
    print
    print("Mode 1: Display actual position data (Recomended)")
    print("Mode 2: Display an approximation of the actual positions in the form of a density grid (this mode is buggy and not recomended)")
    print
    user2 = input("Please input the display mode:  ")

    print

    mode2 = int(user2)


    print
    print "Periodicity modes:"
    print
    print("Mode 1: Periodic environment ")
    print("Mode 2: Non - periodic environment")
    print
    user3 = input("Please input the periodicity mode:  ")

    print

    mode3 = int(user3)


    Grid_Size = 0

    #plt.ion()



    if(mode1 == 1 or mode1 == 2 or mode1 == 3 or mode1 == 4):
        Grid_Size = 8
    else:
        Grid_Size = 100



    system = N_Body.N_Body(Grid_Size ,mode1, mode3)  # pass in the mode and GS

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
        axes.set_xlim([0, Grid_Size])
        axes.set_ylim([0, Grid_Size])

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
        ax.set_xlim([0, Grid_Size])
        ax.set_ylim([0, Grid_Size])
        ax.set_title('N - Body Simulation')





    if(mode2 == 1):

        fig, ax = plt.subplots(subplot_kw={'xlim': [0, Grid_Size], 'ylim': [0, Grid_Size]})
        ax.set_title('N - Body Simulation')

        ani = animation.FuncAnimation(fig, drawA, interval=16)

        plt.show()



    else:

        while(True):
            update_system()
            drawB()



