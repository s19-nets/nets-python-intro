import sys
import re
fileName = sys.argv[1]
outName = sys.argv[2]
words = {}
file = open(fileName,'r').read()
file = re.split('\s|-|\'',file)
for word in file:
    word = word.lower()
    word = re.sub('[\.$;$,$:$]',"",word)
    if word == "":
        continue
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

outFile = open(outName,'w')
for w,k in sorted(words.items()):
    print(w ,k)
    outFile.write('%s %s\n' % (w,k))

outFile.close()






