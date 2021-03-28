# Importing Libraries
import numpy as np
import os    

# Arithmetic Coding Scheme    
class ArithmeticCode():
	def __init__(self,Alphabets, PMF, N):
		PMF = PMF/np.sum(PMF)
		
		# Alphabets and their PMF
		self.Alphabets = Alphabets		
		self.AlphabetsPMF = dict(zip(Alphabets, PMF))
		#self.AlphabetsPMF = {k: v for k, v in sorted(self.AlphabetsPMF.items(), key=lambda item: item[1])}
		
		# CDF of Alphabets
		CDF = []
		pmf = list(self.AlphabetsPMF.values())
		alphabets = list(self.AlphabetsPMF.keys())
		for i in range(len(pmf)):
			if i==0:
				CDF.append(pmf[i])
			else:
				CDF.append(CDF[-1] + pmf[i])
		self.AlphabetsCDF = dict(zip(alphabets, CDF))
		print (self.AlphabetsCDF)
		
		# Length of Sequence Computing Limit
		self.N = N
		
		# Map for Sequence to Probabilities
		self.Map_Seq2Prob = {}
		
		# Map from Sequence to G
		self.Map_Seq2G = {}
		
		# Generating Map for all Possible Sequences
		self.Map_Seq2Prob = self.AlphabetsPMF
		for alpha in self.Alphabets[::-1]:
			self.Map_Seq2G[alpha] = self.AlphabetsCDF[alpha] - self.AlphabetsPMF[alpha]
			
		self.Possibilites("")
		
		
	def Fraction2Binary(self,f,Limit):
		"""
		Converts a Fraction to its Binary Representation
		"""
		Binary = ""
		if f == 0:
			Binary += "0"
			
		while len(Binary) < Limit and f > 0:
			f = f * 2
			Binary += str(int(f))
			f -= int(f)
		
		return Binary
        	
        	
	def Map(self,S):
		"""
		Map a Sequence to its FBar and G Functions by Recursion 
		"""
		l = len(S)
		if l > 1:
			self.Map_Seq2G[S] = self.Map_Seq2G[S[:l-1]] + self.Map_Seq2Prob[S[:l-1]]*self.Map_Seq2G[S[l-1]]
			self.Map_Seq2Prob[S] = self.Map_Seq2Prob[S[:l-1]] * self.AlphabetsPMF[S[l-1]]
		
		
	def Possibilites(self,s):
		"""
		Generates all Possible Alphabet Strings for length n
		"""
		if len(s) == self.N:
			self.Map(s)
			return
		else:
			self.Map(s)
			for alpha in self.Alphabets:
				self.Possibilites(s + alpha)		
				
		
	def Encode(self, Sequence):
		"""
		Encode a Sequence
		"""
		
		n = len(Sequence)
		if n > self.N:
			self.N = n
			self.Map_Seq2Prob = {}
			self.Map_Seq2G = {}
			self.Possibilites("")
		
		CDFBar = self.Map_Seq2G[Sequence] + 0.5*self.Map_Seq2Prob[Sequence]
		l = 1 + np.ceil(-np.log2(self.Map_Seq2Prob[Sequence]))
		
		return self.Fraction2Binary(CDFBar, l)
		
		
AC = ArithmeticCode(['a','b','c'], [0.5152163969,0.3162466569,0.1685369463], 10)

S = "bacaaaaabb"
Encoded = AC.Encode(S)
print ("Encoding for " + S + ": ", Encoded)

S = "bbbcbabbaa"
Encoded = AC.Encode(S)
print ("Encoding for " + S + ": ", Encoded)
