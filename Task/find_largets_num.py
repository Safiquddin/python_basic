x = int(input("Enter x vaule : "))
y = int(input("Enter y value : "))
z = int(input("Enter z value : "))
if (x >= y) and (x >= z):
   largest = x
elif (y >= x) and (y >= z):
   largest = y
else:
   largest = z
print("The largest number is = ", largest)