largest = None
smallest = None

while True:
    num = input("Enter a number: ").strip()
    if num == 'done':break
    try:
        ival = int(num)
    except:
        print ('Invalid input')

    if largest is None or ival>largest:
        largest = ival
    if smallest is None or ival<smallest:
        smallest = ival

print ("Maximum is", largest)
print ("Minimum is", smallest)
