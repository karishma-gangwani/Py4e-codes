filename = open("romeo.txt","r")
reading = filename.read()

for line in reading:
    words = reading.rstrip().split()
    for element in words:
        if element in words:
            continue
        else:
            words.append(element)
#sort the words
words.sort()
#remove duplicate words
correction = list(set(words))
print(correction)
