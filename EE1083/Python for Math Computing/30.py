import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,0.5*np.pi,100)
y = -2*x + (2*np.pi)/3

plt.plot(x,y,label='Normal $(y + 2x = 2\pi/3)$')
plt.plot(0,0,'o')
plt.plot(0,2*np.pi/3,'o')
plt.plot(2*np.pi/6,0,'o')
plt.plot(2*np.pi/4,0,'o')
plt.text(0+0.01,0,'(0,0)')
plt.text(0+0.01,2*np.pi/3,'(0,2$\pi$/3)')
plt.text(np.pi/6+0.02,0,'($\pi$/6,0)')
plt.text(np.pi/4+0.02,0,'($\pi$/4,0)')

plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.show()
