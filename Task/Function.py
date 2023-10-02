#add two numbers 
A = int(input('Enter first number: '))
B = int(input('Enter second number: '))
def sum(x,y):
    return x+y

print(sum(A,B))

#Write a function to print the table of 2 and 4. taking the input from user.
def print_table(num):
     for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
n = int(input("Please Enter a number : "))
print_table(n)

#Write a function to sort the element in the list.


element_list = [1,2,3,4,7,0,5,6]
def element(num):
    return element(num)
element_list.sort(reverse=True)
print(element_list)

#. Write a function to sum all the number in a list.
sum = 0
list = [3,4,5,6,7,8,9]
for element in range (0, len(list)):
    sum = sum + list[element]
    print("Sum of all elements in given list: ", sum)

