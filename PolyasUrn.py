import numpy as np
from numpy import random

class Urn:
    def __init__(self, red=1, green=1):
        self.red = red
        self.green = green

    def draw(self):
        balls = self.red + self.green
        prob_dist = [self.red / balls, self.green / balls]
        result = random.choice(["red", "green"], 1, prob_dist)
        if result == "red":
            self.red += 1
        elif result == "green":
            self.green += 1


def polyas_urn(num_draws1=998, num_draws2=0, num_trials=100):
    trials1 = np.zeros(num_trials)
    trials2 = np.zeros(num_trials)
    for j in range(num_trials):
        urn = Urn()
        for i in range(num_draws1):
            urn.draw()
        trials1[j] = urn.red / num_draws1
        for i in range(num_draws2):
            urn.draw()
        trials2[j] = urn.red / (num_draws1 + num_draws2)
    return trials1, trials2