import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
import tkinter
import PIL
from skimage.color import rgb2gray

img_original = scipy.ndimage.imread('img.png')							# Reading Image
img_original_T = img_original.transpose(1,0,2)
#img_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
img_grayscale = rgb2gray(img_original)									# Converting RGB into Grayscale
img_grayscale_T = img_grayscale.transpose(1,0)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.imshow(img_original)
ax = plt.subplot(1,2,2)
plt.imshow(img_grayscale)
plt.show()

size_original = np.shape(img_original)
size_grayscale = np.shape(img_grayscale)


i,j,k = size_original[0],size_original[1],size_original[2]

def Backward_Differencing():											# Back Differencing Filter
	h = np.zeros(2)
	h[0],h[1] = 1.0,-1.0
	
	return h
	
def Apply_Filter_OneDirection(x):										# Appyling Filter on a array 
	h = Backward_Differencing()
	s = np.shape(x)
	output = np.convolve(x,h)
	output = output.astype(float)
	M,m = max(output),min(output)
	
	return output/(M-m)


def Apply_Filter_RGB(img,fs = 2):
								
	img = img.astype(float)
	size_original = np.shape(img)
	i,j,k = size_original[0],size_original[1],size_original[2]
	output = np.zeros((i,j+fs-1,k),dtype = float)
	
	for n in range(k):
		for l in range(i):
			output[l,:,n] = Apply_Filter_OneDirection(img[l,:,n])
				
	return output/1.0

def Apply_Filter_Grayscale(img,fs = 2):									# Applying  Filter on an image(Grayscale)
	
	size_original = np.shape(img)
	i,j= size_original[0],size_original[1]
	output = np.zeros((i,j+fs-1))
	
	for l in range(i):
		output[l,:] = Apply_Filter_OneDirection(img[l,:])
				
	return output


def Pad_rows_G(img):
	i,j = img.shape[0],img.shape[1]
	z = np.zeros((1,j))
	output = np.append(img, z, axis=0)
	
	return output
	
def Pad_columns_G(img):
	i,j = img.shape[0],img.shape[1]
	z = np.zeros((i,1))
	output = np.append(img, z, axis=1)
	
	return output

def Pad_rows_RGB(img):
	i,j,k = img.shape[0],img.shape[1],img.shape[2]
	z = np.zeros((1,j,k),dtype = float)
	output = np.append(img, z, axis=0)
	
	return output/1.0
	
def Pad_columns_RGB(img):
	i,j,k = img.shape[0],img.shape[1],img.shape[2]
	z = np.zeros((i,1,k),dtype= float)
	output = np.append(img, z, axis=1)
	
	return output/1.0
			
img_G_Horizontal_edges = Apply_Filter_Grayscale(img_grayscale)
img_G_Vertical_edges = Apply_Filter_Grayscale(img_grayscale_T)
img_G_Vertical_edges = img_G_Vertical_edges.transpose(1,0)

img_G_Horizontal_edges_Padded = Pad_rows_G(img_G_Horizontal_edges)
img_G_Vertical_edges_Padded = Pad_columns_G(img_G_Vertical_edges)

img_G_edges = (img_G_Horizontal_edges_Padded + img_G_Vertical_edges_Padded)/2

img_RGB_Horizontal_edges = Apply_Filter_RGB(img_original)
#img_RGB_Horizontal_edges = PIL.Image.fromarray(img_RGB_Horizontal_edges,'RGB')
img_RGB_Vertical_edges = Apply_Filter_RGB(img_original_T)
img_RGB_Vertical_edges = img_RGB_Vertical_edges.transpose(1,0,2)
#img_RGB_Vertical_edges = PIL.Image.fromarray(img_RGB_Vertical_edges,'RGB')

img_RGB_Horizontal_edges_Padded = Pad_rows_RGB(img_RGB_Horizontal_edges)
img_RGB_Vertical_edges_Padded = Pad_columns_RGB(img_RGB_Vertical_edges)


img_RGB_edges = (img_RGB_Vertical_edges_Padded + img_RGB_Horizontal_edges_Padded)/2
img_RGB_edges = PIL.Image.fromarray(img_RGB_edges,'RGB')

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.imshow(img_G_edges)
ax = plt.subplot(1, 2, 2)
plt.imshow(img_RGB_edges)
plt.show()
