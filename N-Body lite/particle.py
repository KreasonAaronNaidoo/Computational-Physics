class particle:

    def __init__(self, x = 0, y = 0):



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

        self.potential = 0





    def solve_force(self, ux_left, ux_right, uy_up, uy_down):

        self.force_x = -1 * (ux_left - ux_right) / 2
        self.force_y = -1 * (uy_up - uy_down) / 2

        self.acceleration_x = self.force_x
        self.acceleration_y = self.force_y


    def solve_velocity(self, dt):

        self.velocity_x = self.velocity_x + self.acceleration_x * dt
        self.velocity_y = self.velocity_y + self.acceleration_y * dt


    def solve_position(self, dt):

        self.position_x = self.position_x + self.velocity_x * dt
        self.position_y = self.position_y + self.velocity_y * dt
