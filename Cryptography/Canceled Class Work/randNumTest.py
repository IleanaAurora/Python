import random
from math import log2

sequenceLength = 25000
sequence = []
charCount = 0
probabilities = []

list1 = ['{:01b}'.format(i) for i in range(2)]
list2 = ['{:02b}'.format(i) for i in range(4)]
list3 = ['{:03b}'.format(i) for i in range(8)]
list4 = ['{:04b}'.format(i) for i in range(16)]
list5 = ['{:05b}'.format(i) for i in range(32)]
list6 = ['{:06b}'.format(i) for i in range(64)]
list7 = ['{:07b}'.format(i) for i in range(128)]
list8 = ['{:08b}'.format(i) for i in range(256)]
list9 = ['{:09b}'.format(i) for i in range(516)]
list10 = ['{:010b}'.format(i) for i in range(1024)]
list15 = ['{:015b}'.format(i) for i in range(32768)]

dict1 = dict.fromkeys(list1, 0)
dict2 = dict.fromkeys(list2, 0)
dict3 = dict.fromkeys(list3, 0)
dict4 = dict.fromkeys(list4, 0)
dict5 = dict.fromkeys(list5, 0)
dict6 = dict.fromkeys(list6, 0)
dict7 = dict.fromkeys(list7, 0)
dict8 = dict.fromkeys(list8, 0)
dict9 = dict.fromkeys(list9, 0)
dict10 = dict.fromkeys(list10, 0)
dict15 = dict.fromkeys(list15, 0)

for _ in range(sequenceLength):
    k = random.randint(0, 1) # decide on a k each time the loop runs
    sequence.append(k)
    charCount += 1

# Python program to convert to a list of characters 
def convert(s):
    new = ""  
    for x in s: 
        new += str(x) 
    return new

def divide_chunks(list, n):
    for i in range(0, len(list), n):
        vals = list[i:i + n]
        if len(vals) != n:
            needed = n - len(vals)
            vals+='0'*needed
        yield vals

def tallyVals(dict):
    for k in range(len(divided_list)):
        for key, value in dict.items():
            if divided_list[k] == key:
                dict[key] += 1

n=1
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict1)

n=2
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict2)

n=3
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict3)

n=4
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict4)

n=5
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict5)

n=6
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict6)

n=7
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict7)

n=8
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict8)

n=9
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict9)

n=10
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict10)

n=15
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n))
tallyVals(dict15)

def getEntropy(probabilities):
    entropy = 0
    for n in range(len(probabilities)):
        if probabilities[n] != 0:
            entropy += (probabilities[n] * log2(probabilities[n]))
        else:
            entropy += 0
    entropy = -entropy
    return entropy
        
#print("The sequence is: ",sequence)

def calculateProbabilities(dict,size):
    for key, value in dict.items():
        probabilities.append(size * value/charCount)
    entropy = getEntropy(probabilities)
    probabilities.clear()
    return entropy

entropy = calculateProbabilities(dict1,1)
print("The entropy of H(M,N=1) is", entropy)
entropy = calculateProbabilities(dict2,2)
print("The entropy of H(M,N=2) is", entropy)
entropy = calculateProbabilities(dict3,3)
print("The entropy of H(M,N=3) is", entropy)
entropy = calculateProbabilities(dict4,4)
print("The entropy of H(M,N=4) is", entropy)
entropy = calculateProbabilities(dict5,5)
print("The entropy of H(M,N=5) is", entropy)
entropy = calculateProbabilities(dict6,6)
print("The entropy of H(M,N=6) is", entropy)
entropy = calculateProbabilities(dict7,7)
print("The entropy of H(M,N=7) is", entropy)
entropy = calculateProbabilities(dict8,8)
print("The entropy of H(M,N=8) is", entropy)
entropy = calculateProbabilities(dict9,9)
print("The entropy of H(M,N=9) is", entropy)
entropy = calculateProbabilities(dict10,10)
print("The entropy of H(M,N=10) is", entropy)
entropy = calculateProbabilities(dict15,15)
print("The entropy of H(M,N=15) is", entropy)
