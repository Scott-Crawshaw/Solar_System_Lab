from math import sqrt

class System:
    GRAVITY = 6.67384E-11

    def __init__(self, body_list, timestep=1):
        self.bodies = body_list
        self.timestep = timestep

    def draw(self):
        for body in self.bodies:
            body.draw()

    def update(self):
        for body in self.bodies:
            ax, ay = self.calculate_acceleration(body)
            body.update_velocity(ax, ay, self.timestep)

    def calculate_acceleration(self, obj):
        ax = 0
        ay = 0

        for body in self.bodies:
            if body.x != obj.x or body.y != obj.y:
                numerator = System.GRAVITY * body.mass
                distance = self.get_r(obj, body)
                denominator = distance ** 2
                acceleration = numerator / denominator
                partial_ax, partial_ay = self.get_accel_components(acceleration, distance, obj, body)
                ax += partial_ax
                ay += partial_ay

        return ax, ay

    def get_r(self, body1, body2):
        dy = body2.y - body1.y
        dx = body2.x - body1.x

        distance = sqrt(dx ** 2 + dy ** 2)

        return distance

    def get_accel_components(self, acceleration, distance, body1, body2):
        dy = body2.y - body1.y
        dx = body2.x - body1.x

        ax = acceleration * (dx / distance)
        ay = acceleration * (dy / distance)

        return ax, ay
