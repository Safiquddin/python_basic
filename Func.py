# def wish():
#     print("Hello Good Morning")
# wish()

# def wish(name):
#     print('Hello',name,'Good Morning')
# wish('Safiq')

# def squareit(number):
#     print('The sqaure of ',number,'number is',number*number)
# squareit(4)

# Return statement
# def add(x,y):
#     return x+y
# x=int(input('Enter First Number'))
# y=int(input('Enter Second Number'))
# result=add(x,y)
# print('The sum is',result)
# print('The sum of return is',add(4,7)) # or

# def even_odd(x):
#     if x%2==0:
#         print(x,'is even number')
#     else:
#         print(x,'is odd number')
# even_odd(10)

## factorial of number
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result
# # for i in range(1,11):
# #     print('The factorial of',i,'is:',fact(i))
# print(fact(6))

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=sum_sub(100,40) # result in tuple
# print('The sum',x)
# print('The substraction',y)

# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div     
# print(calc(100,50))

## Types of actual arguments
# def sub(a,b):
#     print(a-b)
# sub(100,200) # Positional Arguments
# sub(a=200,b=100) # keyword arguments
# def wish(name='Guest'): # Defualt argument
#     print('Hello',name,'good evening')
# wish('Safiq')   
# wish()

## Variable Length Arguments
# def m1(*n): # Variable length argument
#     total=0
#     for n1 in n:
#         total=total+n1
#         print('The sum is:',total)   
# m1()
# m1(10)
# m1(10,20)
# def f1(x,*n):
#     print('Normal argument',x)
#     print('Variable arguments are')
#     for n1 in n:
#         print(n1)
# f1(10,20,30,40,50) # Normal argument is 10 and rest are variable arguments

# def f1(**kwargs): # Dictionary variable arguments  
#     for k,v in kwargs.items():
#         print(k,'=',v)
# f1(x=10,y=20,z=40)
# f1(name='Durga',sub1='java',mark=50)

# Rule for Function parameter are
# Positional Args,Var-arg,Default args

# variables in Function
# a=10 # Global variable
# def f1():
#     # global a # Global keyword
#     a=777 # Local variable
#     print('Local variable is',a)
#     print('declare global variable is',globals()['a'])
# def f2():
#     print('local variable',a) # if not use global keyword
# f1()
# f2()

# def wish(name):
#     print('hello',name,'Good Evening')
# greet=wish
# wish('safiq')
# greet('Shad')
# print(id(wish),id(greet))
    
s='Safiquddin khan'
print(len(s))