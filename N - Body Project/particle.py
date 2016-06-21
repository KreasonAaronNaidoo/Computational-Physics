

import numpy as np


class particle:

    def __init__(self, m = 1, x = 0, y = 0):

        self.mass = m

        self.position_x = x # x position
        self.position_y = y # y position

        self.round_x = 0    #discrete positions in the density matrix
        self.round_y = 0

        self.force_x = 0 # x force
        self.force_y = 0 # y force

        self.velocity_x = 0 # x velocity
        self.velocity_y = 0 # y velocity

        self.acceleration_x = 0 # x acceleration
        self.acceleration_y = 0 # y acceleration





    def solve_force(self, ux_left, ux_right, uy_up, uy_down):

        self.force_x = -1 * (ux_left - ux_right) / 2
        self.force_y = -1 * (uy_up - uy_down) / 2

        self.acceleration_x = self.force_x / self.mass
        self.acceleration_y = self.force_y / self.mass




    def solve_velocity(self, dt):

        self.velocity_x = self.velocity_x + self.force_x * dt
        self.velocity_y = self.velocity_y + self.force_y * dt

        #print self.velocity_x, self.velocity_y

    def solve_position(self, dt):

        self.position_x = self.position_x + self.velocity_x * dt
        self.position_y = self.position_y + self.velocity_y * dt

    def print_info(self):

        print
        print "position x ", self.position_x," position y ", self.position_y
        print "velocity x ", self.velocity_x, " velocity y ", self.velocity_y
        print "force x ", self.force_x, " force y ", self.force_y
        print "round x ", self.round_x, " round y", self.round_y
        print