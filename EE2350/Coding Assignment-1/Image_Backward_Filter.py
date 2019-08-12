"""
In this we will try to apply Backward Differencing Method to an Image.
Using this we will get the edges of an Image.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
import tkinter
import PIL
from skimage.color import rgb2gray

img_original = scipy.ndimage.imread('img.jpg')							# Reading Image
print (img_original.dtype)
img_original_T = img_original.transpose(1,0,2)
#img_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
img_grayscale = rgb2gray(img_original)									# Converting RGB into Grayscale
print (img_grayscale.dtype)
img_grayscale_T = img_grayscale.transpose(1,0)							# Calculating Transpose for Applying Vertical Filter

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
	
def Apply_Filter_Array(x):												# Function to apply filter on a array 
	"""
	Applying Backward Differencing System/Filter on an array
	"""
	h = Backward_Differencing()
	s = np.shape(x)
	output = np.convolve(x,h)
	output = output.astype(float)										# Values are requested to be in float
	M,m = max(output),min(output)
	
	return output/(M-m)													# Normalising Values


def Apply_Filter_RGB(img,fs = 2):										# Function to apply filter on a RGB image
	"""
	Applying Backward Differencing Method to RGB image
	"""							
	img = img.astype(float)
	size_original = np.shape(img)
	i,j,k = size_original[0],size_original[1],size_original[2]
	output = np.zeros((i,j+fs-1,k),dtype = float)
	
	for n in range(k):
		for l in range(i):
			output[l,:,n] = Apply_Filter_Array(img[l,:,n])
				
	return output/1.0

def Apply_Filter_Grayscale(img,fs = 2):									# Function to apply filter on a Grayscale image
	"""
	Applying Backward Differencing Method to Grayscale image
	"""
	size_original = np.shape(img)
	i,j= size_original[0],size_original[1]
	output = np.zeros((i,j+fs-1))
	
	for l in range(i):
		output[l,:] = Apply_Filter_Array(img[l,:])
				
	return output


def Pad_rows_G(img):													# Function to Pad rows to Grayscale image
	"""
	Adding Rows to Gray Scale Image
	"""
	i,j = img.shape[0],img.shape[1]
	z = np.zeros((1,j))
	output = np.append(img, z, axis=0)
	
	return output
	
def Pad_columns_G(img):													# Function to Pad colums to Grayscale image
	"""
	Adding Columns to Gray Scale
	"""
	i,j = img.shape[0],img.shape[1]
	z = np.zeros((i,1))
	output = np.append(img, z, axis=1)
	
	return output

def Pad_rows_RGB(img):													# Function to Pad rows to RGB image
	"""
	Adding Rows to RGB Image
	"""													
	i,j,k = img.shape[0],img.shape[1],img.shape[2]
	z = np.zeros((1,j,k),dtype = float)
	output = np.append(img, z, axis=0)
	
	return output/1.0
	
def Pad_columns_RGB(img):												# Function to Pad columns to RGB image
	"""
	Adding Columns to RGB Image
	"""	
	i,j,k = img.shape[0],img.shape[1],img.shape[2]
	z = np.zeros((i,1,k),dtype= float)
	output = np.append(img, z, axis=1)
	
	return output/1.0


# Applying Backward Differencing Filter to Grayscale Image

img_G_Horizontal_edges = Apply_Filter_Grayscale(img_grayscale)
img_G_Vertical_edges = Apply_Filter_Grayscale(img_grayscale_T)
img_G_Vertical_edges = img_G_Vertical_edges.transpose(1,0)

# Padding the filtered Images
img_G_Horizontal_edges_Padded = Pad_rows_G(img_G_Horizontal_edges)				
img_G_Vertical_edges_Padded = Pad_columns_G(img_G_Vertical_edges)

# Averaging Horizontal and Vertical Grayscale Images
img_G_edges = (img_G_Horizontal_edges_Padded + img_G_Vertical_edges_Padded)/2


# Applying Backward Differencing Filter to RGB Image

img_RGB_Horizontal_edges = Apply_Filter_RGB(img_original)
#img_RGB_Horizontal_edges = PIL.Image.fromarray(img_RGB_Horizontal_edges,'RGB')
img_RGB_Vertical_edges = Apply_Filter_RGB(img_original_T)
img_RGB_Vertical_edges = img_RGB_Vertical_edges.transpose(1,0,2)
#img_RGB_Vertical_edges = PIL.Image.fromarray(img_RGB_Vertical_edges,'RGB')

# Padding the filtered Images
img_RGB_Horizontal_edges_Padded = Pad_rows_RGB(img_RGB_Horizontal_edges)
img_RGB_Vertical_edges_Padded = Pad_columns_RGB(img_RGB_Vertical_edges)

# Averaging Horizontal and Vertical Grayscale Images
img_RGB_edges = (img_RGB_Vertical_edges_Padded + img_RGB_Horizontal_edges_Padded)/2

# Converting a 3D array to Image
img_RGB_edges = PIL.Image.fromarray(img_RGB_edges,'RGB')				

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.imshow(img_G_edges)
ax = plt.subplot(1, 2, 2)
plt.imshow(img_RGB_edges)

plt.show()
