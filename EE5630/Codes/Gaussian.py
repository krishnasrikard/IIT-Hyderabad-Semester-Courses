# Properties of Gaussian Function in Time and Fourier Domain
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal
import seaborn as sns

# DFT of a 2D Matrix
def DFTMatrixMultiplication(I):
    N = I.shape[0]
    w = np.exp(-1.0 * 2j * np.pi/N)

    W = 1j * np.zeros(I.shape)
    
    for i in range(N):
        for j in range(N):
            W[i][j] = pow(w,i*j)
            
    I_DFT = np.dot(W,np.dot(I,W))
    return I_DFT
    
# DFT of a 2D Matrix with Zero Frequencies at the Center
def CenteredDFT(img):
    I = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            I[i][j] = pow(-1,i+j) * img[i][j]
            
    return DFTMatrixMultiplication(I)
    
# IDFT of a DFT of a 2D-Matrix
def IDFTMatrixMultiplication(I_DFT):
    N = I_DFT.shape[0]
    w = np.exp(-1.0 * 2j * np.pi/N)
    W = 1j * np.zeros(I_DFT.shape)
    
    for i in range(N):
        for j in range(N):
            W[i][j] = pow(w,i*j)
            
    Winv = np.linalg.inv(W)
    I_IDFT = np.dot(Winv,np.dot(I_DFT,Winv))
    
    I_IDFT = I_IDFT
    return I_IDFT.real


# X and Y Limits
x, y = np.mgrid[-2:2:50j, -2:2:50j]
xy = np.column_stack([x.flat, y.flat])

# Parameters of 2D-Gaussain
mu = np.array([0.0, 0.0])
covariance = np.array([[0.2,0], [0,0.2]])

# Plotting MultiVariate Gaussian Distribution
z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)
z = np.round(z.reshape(x.shape),decimals=2)

# FFT of Gaussian
zfft = np.round(np.abs(CenteredDFT(z)),decimals=2)


# Plotting and Saving Results
color_map = plt.cm.get_cmap('jet')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, cmap=color_map)
plt.title("Gaussian Distribution")
plt.savefig("../Images/Gaussian.png")
plt.show()

fig = plt.figure()
ax = sns.heatmap(z, cmap=color_map, xticklabels=False, yticklabels=False)
plt.title("Gaussian Distribution Heat-Map")
plt.savefig("../Images/Gaussian_HeatMap.png")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,zfft, cmap=color_map)
plt.title("Zero-Centered DFT of Gaussian Distribution")
plt.savefig("../Images/ZeroCentered_Gaussian_DFT.png")
plt.show()

fig = plt.figure()
ax = sns.heatmap(zfft, cmap=color_map, xticklabels=False, yticklabels=False)
plt.title("Zero-Centered DFT of Gaussian Distribution Heat-Map")
plt.savefig("../Images/ZeroCentered_Gaussian_DFT_HeatMap.png")
plt.show()
