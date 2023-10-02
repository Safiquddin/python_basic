#Tuple Data Type/Data Structure

#Tuple is same as list, list is mutable tuple is immutable.
#immutable = unchangeable
#tuples allows duplicate values
#tuples allows heterogenious daa types 

mytyuple = ("one", "two", 1, True)
print(mytyuple)

mytuple1 = ("one", "two","three","one")
print (mytuple1)


#Diff of tuples from list
#syntax
my_list = [1,2,3,4]
my_tuple = (1,2,3,4)

print (my_list)
print (my_tuple)

#mutability
my_list[2] = 10
print (my_list)  # 1,2,10,4
#my_tuple[1] = 10
print(my_tuple)


print(my_list.__sizeof__())
print(my_tuple.__sizeof__())


#List and tuples are same, the only diff is list is mutable and tuple is immutable
# both are ordered, slicing, duplicate, heterogenious

my_tuple1 = (10,)
print (my_tuple1)
print (type(my_tuple1))


# t=10,20,30,40
# tpl=10,
# print(type(t))
# print(type(tpl))

# x,y=(int(x) for x in input('Enter two numbers for sum').split())
# print(x,y) # add two numbers using single line input

# typecasting of list to tuple
# l=[10,20,30,40]
# t=tuple(l)
# print(type(t))

# Addition of two tuple as we are not changing content of tuple
# x=10,20,30,40
# y=60,70,80
# z=x+y
# t=x*3
# print(z)
# print(t)

# x=10,20,40,30
# y = sorted(x) # return List type..use sorted as immuttable instead if sort
# print(type(y))
# print(tuple(y))
# print(id(x))
# print(id(y))
# min=min(x)
# print(min)
# max=max(x)
# print(max)

#tuple packing and unpack
# a,b,c,d=10,20,30,40
# t=a,b,c,d #packing
# w,x,y,z=t # unpacking
# print(t)
# print(w,x,y,z)

# tuple comprehension (with type generator)
# t=(x**x for x in range(10))
# for e in t:
#     print(e)
# print(type(t))

# Sum of two numbers 
t=eval(input("Enter tuple numbers for sum"))
sum=0
for i in t:
    sum=sum+i
print('The sum is',sum)
print('The average is: ',sum//len(t))
