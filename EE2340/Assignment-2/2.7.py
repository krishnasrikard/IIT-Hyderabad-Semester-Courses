import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import string
from pprint import pprint
from collections import OrderedDict

def PMF_ASCII(s):
	
	# Declaring all ascii characters as a Dictionary and assigning their values to 0
	ascii_char_freq = {}
	x = ''.join([chr(i) for i in range(0,255)])
	
	for c in x:
		ascii_char_freq[c] = 0
			
	# Interating over the entire text and incrementing the corresponding ascii_char only
	for v in s:
		if v in x:
			ascii_char_freq[v] += 1
			
	# Total no.of ascii_char detected		
	Total_Char = sum(ascii_char_freq.values())
	
	# Calculating the fraction of each ascii_char_freq in all the ascii_char_freq
	for key in ascii_char_freq:
		ascii_char_freq[key] = (ascii_char_freq[key] /Total_Char)
	
	# Creating a Dictionary of ASCII Characters having non zero frequency	
	PMF = {x:y for x,y in ascii_char_freq.items() if y!= 0}
	
	return PMF,Total_Char
	
	
def Entropy(p):
	# Calculating Entropy for Probability Values
	p = np.array(list(p))
	lp = -1 * np.log2(p)
	entropy = np.sum(np.multiply(p,lp))
	
	return entropy
	
	
# Reading the Input text file
file1 =  open('file1.txt', 'r+', encoding='utf-8')
data = file1.read()
file1.close()
print ("Length of Data",len(data))	
print ("--------------------------------------------------------------")
		

# Printing the Dictionary containing data of ASCII Characters Frequency in text file in seperate lines.
PMF,Total_Characters = PMF_ASCII(data)
print ("PMF of each ASCII Character in given file")
pprint (PMF)
print ("--------------------------------------------------------------")
print ("No.of unique ASCII Characters:",len(PMF))
print ("--------------------------------------------------------------")

# Calculate Entropy
H = Entropy(PMF.values())
print ("Entropy of given text file is",H)
print ("--------------------------------------------------------------")

# Total Optimal Size
O = Total_Characters * H / 8.0
print ("Optimal Size of given text file is",O)
print ("--------------------------------------------------------------")

# Ploting Histogram for all ascii_char
plt_ = sns.barplot(list(PMF.keys()), list(PMF.values()))
plt_.set_xticklabels(plt_.get_xticklabels(), rotation=90)
plt.show() 
