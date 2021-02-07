hrs = input("Enter Hours:")
h = float(hrs)
hrte = input("hourly rate:")
r = float(hrte)
#standard hours stdh
stdh = 40
if h > 40 :
    print ("Pay:", (stdh*r)+(h-stdh)*(r*1.5))
else :
    print ("Pay:", (stdh*r))
