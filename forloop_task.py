# print 1st 100 Num
First_number = int(input("Enter the 1st Number : "))
for num in range (First_number, 100+First_number+1):
    print("{0}".format(num))

# print max even Number
max = int(input("Enter the Maximum Value : "))
for number in range(2, max, 2):
    print("{0}".format(number))

# Print table
num = int(input(" Enter the number : "))        
print("Multiplication Table of : ")  
for i in range(1,11):    
   print(num,'x',i,'=',num*i)  


#print reverse even Number
N = int(input("Enter the Maximum Value : "))
for number in range(N, 2 , -2):
    print((number))