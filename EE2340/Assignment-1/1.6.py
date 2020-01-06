import seaborn as sns
import matplotlib.pyplot as plt
import string

def PMF_Alphabet(s):
	
	alphabets = {}
	for c in string.ascii_lowercase:
		alphabets[c] = 0
		
	for v in s:
		if v.isalpha():
			alphabets[v.lower()] += 1
			
	total_alphabets = sum(alphabets.values())
	
	for key in alphabets:
		alphabets[key] = alphabets[key] /total_alphabets
	
	return alphabets

with open('inputfile.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
alpha = PMF_Alphabet(data)
print (alpha)

# Ploting Histogram
plt_ = sns.barplot(list(alpha.keys()), list(alpha.values()))
plt_.set_xticklabels(plt_.get_xticklabels(), rotation=90)
plt.show()   
