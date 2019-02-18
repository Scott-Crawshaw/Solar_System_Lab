# Scott Crawshaw
# 2/15/19
# solar_interactive.py
# Extra credit submission for Lab 2. Modified version of solar.py

from math import sqrt
from random import randint
from time import time

from body import Body
from cs1lib import *
from system import System

WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650

GRAVITY = 6.67384E-11  # gravitational constant

TIME_SCALE = 1000000  # real seconds per simulation second
PIXELS_PER_METER = 3 / 2.5e9  # distance scale for the simulation

FRAMERATE = 100  # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def press(x, y):
    global press_time, pressed, press_coords, new_planet_size

    press_time = time() - 1
    pressed = True
    press_coords = [x, y]
    new_planet_size = 1


def release(x, y):
    global solar, press_time, pressed, press_coords

    pressed = False

    mass = 3.30e23 * (10 ** (new_planet_size / 6))  # trial and error

    distance_from_sun = sqrt((x - (WINDOW_WIDTH / 2)) ** 2 + (y - (WINDOW_HEIGHT / 2)) ** 2) / PIXELS_PER_METER

    dy = ((y - (WINDOW_HEIGHT / 2)) / PIXELS_PER_METER)
    dx = ((x - (WINDOW_WIDTH / 2)) / PIXELS_PER_METER)

    sin = dy / distance_from_sun
    cos = dx / distance_from_sun

    speed = sqrt((GRAVITY * sun.mass) / distance_from_sun)  # got this orbital speed equation from Wikipedia

    # randomize color but don't allow for colors that are too dark
    r = randint(10, 100) / 100
    g = randint(10, 100) / 100
    b = randint(10, 100) / 100

    new_body = Body(mass, dx, dy, speed * sin, -speed * cos, new_planet_size, r, g, b)

    solar.bodies.append(new_body)


def planet_preview():
    global new_planet_size

    new_planet_size = (time() - press_time) ** 2  # trial and error
    draw_circle(press_coords[0], press_coords[1], new_planet_size)


def main():
    set_clear_color(0, 0, 0)  # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)

    if pressed:
        planet_preview()


sun = Body(1.98892e30, 0, 0, 0, 0, 30, 1, 1, 0)
mercury = Body(3.30e23, 5.79e10, 0, 0, -47400, 3, 1, 0.5, 0)
venus = Body(4.87e24, 1.082e11, 0, 0, -35000, 8, 0, 1, 0)
earth = Body(5.9736e24, 1.496e11, 0, 0, -29800, 8, 0, 0, 1)
mars = Body(6.42e23, 2.279e11, 0, 0, -24100, 4, 1, 0, 0)

solar = System([sun, mercury, venus, earth, mars])

# added these variables for interactive planet creating functionality
press_time = None
press_coords = []
pressed = False
new_planet_size = 1

start_graphics(main, 2400, framerate=FRAMERATE, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, mouse_press=press,
               mouse_release=release)
