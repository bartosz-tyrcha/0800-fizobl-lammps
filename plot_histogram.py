import numpy as np
import matplotlib.pyplot as plt

time, dist, cord = np.loadtxt("irtg-school-mainz-2020/COLVAR-driver", unpack=True)

plt.figure()
hist = plt.hist(dist, bins=100, density=True, color="olivedrab")
plt.xlabel("Odległość pomiędzy Na-Cl [nm]")
plt.title("Histogram")
#plt.show()

temp = 300  # K
#k = 0.0083144626  # kJ/(mol*K)
k = 8.6173333e-05  # eV/K

N = hist[0]
bins = hist[1]

F = - np.log(N) * k * temp

plt.figure()
plt.hist(bins[:-1], bins=bins, weights=F)
plt.xlabel("Odległość pomiędzy Na-Cl [nm]")
plt.ylabel("F [eV]")
plt.show()
