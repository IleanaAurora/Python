import random
from math import log2

sequenceLength = 100000
sequence = []
charCount = 0
binCount = [0,0]
#array2 = [0,1]
#array3 = [00,01,10,11]
#array4 = [000,001,010,011,100,101,110,111]
#array5 = [0000,0100,1000,1100,0001,0101,1001,1101,0010,0110,1010,1110,0011,0111,1011,1111]
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

dict1 = dict.fromkeys(list1, 0)
dict2 = dict.fromkeys(list2, 0)
dict3 = dict.fromkeys(list3, 0)
dict4 = dict.fromkeys(list4, 0)
dict5 = dict.fromkeys(list5, 0)
dict6 = dict.fromkeys(list6, 0)
dict7 = dict.fromkeys(list7, 0)
dict8 = dict.fromkeys(list8, 0)
dict9 = dict.fromkeys(list9, 0)

for _ in range(sequenceLength):
    k = random.randint(0, 1) # decide on a k each time the loop runs
    #print(k)
    sequence.append(k)
    charCount += 1

#for i in range(0,sequenceLength, 4):
    #end = start + 11
    #print(sequence[i])
 #   print("\n")

# Python program to convert a list of character 
def convert(s): 
    # initialization of string to "" 
    new = "" 
    # traverse in the string  
    for x in s: 
        new += str(x)  
    # return string  
    return new

def divide_chunks(list, n): 
    # looping till length l 
    for i in range(0, len(list), n):
        vals = list[i:i + n]
        if len(vals) != n:
            #print("Not long enough")
            needed = n - len(vals)
            #print(type(vals))
            vals+='0'*needed
        #print(len(vals), vals)
        yield vals

def tallyVals(dict):
    for k in range(len(divided_list)):
        for key, value in dict.items():
            #print(divided_list[k], key)
            if divided_list[k] == key:
                dict[key] += 1
    #print(dict)
  
# How many elements each list should have 
#n = 2
#your_list = '010101010'
#sequenceString = convert(sequence)
#divided_list = list(divide_chunks(sequenceString, n)) 
#print(divided_list)

n=1
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=1 is:",divided_list)
tallyVals(dict1)

n=2
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=2 is:",divided_list)
tallyVals(dict2)

n=3
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=3 is:",divided_list)
tallyVals(dict3)

n=4
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=4 is:",divided_list)
tallyVals(dict4)

n=5
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=5 is:",divided_list)
tallyVals(dict5)

n=6
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=6 is:",divided_list)
tallyVals(dict6)

n=7
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=7 is:",divided_list)
tallyVals(dict7)

n=8
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=8 is:",divided_list)
tallyVals(dict8)

n=9
sequenceString = convert(sequence)
divided_list = list(divide_chunks(sequenceString, n)) 
#print("The divided list when n=9 is:",divided_list)
tallyVals(dict9)

def getEntropy(probabilities):
    entropy = 0
    for n in range(len(probabilities)):
        #print(probabilities[n])
        #print("N is ",n,"and the probability is ",probabilities[n])
        if probabilities[n] != 0:
            entropy += (probabilities[n] * log2(probabilities[n]))
        else:
            entropy += 0
    entropy = -entropy
    return entropy
        
print("The sequence is: ",sequence)
#print(dict1)
#for i in dict1:
#    print(dict1[i])
    
#probabilities[0] = dict1['0']/charCount
#probabilities[1] = dict1['1']/charCount
#print(probabilities)
#entropy = getEntropy(probabilities)
#print("The entropy of H(M,N=1) is", entropy)
#print("The entropy of H(M,N=2) is", entropy)

def calculateProbabilities(dict):
    for key, value in dict.items():
        probabilities.append(value/charCount)
    #print("Before",probabilities)
    entropy = getEntropy(probabilities)
    probabilities.clear()
    #print("After",probabilities)
    return entropy

entropy = calculateProbabilities(dict1)
print("The entropy of H(M,N=1) is", entropy)
entropy = calculateProbabilities(dict2)
print("The entropy of H(M,N=2) is", entropy)
entropy = calculateProbabilities(dict3)
print("The entropy of H(M,N=3) is", entropy)
entropy = calculateProbabilities(dict4)
print("The entropy of H(M,N=4) is", entropy)
entropy = calculateProbabilities(dict5)
print("The entropy of H(M,N=5) is", entropy)
entropy = calculateProbabilities(dict6)
print("The entropy of H(M,N=6) is", entropy)
entropy = calculateProbabilities(dict7)
print("The entropy of H(M,N=7) is", entropy)
entropy = calculateProbabilities(dict8)
print("The entropy of H(M,N=8) is", entropy)
entropy = calculateProbabilities(dict9)
print("The entropy of H(M,N=9) is", entropy)


#https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python

