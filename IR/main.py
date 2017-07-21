import os, sys

f = open("lib/pagedata1")
count = 0
folder = "lib/documents"
if not os.path.exists(folder):
    os.makedirs(folder)
for line in f:
    count += 1
    #print line.split('\t')[1] + "\n-------------------------------\n"
    docName = folder + '/' + str(count)
    doc = open(docName, 'w')
    doc.write(line.split('\t')[1])
    doc.close()
    if count == 1000:
        break
f.close()
