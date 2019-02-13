# Scott Crawshaw
# 2/12/19
# solar.py
# Submission for Lab 2. Modified version of earthmoon.py

from body import Body
from cs1lib import *
from system import System

WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650

TIME_SCALE = 1000000  # real seconds per simulation second
PIXELS_PER_METER = 3 / 2.5e9  # distance scale for the simulation

FRAMERATE = 30  # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():
    set_clear_color(0, 0, 0)  # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, 30, 1, 1, 0)
mercury = Body(3.30e23, 5.79e10, 0, 0, 47400, 3, 1, 0.5, 0)
venus = Body(4.87e24, 1.082e11, 0, 0, 35000, 8, 0, 1, 0)
earth = Body(5.9736e24, 1.496e11, 0, 0, 29800, 8, 0, 0, 1)
mars = Body(6.42e23, 2.279e11, 0, 0, 24100, 4, 1, 0, 0)

solar = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
