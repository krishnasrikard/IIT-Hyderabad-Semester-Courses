# Importing Libraries
import numpy as np
import os
import struct
from bitstring import BitArray

# File Operations
def Bitstring2Bytes(s):
    """
    Converts BitString to Bytes
    """
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])
    
def SaveCompressedFile(bitstring, FileName):
    """
    Save BitString. Here BitString denotes Compressed file
    """
    ByteSequence = Bitstring2Bytes(bitstring)
    with open(FileName, "wb") as f:
        f.write(ByteSequence)
        
def ReadCompressed(FileName):
    """
    Read a compressed file to BitString
    """
    Bitstring = ""
    with open(FileName, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            Bitstring += (BitArray(byte).bin)
            byte = f.read(1)
    
    return Bitstring

def FileSize(File):
    """
    Prints File Size
    """
    return os.path.getsize(File)
    
    
# Mathematical Operations
def EstimatePMF(s):
    """
    Estimates PMF of Characters in String
    """
    Data = []
    for char in s:
        Data.append(char)

    Data = np.array(Data)
    UniqueChars, Freq = np.unique(Data, return_counts=True)
    PMF = Freq/Data.shape[0]
    CharProb = {k:v for k,v in zip(UniqueChars, PMF)}
    #CharFreq = {k:v for k,v in zip(UniqueChars, Freq)}
    return CharProb, Data
    
def CalculateEntropy(PMF):
    """
    Calculates Entropy of given Probabilities
    """
    PMF = np.array(PMF)
    log2p = -np.log2(PMF)
    return np.dot(PMF.T,log2p)
    

# Shannon Code
class ShannonCode():
    def __init__(self):
        """
        Header Info
        """
        # PMF of Alphabets
        self.PMF = None
        # No.of appended bits
        self.p = 0
        
    def Append(self, s):
        """
        Appends 0's at the end to make it a multiple of 8
        """
        if len(s) % 8 == 0:
            return s
        else:
            n = len(s) % 8
            self.p = 8-n
            s = s + "0"*(8-n)
            return s
        
    def FileParameters(self, File, CompressedFile):
        """
        Prints all File Parameters
        """
        print ("File-Details:")
        print ("-"*50)
        print ("File-Size of Original-File:", FileSize(File), "bytes")
        print ('Alphabets:', self.Alphabets)
        print ("PMF:", self.PMF)
        print ("Entropy:", self.H)
        print ("Lengths:", self.Lengths)
        print ("Expected-Length:", self.El)
        print ("H(X) <= E(l) <= H(X) + 1 is", 0 <= self.El - self.H and self.El - self.H <=1)
        print ('Coding-Scheme:', self.CodeWords)
        print ('Length of Encoded BitString after Padding', len(self.CompressedData))
        print ("File-Size of Compressed-File:", FileSize(CompressedFile), "bytes")
        print ("-"*50)
        
        
    def Possibilites(self,s):
        """
        Generates all Possible Binary Strings
        """
        if np.any(len(s) == self.Lengths):
            self.CodePossibilities.append(s)
            
        if len(s) == max(self.Lengths):
            return
        
        self.Possibilites(s + "0")
        self.Possibilites(s + "1")
        
        
    def CodingScheme(self):
        """
        Create a Prefix-Free Shannon Coding
        """
        self.CodePossibilities = []
        self.Possibilites("")
        self.CodePossibilities = sorted(self.CodePossibilities, key=len)
        
        self.CodeWords = {}
        
        for i in range(len(self.Alphabets)):
            
            for word in self.CodePossibilities[:]: 
                if len(word) < self.Lengths[i]: 
                    self.CodePossibilities.remove(word) 
                    
            alpha = self.Alphabets[i]
            self.CodeWords[alpha] = self.CodePossibilities[0]
            
            for word in self.CodePossibilities[:]: 
                if word.startswith(self.CodeWords[alpha]): 
                    self.CodePossibilities.remove(word)
                    
        self.CodeWords2Alpha = {v: k for k, v in self.CodeWords.items()}
        
        
    def ReConstruct(self, BitString):
        """
        ReConstructs Data from BitString
        """
        Data = []
        
        Codes = np.array(list(self.CodeWords2Alpha.keys()))
        tmp = ""
        for i in range(len(BitString)):
            tmp += BitString[i]
            if np.any(tmp == Codes):
                Data.append(self.CodeWords2Alpha[tmp])
                tmp = ""
                
        return Data
    
    
    def Calculate(self,File):
        """
        Calculate Information from Original File
        """
        f = open(File, 'r')
        self.CharProb, self.Data = EstimatePMF(f.read())
        self.CharProb = dict(sorted(self.CharProb.items(), key=lambda item: -item[1]))
        
        # Alphabets
        self.Alphabets = list(self.CharProb.keys())
        
        # PMF
        self.PMF = list(self.CharProb.values())
        
        # Entropy
        self.H = CalculateEntropy(self.PMF)
        
        # Length of Code of Each Alphabet
        self.Lengths = np.ceil(-np.log2(self.PMF))
        
        # Expected Length of Output
        self.El = np.dot(self.Lengths.T, self.PMF)
        
        # Creating a Coding Scheme
        self.CodingScheme()
        
        
    def CompressFile(self,File,CompressedFileName):
        """
        Compresses the given File
        """
        
        # Calculate Information from Original File
        self.Calculate(File)
        
        # Creating Bit String
        self.CompressedData = ""
        for alpha in self.Data:
            self.CompressedData += self.CodeWords[alpha]
            
        # Appending Zeros at the End
        self.CompressedData = self.Append(self.CompressedData)
            
        # Saving Compressed File
        SaveCompressedFile(self.CompressedData, CompressedFileName)
        
        # Printing File Parameters
        self.FileParameters(File, CompressedFileName)
        
        return self.CompressedData
        
    
    def ReadCompressedFile(self,File,CompressedFileName):
        """
        Read Compressed File
        """
        
        # Calculate Information from Original File
        self.Calculate(File)
        
        # Reconstructing Compressed File
        BitString = ReadCompressed(CompressedFileName)
        BitString = BitString[:len(BitString)-self.p]
        
        # Reconstruct Data
        self.ReConstructedData = self.ReConstruct(BitString)
        
        print ("No.of Wrong Characters:", np.sum(np.array(self.ReConstructedData) != np.array(self.Data)))
        

# Huffman Code
class HuffmanCode():
    def __init__(self):
        """
        Header Info
        """
        # PMF of Alphabets
        self.PMF = None
        # No.of appended bits
        self.p = 0
        
    def Append(self, s):
        """
        Appends 0's at the end to make it a multiple of 8
        """
        if len(s) % 8 == 0:
            return s
        else:
            n = len(s) % 8
            self.p = 8-n
            s = s + "0"*(8-n)
            return s
        
    def FileParameters(self, File, CompressedFile):
        """
        Prints all File Parameters
        """
        print ("File-Details:")
        print ("-"*50)
        print ("File-Size of Original-File:", FileSize(File), "bytes")
        print ('Alphabets:', self.Alphabets)
        print ("PMF:", self.PMF)
        print ("Entropy:", self.H)
        print ("Lengths:", self.Lengths)
        print ("Expected-Length:", self.El)
        print ("H(X) <= E(l) <= H(X) + 1 is", 0 <= self.El - self.H and self.El - self.H <=1)
        print ('Coding-Scheme:', self.CodeWords)
        print ('Length of Encoded BitString after Padding', len(self.CompressedData))
        print ("File-Size of Compressed-File:", FileSize(CompressedFile), "bytes")
        print ("-"*50)
        
        
    def UnWrap(self,t,s):
        """
        Generates Binary Tree
        """
        if len(t) == 1:
            self.CodeWords[t[0]] = s
        else:
            left, right = t
            if isinstance(left,str):
                left = (left)
            if isinstance(right,str):
                right = (right)            
            self.UnWrap(left, s + '0')
            self.UnWrap(right, s + '1')
        
    def CodingScheme(self):
        """
        Create a Prefix-Free Huffman Coding
        """
        ProbChars = self.CharProb
        ProbChars = dict(sorted(ProbChars.items(), key=lambda item: item[1]))

        while len(ProbChars) != 1:
            Keys, Values = list(ProbChars.keys()), list(ProbChars.values())

            NewKey = (Keys[0] , Keys[1])
            NewValue = Values[0] + Values[1]

            Keys.pop(0), Keys.pop(0)
            Values.pop(0), Values.pop(0)

            Keys.append(NewKey)
            Values.append(NewValue)

            ProbChars = {k:v for k,v in zip(Keys,Values)}
            ProbChars = dict(sorted(ProbChars.items(), key=lambda item: item[1]))

        self.CodeWords = {}
        self.UnWrap(list(ProbChars.keys())[0],"")
        self.CodeWords = dict(sorted(self.CodeWords.items(), key=lambda item: len(item[1])))

        self.CodeWords2Alpha = {v: k for k, v in self.CodeWords.items()}
        
        
    def ReConstruct(self, BitString):
        """
        ReConstructs Data from BitString
        """
        Data = []
        
        Codes = np.array(list(self.CodeWords2Alpha.keys()))
        tmp = ""
        for i in range(len(BitString)):
            tmp += BitString[i]
            if np.any(tmp == Codes):
                Data.append(self.CodeWords2Alpha[tmp])
                tmp = ""
                
        return Data
    
    
    def Calculate(self,File):
        """
        Calculate Information from Original File
        """
        f = open(File, 'r')
        self.CharProb, self.Data = EstimatePMF(f.read())
        self.CharProb = dict(sorted(self.CharProb.items(), key=lambda item: -item[1]))
        
        # Alphabets
        self.Alphabets = list(self.CharProb.keys())
        
        # PMF
        self.PMF = list(self.CharProb.values())
        
        # Entropy
        self.H = CalculateEntropy(self.PMF)
        
        # Creating a Coding Scheme
        self.CodingScheme()
        
        # Length of Code of Each Alphabet
        self.Lengths = []
        for val in list(self.CodeWords.values()):
            self.Lengths.append(len(val))
        self.Lengths = np.array(self.Lengths)
        
        # Expected Length of Output
        self.El = np.dot(self.Lengths.T, self.PMF)
        
        
    def CompressFile(self,File,CompressedFileName):
        """
        Compresses the given File
        """
        
        # Calculate Information from Original File
        self.Calculate(File)
        
        # Creating Bit String
        self.CompressedData = ""
        for alpha in self.Data:
            self.CompressedData += self.CodeWords[alpha]
            
        # Appending Zeros at the End
        self.CompressedData = self.Append(self.CompressedData)
            
        # Saving Compressed File
        SaveCompressedFile(self.CompressedData, CompressedFileName)
        
        # Printing File Parameters
        self.FileParameters(File, CompressedFileName)
        
        return self.CompressedData
        
    
    def ReadCompressedFile(self,File,CompressedFileName):
        """
        Read Compressed File
        """
        
        # Calculate Information from Original File
        self.Calculate(File)
        
        # Reconstructing Compressed File
        BitString = ReadCompressed(CompressedFileName)
        BitString = BitString[:len(BitString)-self.p]
        
        # Reconstruct Data
        self.ReConstructedData = self.ReConstruct(BitString)
        
        print ("No.of Wrong Characters:", np.sum(np.array(self.ReConstructedData) != np.array(self.Data)))        
  
        
# Shannon-Fano-Elias Code
class SFECode():
    def __init__(self):
        """
        Header Info
        """
        # PMF of Alphabets
        self.PMF = None
        # No.of appended bits
        self.p = 0
        
    def Append(self, s):
        """
        Appends 0's at the end to make it a multiple of 8
        """
        if len(s) % 8 == 0:
            return s
        else:
            n = len(s) % 8
            self.p = 8-n
            s = s + "0"*(8-n)
            return s
        
    def FileParameters(self, File, CompressedFile):
        """
        Prints all File Parameters
        """
        print ("File-Details:")
        print ("-"*50)
        print ("File-Size of Original-File:", FileSize(File), "bytes")
        print ('Alphabets:', self.Alphabets)
        print ("PMF:", self.PMF)
        print ("Entropy:", self.H)
        print ("Lengths:", self.Lengths)
        print ("Expected-Length:", self.El)
        print ("H(X) + 1 <= E(l) <= H(X) + 2 is", 1 <= self.El - self.H and self.El - self.H <=2)
        print ("FBar(xi):", self.FBar)
        print ('Coding-Scheme:', self.CodeWords)
        print ('Length of Encoded BitString after Padding', len(self.CompressedData))
        print ("File-Size of Compressed-File:", FileSize(CompressedFile), "bytes")
        print ("-"*50)
        
        
    def Fraction2Binary(self,f,Limit):
        """
        Converts a Fraction to its Binary Representation
        """
        Binary = ""
        while len(Binary) < Limit and f > 0:
            f = f * 2
            Binary += str(int(f))
            f -= int(f)
        return Binary
            
            
    def CodingScheme(self):
        """
        Create a Prefix-Free Shannon-Falo-Elias Coding
        """
        
        self.CodeWords = {}
        self.FBar = np.zeros((len(self.PMF),))
        
        for i in range(len(self.PMF)):
            if i == 0:
                self.FBar[i] = self.PMF[i] * 0.5
            else:
                self.FBar[i] = self.FBar[i-1] + self.PMF[i-1] * 0.5 + self.PMF[i] * 0.5
                
        for i in range(len(self.Alphabets)):
            self.CodeWords[self.Alphabets[i]] = self.Fraction2Binary(self.FBar[i], self.Lengths[i])
                    
        self.CodeWords2Alpha = {v: k for k, v in self.CodeWords.items()}
        
        
    def ReConstruct(self, BitString):
        """
        ReConstructs Data from BitString
        """
        Data = []
        
        Codes = np.array(list(self.CodeWords2Alpha.keys()))
        tmp = ""
        for i in range(len(BitString)):
            tmp += BitString[i]
            if np.any(tmp == Codes):
                Data.append(self.CodeWords2Alpha[tmp])
                tmp = ""
                
        return Data
    
    
    def Calculate(self,File):
        """
        Calculate Information from Original File
        """
        f = open(File, 'r')
        self.CharProb, self.Data = EstimatePMF(f.read())
        self.CharProb = dict(sorted(self.CharProb.items(), key=lambda item: -item[1]))
        
        # Alphabets
        self.Alphabets = list(self.CharProb.keys())
        
        # PMF
        self.PMF = list(self.CharProb.values())
        
        # Entropy
        self.H = CalculateEntropy(self.PMF)
        
        # Length of Code of Each Alphabet
        self.Lengths = np.ceil(-np.log2(self.PMF)) + 1
        
        # Expected Length of Output
        self.El = np.dot(self.Lengths.T, self.PMF)
        
        # Creating a Coding Scheme
        self.CodingScheme()

    
    def CompressFile(self,File,CompressedFileName):
        """
        Compresses the given File
        """
        
        # Calculate Information from Original File
        self.Calculate(File)
        
        # Creating Bit String
        self.CompressedData = ""
        for alpha in self.Data:
            self.CompressedData += self.CodeWords[alpha]
            
        # Appending Zeros at the End
        self.CompressedData = self.Append(self.CompressedData)
            
        # Saving Compressed File
        SaveCompressedFile(self.CompressedData, CompressedFileName)
        
        # Printing File Parameters
        self.FileParameters(File, CompressedFileName)
        
        return self.CompressedData
        
    
    def ReadCompressedFile(self,File,CompressedFileName):
        """
        Read Compressed File
        """
        
        # Calculate Information from Original File
        self.Calculate(File)
        
        # Reconstructing Compressed File
        BitString = ReadCompressed(CompressedFileName)
        BitString = BitString[:len(BitString)-self.p]
        
        # Reconstruct Data
        self.ReConstructedData = self.ReConstruct(BitString)
        
        print ("No.of Wrong Characters:", np.sum(np.array(self.ReConstructedData) != np.array(self.Data)))

print ("Compressing and Reading Data using Shannon Code")
SC = ShannonCode() 
SC.CompressFile("inputfile_problem3_18.txt", "OutputFile-3c-Shannon.bin")
SC.ReadCompressedFile("inputfile_problem3_18.txt", "OutputFile-3c-Shannon.bin")
print ("\n")

print ("Compressing and Reading Data using Huffman Code")
HC = HuffmanCode()
HC.CompressFile("inputfile_problem3_18.txt", "OutputFile-3c-Huffman.bin")
HC.ReadCompressedFile("inputfile_problem3_18.txt", "OutputFile-3c-Huffman.bin")
print ("\n")

print ("Compressing and Reading Data using Shannon-Fano-Elias Code")
SFEC = SFECode()
SFEC.CompressFile("inputfile_problem3_18.txt", "OutputFile-3c-SFE.bin")
SFEC.ReadCompressedFile("inputfile_problem3_18.txt", "OutputFile-3c-SFE.bin")
