filename = open("mbox-short.txt","r")
count = dict()
lst = list()
for line in filename:
    if line.startswith("From "):
        line = line.split()
        time = line[5]
        hours = time[:2]
        count[hours] = count.get(hours,0) + 1

for key, value in count.items():
    lst.append((key,value))
lst.sort()

for hour, count in lst:
    print(hour,count)
