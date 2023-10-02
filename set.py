from typing import Sequence


# s={10,20,30,40}
# d={}# empty curlibracket is dict
# s1=set(d) # for dict to set
# s2=set(range(10))
# print(type(s),type(d))
# print(s2)

# l=[10,20,30,10,20,30,20,10]
# s=set(l) # output with no duplicate & order
# print(s)

# Adding values to set
# s=set()
# s.add(10)
# s.add(10)
# s.add(50) # Add single element to set
# s.add((10,30,40))# can be add as a tuple but not list(due to hashable)
# # s.add([10,20,30]) #TypeError: unhashable type: 'list'
# s.update([10,20,30],(40,50,10),'Safiq',range(10)) # add iterable elements but not int,float & complex
# s.add('pyara')
# print(s)

#using copy() for clone object
# s1={10,20,30}
# s2=s1.copy()
# s1.add(40) 
# print(s2) # due to deep cloaning add 40 affected on s1

# using pop()
# s1={10,20,30,'safiq','pyara',10.5,10+20j}
# s1.pop() # remove randomly in s1
# print(s1)

#using remove() to perticular element
# s={10,20,30,'safiq','pyara',10.5,10+20j}
# s.remove(20)
# print(s)

#using discard() like remove but no error if value not present
# s={10,20,30}
# s.discard(10)
# s.discard(50) # no error in discard()
# print(s)

#using clear() to remove all elements from set
# s={10,20,30}
# s.clear()
# print(s)

#--------MATHMATICAL OPERATOR------------
# x={10,20,30,40}
# y={30,40,50,60}
# print(x|y)# using union operator
# print(x.union(y))
# print(x&y) # using Intersection operator
# print(x.intersection(y))
# print(x-y) # using difference operator
# print(x.difference(y))
# print(x^y) # using symmetric_difference operator
# print(x.symmetric_difference(y))
# print(type(x))

# Member opertor
# s=set('Safiq')
# print(s)
# print('f' in s)

# Set Comprehension
# s1={x*x for x in range(12)}
# print(s1)
# s2={2**x for x in range(2,12,2)}
# print(s2)

# write to delete duplicate element present in a list
# l=eval(input('Enetr some list value for extract duplicate element'))
# print(l)
# s=set(l)
# print(s)
#output with order & no duplicate
# l=eval(input('Enetr some list value for extract duplicate element'))
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)

#Write a program different vowels presnt in word
# l=input('Enetr some list value for extract duplicate element')
# s=set(l)
# print(s)
# vowel={'a','e','i','o','u'}
# d=s.intersection(vowel)
# # d=s&v
# print('element present provided',l,'are',sorted(d))
#------------or--------------------
# l=eval(input('Enter Some list'))
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)

#Write a program to find vowel in word with sort
# word=input('Enter some word')
# s=set(word)
# vowel={'a','e','i','o','u'}
# d=s&vowel
# print('The Difference vowels present in',word,'are',sorted(d))
         