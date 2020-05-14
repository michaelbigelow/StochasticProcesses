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


# part A
bin_edges = [np.round(0.05 * i, 2) for i in range(21)]
print("Computing proportion of trials resulting in fraction of red balls within these intervals...\n", bin_edges)
trials = polyas_urn(num_trials=2000)[1]
hist = np.histogram(trials, bin_edges)[0]

print(hist)

# part B
trials1, trials2 = polyas_urn(num_draws2=1000, num_trials=100)
indicators = []
for i in range(len(trials1)):
    if trials1[i] > trials2[i]:
        indicators.append(1)
    else:
        indicators.append(0)
print("Proportion of trials resulting in M_998 > M_1998 =", np.mean(indicators))

