# s=input('Enter string:')
# print("character at even position:",s[0::2])
# print("charcater at odd position",s[1::2])

# reverse string
# s=input("Enter string")
# print(s[::-1])
# print(''.join(reversed(s))) # other method
# other method
# i=len(s)-1
# output=''
# for i in range(len(s)-1,-1,-1):
#     output=output+s[i]
#     i=i-1
# print(output)

# reverse of words
# s=input("Enter string:")
# l=s.split()
#  l1=[]
#  i=len(l)-1
#  while i>=0:
#      l1.append(l[i])
#      i=i-1
#  output=' '.join(l1)
# print(output)
# print(' '.join(reversed(l)))

# reverse internal content of words
# s=input("Enter string:") # or with comma
# l=s.split(',')
# l1=[]
# i=len(l)-1
# while i>=0:
#      l1.append(l[i][::-1])
#      i=i-1
# output=','.join(l1)
# print(output)
# print(' '.join(reversed(l)))
# other method -------------
# s=input("Enter string:") # or with comma
# l=s.split(',')
# l1=[]
# for x in l:
#     l1.append(x[::-1])
# output=','.join(l1)
# print(output)
# print(' '.join(reversed(l1))) # or

# find even & odd position in string
# s=input("Enter string:")
# print("character at even position",s[0::2])
# print("character at odd postion",s[1::2])
# -------or--------
# s=input("Enter string:")
# i=0
# print("character at even posion")
# while i<len(s):
#     print(s[i],end=',')
#     i+=2
# print()
# i=1
# print("character at odd posion")
# while i<len(s):
#     print(s[i],end=',')
#     i+=2

# merge character of two string into single string
# s1=input("Enter string1:")
# s2=input("Enter string2:")
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#     i=i+1
#     if j<len(s2):
#         output=output+s2[j]
#     j=j+1
# print(output)

#sort the character & number in string
#------------------------------------
# s=input("Enter alnum string1:")
# s1=s2=output=''
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# # for x in sorted(s1):
# #     output=output+x
# # for x in sorted(s2):
# #     output=output+x
# # print(output)
# print(''.join(sorted(s1))+''.join(sorted(s2)))

#String with number of counts
# s=input("Enter alnum string1:")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output+previous*(int(x)-1)
# print(output)

#String with next following sequence character
# s=input("Enter alnum string:")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output+chr(ord(previous)+int(x))
# print(output)

#String with no repeatation
# s=input("Enter Repeatation letter string:")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# print(l)
# output=''.join(l)
# print(output)

#Find no. of occurance in string
s=input("Enter alnum string:")
d={}
for x in s:
    if x in d.keys:
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print('{}={} times'.format(k,v))

