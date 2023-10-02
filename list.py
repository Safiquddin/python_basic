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