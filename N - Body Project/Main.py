import NBody
import matplotlib.pyplot as plt
import random as ran



system = NBody.N_Body()

for x in range(1,101,1): #this will add 100 particles to the system

    system.add(ran.randint(1,101), ran.randint(1,51), ran.randint(1,51))

for i in range(len(system.part)):

    plt.plot(system.part[i].x , system.part[i].y, "ro")

plt.axis([-10, 60, -10, 60])
plt.show()

system.setTotalForce()
system.setA()
system.setV()
system.setx()

for i in range(len(system.part)):

    plt.plot(system.part[i].x , system.part[i].y, "ro")

plt.axis([-10, 60, -10, 60])
plt.show()


print
print
print system.tot_pot_energy()



