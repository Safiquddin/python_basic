# Lambda funcation
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Recursive funcation
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = int(input("Please Enter a number : "))
print("The factorial of", num, "is", factorial(num))