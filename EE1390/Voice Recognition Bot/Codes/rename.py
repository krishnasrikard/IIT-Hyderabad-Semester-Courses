import numpy as np
import os


os.chdir("/home/krishna/Desktop/Voice Recognition/Samples/Stop")

path = os.getcwd()
print path
filenames = os.listdir(path)
i=0
for f in filenames:
	a = "stop"+str(i)+".wav"
	os.rename(f,a)
	i = i+1
	print a
			

