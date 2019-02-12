from cs1lib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = pixel_radius
        self.red = r
        self.green = g
        self.blue = b

    def draw(self, cx, cy, pixels_per_meter):
        disable_stroke()
        set_fill_color(self.red, self.green, self.blue)
        draw_circle(cx + self.x * pixels_per_meter, cy + self.y * pixels_per_meter, self.radius)

    def update_velocity(self, ax, ay, timestep):
        self.vx += (ax * timestep)
        self.vy += (ay * timestep)

    def update_position(self, timestep):
        self.x += (self.vx * timestep)
        self.y += (self.vy * timestep)
