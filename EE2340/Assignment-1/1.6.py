import seaborn as sns
import matplotlib.pyplot as plt
import string
from pprint import pprint

def PMF_Alphabet(s):
	
	# Declaring all small alphabets as a Dictionary and having values=0
	alphabets = {}
	for c in string.ascii_lowercase:
		alphabets[c] = 0
	
	# Interating over the entire text and incrementing the corresponding alphabet only
	for v in s:
		if v.isalpha():
			alphabets[v.lower()] += 1
	
	# Total no.of alphabets detected		
	total_alphabets = sum(alphabets.values())
	
	# Calculating the fraction of each alphabet in all the alphabets
	for key in alphabets:
		alphabets[key] = alphabets[key] /total_alphabets
	
	# Returning the Dictionary
	return alphabets

# Reading the Input text file
with open('inputfile.txt', 'r') as file:
	data = file.read().replace('\n', '')
	
# Printing the Dictionary containing data of Alphabets in text file in seperate lines.
alpha = PMF_Alphabet(data)
pprint (alpha)

# Ploting Histogram for all Alphabets
plt_ = sns.barplot(list(alpha.keys()), list(alpha.values()))
plt_.set_xticklabels(plt_.get_xticklabels(), rotation=90)
plt.show()   
