fname = input("Enter a file name: ")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    number = line.find("0")
    usenumber = float(line[number:])
    count = float(count + 1)
    total = total + usenumber
    average = total/count
print("Average spam confidence:", average)
