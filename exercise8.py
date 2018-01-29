import random
import sys

from pygame import display, draw, time, event, KEYDOWN, NOEVENT

screen = display.set_mode([800, 600])
screen.fill([0, 0, 0])

class Circle(object):

    def __init__(self):
        """
        Generates a random circle.
        """

        self.colour = [random.randint(0, 255) for i in range(3)]
        self.center = [random.randint(50, 750), random.randint(50, 550)]
        self.radius = 10

    def draw(self):
        """
        Draw the circle.
        """

        draw.circle(screen, self.colour, self.center, self.radius, 1)

    def grow(self):
        """
        Make the circle grow!
        """

        self.radius = self.radius + 1


circles = []

display.flip()

clock = time.Clock()

while True:
    # Detect events and exit upon keypress
    ev = event.poll()
    if ev.type == KEYDOWN:
        sys.exit(0)

    screen.fill([0, 0, 0])
    for circle in circles:
        circle.draw()
        circle.grow()

    display.flip()

    # Remove circles too big
    circles = [c for c in circles if c.radius < 160 + random.randint(1, 40)]

    # Add new circle, if necessary
    if len(circles) < 50 + random.randint(1, 20):
        if random.random() > 0.90 + (len(circles) / 1000.0):
            circles.append(Circle())

    clock.tick(60)