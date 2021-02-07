filename = open("mbox-short.txt","r")
greatestcount = dict()
lst = list()
for line in filename:
    if line.startswith("From "):
        line = line.split()
        lst.append(line[1])
for word in lst:
    greatestcount[word] = greatestcount.get(word,0) + 1

bigcount = None
bigword = None
for word,count in greatestcount.items():
    if bigcount is None or count>bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
