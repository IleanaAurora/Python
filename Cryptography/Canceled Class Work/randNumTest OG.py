import random
from math import log2

sequence = []
charCount = 0
binCount = [0,0]
#array2 = [0,1]
#array3 = [00,01,10,11]
#array4 = [000,001,010,011,100,101,110,111]
#array5 = [0000,0100,1000,1100,0001,0101,1001,1101,0010,0110,1010,1110,0011,0111,1011,1111]
probabilities = [0,0]

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

for _ in range(100):
    k = random.randint(0, 1) # decide on a k each time the loop runs
    #print(k)
    sequence.append(k)
    charCount += 1
    if k == 0:
        dict1['0'] += 1
    elif k == 1:
        dict1['1'] += 1

def getEntropy(probabilities):
    entropy = 0
    for n in range(len(probabilities)):
        #print(probabilities[n])
        entropy += (probabilities[n] * log2(probabilities[n]))
    entropy = -entropy
    return entropy
        
print("The sequence is: ",sequence)
#print(dict1)
probabilities[0] = dict1['0']/charCount
probabilities[1] = dict1['1']/charCount
#print(probabilities)
entropy = getEntropy(probabilities)
print("The entropy of H(M,N=1) is", entropy)


#https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python

