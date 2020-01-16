import seaborn as sns
import matplotlib.pyplot as plt
import string
from pprint import pprint

def PMF_ASCII(s):
	
	# Declaring all ascii as a Dictionary and having values=0
	ascii_char = {}
	x = ''.join([chr(i) for i in range(128)])

	for c in x:
		ascii_char[c] = 0
	
	# Interating over the entire text and incrementing the corresponding ascii_char only
	for v in s:
		ascii_char[v.lower()] += 1
	
	# Total no.of ascii_char detected		
	total_ascii_char = sum(ascii_char.values())
	
	# Calculating the fraction of each ascii_char in all the ascii_char
	for key in ascii_char:
		ascii_char[key] = ascii_char[key] /total_ascii_char
	
	# Returning the Dictionary
	return ascii_char

# Reading the Input text file
with open('file2.txt', 'r') as file:
	data = file.read().replace('\n', '')
	
# Printing the Dictionary containing data of ascii_char in text file in seperate lines.
alpha = PMF_ASCII(data)
pprint (alpha)


# Ploting Histogram for all ascii_char
plt_ = sns.barplot(list(alpha.keys()), list(alpha.values()))
plt_.set_xticklabels(plt_.get_xticklabels(), rotation=90)
plt.show() 
