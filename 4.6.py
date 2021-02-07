h = float(input("Enter Hours:"))
r = float(input("Enter Rate per hour:"))
def computepay(h,r):
    if h > 40:
       p = (40*r)+(h-40)*(r*1.5)
    else:
       p = (40*r)
    return p
print ("Pay", computepay(h,r))
