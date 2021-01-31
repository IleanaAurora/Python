fr = open("sherlock.txt", "r")
fw = open("SingleSubstitutedFile.txt", "w")

key = {'a':'h','b':'r','c':'q','d':'c','e':'b','f':'k','g':'m','h':'g','i':'a','j':'p','k':'z','l':'f','m':'i','n':'x','o':'v','p':'t','q':'w','r':'n','s':'d','t':'y','u':'s','v':'e','w':'o','x':'l','y':'u','z':'j'}

for line in fr:  
       for ch in line:
              ch = ch.lower()
              for letter, encrypted in key.items():
                     if ch == letter:
                            fw.write(encrypted)
                            break
fw.close()
fr.close()
