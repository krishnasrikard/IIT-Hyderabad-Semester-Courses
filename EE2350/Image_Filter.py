import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
from skimage.color import rgb2gray

img_original = scipy.ndimage.imread('img.png')							# Reading Image
img_grayscale = rgb2gray(img_original)									# Converting RGB into Grayscale

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.imshow(img_original)
ax = plt.subplot(1,2,2)
plt.imshow(img_grayscale)
plt.show()

size_original = np.shape(img_original)
size_grayscale = np.shape(img_grayscale)

print (size_original,size_grayscale)
i,j,k = size_original[0],size_original[1],size_original[2]
print (i,j,k)

def Backward_Differencing():											# Back Differencing Filter
	h = np.zeros(2)
	h[0],h[1] = 1,-1
	
	return h
	
def Apply_Filter_OneDirection(x):										# Appyling Filter on a array 
	h = Backward_Differencing()
	s = np.shape(x)
	output = np.convolve(x,h)
	
	return output


def Apply_Filter_RGB(img):												
	# Incomplete
	size_original = np.shape(img)
	i,j,k = size_original[0],size_original[1],size_original[2]
	output = np.zeros((i,j+1,k))
	
	for n in range(k):
			for l in range(i):
				output[l,:,n] = Apply_Filter_OneDirection(img[l,:,n])
				
	return output/255

def Apply_Filter_Grayscale(img):										# Applying Filter on an image(Grayscale)
	
	size_original = np.shape(img)
	i,j= size_original[0],size_original[1]
	output = np.zeros((i,j+1))
	
	for l in range(i):
		output[l,:] = Apply_Filter_OneDirection(img[l,:])
				
	return output

img_G_Horizontal_edges = Apply_Filter_Grayscale(img_grayscale)
plt.imshow(img_G_Horizontal_edges)
plt.show()

img_RGB_Horizontal_edges = Apply_Filter_RGB(img_original)
plt.imshow(img_RGB_Horizontal_edges)
plt.show()
