import csv
import matplotlib.pyplot as plt

fr = open("PlainTextFile.txt", "r")

columnHeaders = ['Letter', 'Frequency']
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

a = sorted(array.items(), key=lambda x: x[1])
print(a)
x, y = map(list, zip(*a))

plt.plot(x,y)
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.show()

try:
       with open('CharCountReport.csv', 'w', newline="") as csv_file:  
           writer = csv.writer(csv_file)
           writer.writerow(["Letter","Frequency"])
           for x, y in a:
              writer.writerow([x, y])
except IOError:
    print("I/O error")
