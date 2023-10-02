s=input("Enetr Some string")
# i=0
# for x in s:
#     print("The character at +ve index {} and -ve index {} is {}".format(i,i-len(s),x))
#     i+=1
s=s[::1]

s=s[5:-2:-1]
print(s)