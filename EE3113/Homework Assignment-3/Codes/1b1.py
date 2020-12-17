import numpy as np
import matplotlib.pyplot as plt

S = np.array([1,2,4,6,8,10])
tpHL = 1e-7 * np.array([1.07143, 1.06322, 1.06322, 1.06322, 1.06322, 1.06322])
tpLH = 1e-7 * np.array([0.64881, 0.336392, 0.16667, 0.12069, 0.08621, 0.07471])
tp = 0.5*(tpLH + tpHL)

plt.grid()
plt.title(r"$t_{p}$ vs $S$")
plt.xlabel(r"$S$")
plt.ylabel(r"$t_{p}$")
plt.plot(S,tp)
plt.scatter(S,tp,color='r')
plt.savefig("../Images/1b1.png")
plt.show()
