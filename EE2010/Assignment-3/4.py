import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
# Axes3D import has side effects, it enables using projection='3d' in add_subplot


def function1(x, y):													# Function to return z = x^2 + y^2
    return x**2 + y**2
    

def function2(x, y):													# Function to return z = x^2 - y^2
    return x**2 - y**2
    
x = y = np.arange(-1.0, 1.0, 0.01)
X, Y = np.meshgrid(x, y)

zs1 = np.array(function1(np.ravel(X), np.ravel(Y)))
Z1 = zs1.reshape(X.shape)

zs2 = np.array(function2(np.ravel(X), np.ravel(Y)))
Z2 = zs2.reshape(X.shape)

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(X, Y, Z1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V(x,y)')


ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot_surface(X, Y, Z2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V(x,y)')

plt.show()
