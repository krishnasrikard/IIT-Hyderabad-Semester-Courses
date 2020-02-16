import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import cm

Denominator = [1 , 10001, 10000]
Numerator = [1]

s1 = signal.lti(Numerator, Denominator)
w, mag, phase = signal.bode(s1)
plt.figure()
plt.grid(b=1)
plt.title("Magnitude Plot")
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.grid(b=1)
plt.title("Phase Plot")
plt.semilogx(w, phase)  # Bode phase plot
plt.show()
