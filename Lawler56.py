import numpy as np
from PolyasUrn import polyas_urn

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