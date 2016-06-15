import numpy as np
from matplotlib import pyplot as plt










def mainLoop(dt, t_max):
    kinVec = []

    # position of the particles
    x0 = -10;
    y0 = 5
    x1 = 10;
    y1 = 5

    # velocity of the particles

    vx_x0 = 0;
    vy_x0 = 0
    vx_x1 = 0;
    vy_x1 = 0

    # mass of the particles

    m_x0 = 1
    m_x1 = 1

    # for simplicity lets set G to be 1

    G = 1

    for t in np.arange(0, t_max, dt):
        dx = x0 - x1
        dy = y0 - y1

        r_squared = dx ** 2 + dy ** 2

        r = np.sqrt(r_squared)

        r_cubed = r ** 3

        # Calculate the force components in x and y on particle 1

        fx0 = m_x1 * G * (dx / r_cubed)
        fy0 = m_x1 * G * (dy / r_cubed)

        # By NL3, the forces on the second particle are the negitive of the first

        fx1 = -fx0
        fy1 = -fy0

        # Update the positions of the particles

        x0 = x0 + dt * vx_x0
        y0 = x0 + dt * vy_x0

        x1 = x1 + dt * vx_x1
        y1 = y1 + dt * vy_x1

        # update the velocities of the particles

        vx_x0 = vx_x0 - fx0 * dt
        vy_x0 = vy_x0 - fy0 * dt

        vx_x1 = vx_x1 - fx1 * dt
        vy_x1 = vy_x1 - fy1 * dt

        potential = G * 1.0 / r
        kinetic = 0.5 * (m_x0 * (vx_x0 ** 2 + vy_x0 ** 2) + m_x1 * (vx_x1 ** 2 + vy_x1 ** 2))

        kinVec.append(kinetic)

        return dt,kinVec




a, b = mainLoop(0.2, 5)
print "Max kinectic energy for dt = ",a," is " , max(b)

print
c,d = mainLoop(5, 125)
print "Max kinectic energy for dt = ",c," is " , max(d)



