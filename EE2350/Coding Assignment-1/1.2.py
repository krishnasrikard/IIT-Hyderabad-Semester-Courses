# We will Quantise a Grayscale Image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
import tkinter
import PIL
from skimage.color import rgb2gray

img_original = scipy.ndimage.imread('img.jpg')							# Reading Image
img_grayscale = rgb2gray(img_original)									# Converting RGB into Grayscale

img_grayscale = img_grayscale.astype(float)

size_grayscale = np.shape(img_grayscale)

i,j = size_grayscale[0],size_grayscale[1]

def Quantise_Signal(data,N):											# Function to Quantise a given Signal
	"""
	data = Signal that has to be quantised
	N = No.of bits
	"""
	b,a = max(data),min(data)
	
	data_new = np.ceil((data - a)*(2**N - 1)/(b-a))
	data_new = (data_new /(2**N - 1))*(b-a) + a
	
	return data_new
	
def Quantise_Grayscale(img,N):											# Function to quantise a Grayscale image
	"""
	Quantising a Grayscale image
	"""
	size_original = np.shape(img)
	i,j= size_original[0],size_original[1]
	output = np.zeros((i,j))
	
	for l in range(i):
		output[l,:] = Quantise_Signal(img[l,:],N)
				
	return output


Quantise_values = [64,32,16,8,4,2]

for i in Quantise_values:
	img_quantised = Quantise_Grayscale(img_grayscale,i)
	plt.imshow(img_quantised)
	plt.show()
