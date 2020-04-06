import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import cm

Denominator = [1 , 1, 1]
Numerator = [1,0,0]

s1 = signal.lti(Numerator, Denominator)
w, mag, phase = signal.bode(s1)

plt.figure()
plt.grid(b=1)
plt.title("Magnitude Plot")
plt.semilogx(w, mag)
plt.show()

plt.grid(b=1)
plt.title("Phase Plot")
plt.semilogx(w, phase)

plt.show()
