import numpy as np
import matplotlib.pyplot as plt

time, dist, cord = np.loadtxt("irtg-school-mainz-2020/COLVAR-driver", unpack=True)

plt.figure()
hist = plt.hist(dist, bins=100, density=True, color="olivedrab")
plt.xlabel("Odległość pomiędzy Na-Cl [nm]")
plt.title("Histogram dla odległości Na-Cl")

temp = 300  # K
k = 0.0083144626  # kJ/(mol*K)
# k = 8.6173333e-05  # eV/K

N = hist[0]
bins = hist[1]

F = -np.log(N) * k * temp

dist_prime = []
for i in range(len(bins) - 1):
    dist_prime.append(0.5 * (bins[i] + bins[i + 1]))

plt.figure()
plt.plot(dist_prime, F, color="olivedrab")
plt.xlabel("Odległość pomiędzy Na-Cl [nm]")
plt.ylabel("F [kJ/mol]")
plt.title("Energia swobodna dla odległości Na-Cl")

plt.show()
