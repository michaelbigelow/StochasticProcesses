import numpy as np
from PolyasUrn import Urn


def polyas_urn(num_draws1=998, num_draws2=0, num_trials=100):
    trials1 = np.zeros(num_trials)
    trials2 = np.zeros(num_trials)
    for j in range(num_trials):
        urn = Urn()
        for i in range(num_draws1):
            urn.update()
        trials1[j] = urn.red / num_draws1
        for i in range(num_draws2):
            urn.update()
        trials2[j] = urn.red / (num_draws1 + num_draws2)
    return trials1, trials2


# part A
bin_edges = [np.round(0.05 * i, 2) for i in range(21)]
print("Computing proportion of trials resulting in fraction of red balls within these intervals...\n", bin_edges)
trials = polyas_urn(num_trials=2000)[0]
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