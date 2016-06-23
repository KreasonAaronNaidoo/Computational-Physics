import N_Body
import matplotlib.pyplot as plt
import random as ran



if __name__ == "__main__":

    print("Simulations modes:")
    print("Mode 1: Single particla starting at rest")
    print("Mode 2: Two particles starting rest ")
    print("Mode 3: Full N-body simulation")
    print
    user = input("Please input the simulation mode:  ")

    print

    mode = int(user)

    system = N_Body.N_Body(mode) #pass in the mode

    x,y = [],[]

    plt.ion()

    system.populate_real_space_list()

    print len(system.real_space_list)

    plt.imshow(system.potential_matrix);



    def convert_positions_to_list():

        for i in range(len(system.real_space_list)):

           # print(system.real_space_list[i].position_x)


            x.append(system.real_space_list[i].position_x)
            y.append(system.real_space_list[i].position_y)




    def draw():

        plt.clf()


        plt.plot(x, y, ".")

        plt.draw()

        plt.pause(.1)





    while(True): #This is the main loop

        system.generate_density_matrix()

        system.generate_potential_matrix()

        plt.imshow(system.potential_matrix)

        plt.pause(30)

        system.update_particle_positions()

        convert_positions_to_list()

        draw()