# Scott Crawshaw
# 2/17/19
# system.py
# Submission for Lab 2

from math import sqrt


class System:
    GRAVITY = 6.67384E-11  # gravitational constant

    def __init__(self, body_list):
        self.bodies = body_list

    def draw(self, cx, cy, pixels_per_meter):
        for body in self.bodies:
            body.draw(cx, cy, pixels_per_meter)

    def update(self, timestep):
        for body in self.bodies:
            ax, ay = self.calculate_acceleration(body)
            body.update_velocity(ax, ay, timestep)
            body.update_position(timestep)

    def calculate_acceleration(self, obj):
        # returns the total x and y acceleration on a given body
        ax = 0
        ay = 0

        for body in self.bodies:
            if body.x != obj.x or body.y != obj.y:
                # adds up the accelerations due to all other bodies
                numerator = System.GRAVITY * body.mass
                distance = self.get_distance(obj, body)
                denominator = distance ** 2

                acceleration = numerator / denominator
                partial_ax, partial_ay = self.get_accel_components(acceleration, distance, obj, body)
                ax += partial_ax
                ay += partial_ay

        return ax, ay

    def get_distance(self, body1, body2):
        # returns the distance between two bodies
        dy = body2.y - body1.y
        dx = body2.x - body1.x

        distance = sqrt(dx ** 2 + dy ** 2)

        return distance

    def get_accel_components(self, acceleration, distance, body1, body2):
        # return the x and y components of a given acceleration between two bodies
        dy = body2.y - body1.y
        dx = body2.x - body1.x

        ax = acceleration * (dx / distance)
        ay = acceleration * (dy / distance)

        return ax, ay
