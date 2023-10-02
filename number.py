a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
max=a if a>b>c else b if b>a and b>c else c;
print("Minimum Valube",max)