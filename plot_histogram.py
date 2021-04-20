import numpy as np
import matplotlib.pyplot as plt

time, dist, cord = np.loadtxt("irtg-school-mainz-2020/COLVAR-driver", unpack=True)

plt.figure()
plt.hist(dist, bins=100, density=True, color="olivedrab")
plt.xlabel("Odległość pomiędzy Na-Cl [nm]")
plt.title("Histogram")
plt.show()
