import numpy as np
import matplotlib.pyplot as plt

S = np.array([1,2,4,6,8,10])
tpHL = 1e-7 * np.array([1.07143, 0.695402, 0.408046, 0.281609, 0.218391, 0.172414])
tpLH = 1e-7 * np.array([0.64881, 0.65517, 0.65517, 0.65517, 0.65517, 0.65517])
tp = 0.5*(tpLH + tpHL)

plt.grid()
plt.title(r"$t_{p}$ vs $S$")
plt.xlabel(r"$S$")
plt.ylabel(r"$t_{p}$")
plt.plot(S,tp)
plt.scatter(S,tp,color='r')
plt.savefig("../Images/1b2.png")
plt.show()
