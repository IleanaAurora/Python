import math

fr = open("sherlock.txt", "r")
fw = open("sherlockTextEntropy.txt", "w")

array = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
charCount = 0

for line in fr:  
       for ch in line:
              charCount += 1
              ch = ch.lower()
              for letter, count in array.items():
                     if ch == letter:
                            array[letter] += 1
                            break

fr.close()

for key, value in array.items():
    array[key] = value/charCount

entropy = 0.0
for key, value in array.items():
    if array[key] != 0:
           entropy -= array[key] * math.log2(array[key])

e = str(entropy)
c = str(charCount)

fw.write("The single letter entropy of the file is "+e+" for "+c+" total characters.")

fw.close()
