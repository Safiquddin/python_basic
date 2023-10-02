# Aliasing & Cloaning
# x=[10,20,30,40]
# y=x #aliasing
# y[2]=555
# print(id(x))
# print(id(y))
# print(x)
# z=x.copy() # cloaning using copy()
# x[2]=777
# print(id(z)) 
# print(z)
# s=x[:] # cloaning using slice operator
# s[1]=888
# print(s)
# print(id(s))

#Matchmatical Operator
# x=[10,20,30,40]
# y=x+[50]
# z=x+y #preferable over extend() for concatenation i.e x.extend(y)
# z=2*x # repetation operator
# print(y)
# print(z)

#Comparing Operator
# x=['Safiq','Pyara','Shad']
# y=['Safiq','Pyara','Shad']
# z=['Pyara','Shad','Safiq']
# print(x==y)
# print(x==z)#order not maintained
# print(y>z) #only first element will compare

#Comparing element using numbers
# x=[10,20,30,40]
# y=[50]
# print(x<y) #only first element will compare

#Membership Operator
# x=[10,20,30,40]
# print(10 in x)
# print(50 not in x)

#Remove all elements in list
# x=[10,20,30,40,50,60]
# x.clear()
# print(x)

#Nested List
# x=[10,20,30,[40,50,60]]
# print(x[3])
# print(x[3][1])

# Nested list as matrix
# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# print("Row Wise: ")
# for n in x:
#     print(n)
# print('Element in Matrix wise:')
# for i in x:
#     for j in i:
#         print(j,end=' ')
#     print()

#List Comprehensions
# s=[x*x for x in range(11)]
# print(s)
# m=[x for x in s if x%2==0]
# print(m)

# words=['Safiq','Pyara','Shad']
# y=[x[0] for x in words]
# print(y)

# n1=[10,20,30,40]
# n2=[50,40,30,40]
# n3=[x for x in n1 if x not in n2]
# print(n3)
# n4=[y for y in n1 if y in n2]
# print(n4)

#Program to upper all word in string
# word=input('Enter Sentence:').split()
# print(word)
# u=[[w.upper(),len(w)] for w in word]
# print(u)

#Program to display vowels in given string
# v="aeiou"
# str=input('Enter Word to search for vowel:')
# print(str)
# vowel=[i for i in str if i in v]
# print("Length of Vowel",len(vowel))
# print(vowel)

#______________or _______________
# vowels=['a','e','i','o','u']
# word=input('Enter word for vowel search: ')
# found=[]
# for x in word:
#     if x in vowels:
#         if x not in found:
#             found.append(x)
# print(found)
# print('The number of vowel in given word is',len(found))
