import numpy as np
import matplotlib.pyplot as plt

S = np.array([1,2,4,6,8,10])
tpHL = 1e-7 * np.array([1.07143, 0.692982, 0.408046, 0.280702, 0.219298, 0.184211])
tpLH = 1e-7 * np.array([0.64881, 0.34211, 0.17816, 0.12281, 0.0965, 0.07018])
tp = 0.5*(tpLH + tpHL)

plt.grid()
plt.title(r"$t_{p}$ vs $S$")
plt.xlabel(r"$S$")
plt.ylabel(r"$t_{p}$")
plt.plot(S,tp)
plt.scatter(S,tp,color='r')
plt.savefig("../Images/1a.png")
plt.show()
