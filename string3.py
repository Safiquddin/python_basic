# name=""

# while name!="safiq":
#     name=input("Enter name~")
# print("Thanks for confirmation")

# n=int(input("Enter number of rows:"))
# for i in range(n):
#     print(" "*(n-i),end="")
#     print("* "*i)

# for i in range(100):
#     if i%9==0:
#         print(i)
#     else:pass

# s="Learning python is easy"
# print(s.find('python'))
# print(s.find("a"))
# print(s.find("java"))
# print(s.rfind("python"))
# print(s.find('python',3,20))

# s=input("Enter some String: ")
# sub=input("Enter some substring: ")
# try:
#     n=s.index(sub)
# except ValueError:
#     print("Substring not found")
# else:
#     print(n)

s=input("Enter some String:")
sub=input("Enter some substring:")
flag=False
pos=-1
n=len(s)
count=0
print('length of string',n)
while True:
    pos=s.find(sub,pos+1,n)
    if pos==-1:
        break
    print('Found at Position',pos)
    count+=1
    flag=True
if flag==False:
    print('Not Found')
else:
    print('The number of Occurance',count)
    print('The number of occurance',s.count(sub))

# s=input("Enter some String:")
# s=s.replace('uddin', 'khan')
# list=s.split()
# print(list)
# for x in list:
#     print(x)
# print(s)

# s="19-05-1996"
# list=s.split('-')
# print(list)

# l=['safiq','shad','pyara']
# s=':'.join(l)
# print(s)

# s=''.join({'c','a','t'})
# print(s)

# s=input("Enter string")
# l=s.strip()
# print(l)

# s='learning Python is easy'
# u=s.upper()
# l=s.lower()
# swap=s.swapcase()
# t=s.title()
# c=s.capitalize()
# print(u)
# print(l)
# print(swap)
# print(t)
# print(c)

s=input('Enter character:')
if s.isalnum():
    print('Alpha numeric')
    if s.isalpha():
        print('Alpha character')
        if s.islower():
            print('Lower case character')
        else:
            print('Upper case character')
    else:
        print('it is digit')
elif s.isspace():
    print('Space character')
else:
    print('it is special character')

