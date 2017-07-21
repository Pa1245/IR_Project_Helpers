f = open('lib/wikidata')
data = open('lib/wikidata.csv', 'w')
count = 0
for line in f:
    count += 1
    token = line.split('\t')
    loc = token[1].split()
    data.write(loc[0] + ',' + loc[1] + ',' + 'documents/' + token[0] + '\n')
    if count == 1000:
        break
data.close()
f.close()
