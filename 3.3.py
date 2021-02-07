score = input("Enter Score:")
points = float(score)
#range of score should be between 0 and 1
if points>= 0.9:
        print ("A")
elif points>= 0.8:
        print ("B")
elif points>= 0.7:
        print ("C")
elif points>= 0.6:
        print("D")
else :
        print ("F")
if points>1.0:
        print ("Error")
        exit()
if points<0.0:
        print ("Error")
        exit()
