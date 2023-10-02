# s=input("Enter string")
# i=0
# n=len(s)
# print("In Forward Direction")
# while i>=n:
#     print(s[i],end=' ')
#     i=i+1
# print()

# s=input("Enter for backward string")
# i=-1
# n=len(s)
# print("In backward Direction")
# while i>=-n:
#     print(s[i],end=' ')
#     i=i-1

# s=input("Enter string")
# print("Forward Direction")
# for i in s[::]:
#     print(i,end=' ')
# print()
# print("Backward Direction")
# for i in s[::-1]:
#     print(i,end=' ')

# ------------------------------
# main=input("Enter string")
# sub=input("Enter Sub string")
# if sub in main:
#     print("sub,is avalable in main")
# else:
#     print("sub, is available in main")
# ---------------------------------
# s1=input("Enter string")
# s2=input("Enter string 2")
# if s1==s2:
#     print("both are equal")
# elif s1<s2:
#     print("s1 is less than s2")
# else:
#     print("s1 is greater than s2")

city=input("Enter city name")
scity=city.strip() #Strip,lstrip,rstrip for remove space
if scity=="khan":
    print("khan is prestn inside scity")
else:
    print("Enter valid city name")