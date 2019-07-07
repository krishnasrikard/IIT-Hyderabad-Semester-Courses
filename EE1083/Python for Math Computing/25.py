import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.5*np.pi,0.5*np.pi,100)
im_z = (2 - 6*np.sin(t)**2)/(1+4*np.sin(t)**2)
plt.plot(t,im_z)
plt.plot(-np.arcsin(1/np.sqrt(3)),0,'o')
plt.plot(np.arcsin(1/np.sqrt(3)),0,'o')
plt.grid()
plt.xlabel('$\\theta$ (Radians)')
plt.ylabel('Imaginary part')
plt.show()
