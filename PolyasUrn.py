from numpy import random

class Urn:
    def __init__(self, red=1, green=1):
        self.red = red
        self.green = green

    def draw(self):
        balls = self.red + self.green
        prob_dist = [self.red / balls, self.green / balls]
        result = random.choice(["red", "green"], p=prob_dist)
        return result

    def update(self):
        draw = self.draw()
        if draw == "red":
            self.red += 1
        elif draw == "green":
            self.green += 1
