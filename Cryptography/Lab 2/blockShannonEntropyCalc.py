import math
from math import log2
import random
import itertools

fr = open("DoubleSubstitutedFile.txt", "r")
fw1 = open("sherlockTextEntropyForBlocks.txt", "w")

array = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
options = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charCount = 0
sequence = []

#add contents of txt file to list
for line in fr:  
       for ch in line:
              charCount += 1
              ch = ch.lower()
              sequence.append(ch)

fr.close()

#divide list holding txt file into n blocks
def divide_chunks(list, n):
    for i in range(0, len(list), n):
        vals = list[i:i + n]
        if len(vals) != n:
            needed = n - len(vals)
            for x in range(0, needed):
                   vals+=random.choice(options)
        yield vals

#merge nested list into char string
def sectionList(list):
       return [''.join(x) for x in list]

#create alphabet block combinations of size n      
def createNblocks(n):
       keywords = [''.join(i) for i in itertools.product(options, repeat = n)]
       return(keywords)

#initialize set of generate alphabet combinations to 0 to keep count
def initialize(dict, keywords):
       for x in range(len(keywords)):
              dict[keywords[x]] = 0

#count alphabet combinations in txt file contents
def tallyVals(dict):
    for k in range(len(new_list)):
           for key, value in dict.items():
            if new_list[k] == key:
                dict[key] += 1

n=1
divided_list = list(divide_chunks(sequence, n))
new_list = sectionList(divided_list)
keywords = createNblocks(1)
dict1 = {}
initialize(dict1, keywords)
tallyVals(dict1)

n=2
divided_list = list(divide_chunks(sequence, n))
new_list = sectionList(divided_list)
keywords = createNblocks(2)
dict2 = {}
initialize(dict2, keywords)
tallyVals(dict2)

n=3
divided_list = list(divide_chunks(sequence, n))
new_list = sectionList(divided_list)
keywords = createNblocks(3)
dict3 = {}
initialize(dict3, keywords)
tallyVals(dict3)

n=4
divided_list = list(divide_chunks(sequence, n))
new_list = sectionList(divided_list)
keywords = createNblocks(4)
dict4 = {}
initialize(dict4, keywords)
tallyVals(dict4)

def getEntropy(probabilities):
    entropy = 0
    for n in range(len(probabilities)):
        if probabilities[n] != 0:
            entropy += (probabilities[n] * log2(probabilities[n]))
        else:
            entropy += 0
    entropy = -entropy
    return entropy

def calculateProbabilities(dict,size):
    for key, value in dict.items():
        probabilities.append(size * value/charCount)
    entropy = getEntropy(probabilities)
    probabilities.clear()
    return entropy

probabilities = []
entropy = calculateProbabilities(dict1,1)
print("The entropy of H(M,N=1) is", entropy)
fw1.write("The entropy of H(M,N=1) is " + str(entropy)+ "\n")
entropy = calculateProbabilities(dict2,2)
print("The entropy of H(M,N=2) is", entropy)
fw1.write("The entropy of H(M,N=2) is " + str(entropy)+ "\n")
entropy = calculateProbabilities(dict3,3)
print("The entropy of H(M,N=3) is", entropy)
fw1.write("The entropy of H(M,N=3) is " + str(entropy)+ "\n")
entropy = calculateProbabilities(dict4,4)
print("The entropy of H(M,N=4) is", entropy)
fw1.write("The entropy of H(M,N=4) is " + str(entropy)+ "\n")

fw1.close()
