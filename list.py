#List! -> heterogenious, mixed data types 
#Array -> homogenious data type, data of same type

#How to declare list empy
my_first_list = []

#List with values 
my_list_with_values = [2,6,3,6]
print (my_list_with_values)

#List with diff data types 
my_list_with_diff_data_types = [4,True,"Aditya",9.4]
print (my_list_with_diff_data_types)

#Indexing
second_list = ['r','t','a','z','w','p']
print ("The first character is:", second_list[0])
print (second_list[:-1])

#Nested list, list in list
nested_list = ["Aditya", [26,7], True]
print (nested_list[0][1])

#Negative Indices
negativeIndices = ['r','t','a']
print(negativeIndices[-2])

#Appending Lists
my_list = [2,4,6,7]
my_list.append(7)
print(my_list)
my_list.extend([8,3,9])
print(my_list)
my_list.sort()
print (my_list)
my_list.reverse()
print (my_list)

#delete/remove List

del_list = ['d','t','u','i','a','o']
del del_list[2]
print (del_list)
#remove multiple items
del del_list[1:3]
print (del_list)

length_list = [2,4,5,7,8,5]
print (len(length_list))


# l=eval(input("Enter list: "))
# print(l)
# l=list(input("Enter list:"))
# print(l)
# s=input("Enter list: ")
# l=s.split(',')
# print(l[1])

# nested list
# n=[0,1,2,3,4,[5,6,7]]
# n[0]=[34,54,76]
# print(n[5][2])
# print(n)

#traverse elements
# l=[2,3,4,5,6,7]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# l=[2,3,2,4,5,6,3,3,7]
# i=0
# for i in range(len(l)):
#     print("{} is available at +ve index is {} and -ve index is {}".format(l[i],i,i-len(l)))
# print(l.index(3))
# print(l.count(2))

# find element in list
# l=[2,3,2,4,5,6,3,3,7]
# n=int(input("Enter number to search in index"))
# if n in l:
#     print(n,"present at index {}".format(l.index(n)))
# else:
#     print("number not present")

#Put element in list divided by 10 with append
# l=[]
# for i in range(100):
#     if i%10==0:
#         l.append(i)
# print(l)

# insert element in list in perticular index
# l=[1,2,3,4,5,6,7]
# l.insert(2,[9,10])
# print(l) # [1,10,3,4,5,6,7]
# l.insert(10,40)
# l.insert(-9,60)
# print(l)

#add elements of one list to anoather list using extend
# l1=['fish','chicken','mutton']
# l2=[100,200,300]
# l1.extend(l2)
# print(l1)
# print(l2)

# To remove specified item in the list
# l=[10,20,30,40]
# l.remove(10)
# print(l)

#To remove & returned last element
# l=[10,20,30,40]
# print(l.pop())
# print(l.pop())
# print(l)

#remove element from specified index
# l=[10,20,30,40]
# print(l.pop(1))
#-------------------------

#Order elements from list
# l=[10,50,30,40]
# s=['cat','dog','lion','rat','tigers']
# s.sort()
# print(s)# descending order
# l.reverse()
# print(l)
# l.sort()
# print(l)# ascending order
# l.sort(reverse=True) # reverse of sort
# print(l)