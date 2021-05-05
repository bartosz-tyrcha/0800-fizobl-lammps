import numpy as np
import matplotlib.pyplot as plt

t, dist, cord = np.loadtxt("irtg-school-mainz-2020/COLVAR-driver", unpack=True)

t = t * 1e-2  # ps

plt.figure()
plt.plot(t, dist, color="olivedrab")
plt.xlabel("Czas [ps]")
plt.ylabel("Odległość pomiędzy Na-Cl [nm]")
plt.title("Zależnośc odległosci Na-Cl od czasu")

plt.figure()
plt.plot(t, cord, color="olivedrab")
plt.xlabel("Czas [ps]")
plt.ylabel("Liczba koordynacyjna")
plt.title("Zależnośc liczby koordynacyjnej od czasu")
plt.show()