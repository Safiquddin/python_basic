# d={}
# d[100]='Safiq'
# d[200]='Shad'
# d[300]='Pyara'
# d[100]='Arhan'
# print(d[100])

# checking key is available or not
# d={100:'Arhan',200:'Shad',300:'Pyara'}
# if 200 in d:
#     print(d[200])
 
# add two data types oen as a key & other as a value   
# tuple=(100,200,300)
# list=['Arhan','Shad','Pyara']
# d={tuple:list}
# print(d)

# dict comprehension
# val,key=['abc','def','ghi'], [1,2,3]
# d={key[i]:val[i] for i in range(len(val))}
# square={x:x*x for x in range(6)}
# print(square)
# print(d)

# WAP to enter name & marks in dictionaries & print on screen
# rec={}
# n=int(input('Enter number of students'))
# i=1
# while i<=n:
#     name=input('Enter student name:')
#     marks=input('Enter student marks:')
#     rec[name]=marks
#     i=i+1
# print('Name of student','\t','% of marks')
# for x in rec:
#     # print(x,'              ','\t', rec[x])
#     print(x,'\t\t\t',rec[x])            
    
# Update dictionarie
# d={100:'safiq', 200:'pyara',300:40}
# d[100]='Arhan'
# d[300]=d[300]+1
# print(d)

# Delete dictionarie
# d={100:'safiq',200:'pyara',300:40}
# print(d)
# del d[300]
# print(d)

# Clear all element in dictionarie
# d={100:'safiq', 200:'pyara',300:40}
# d.clear()
# print(d)

# delete dict
# d={100:'safiq', 200:'pyara',300:40}
# del d
# print(d)

##------Important function of dict------
# d=dict({100:'Safiq',200:'Pyara',300:'Shad',400:'Arhan'})
# # print(d)
# # d=dict([(100,'Safiq'),(200,'Arhan'),(300,'Shad')])
# # print(d)
# d=dict(((100,'pyara'),(200,'Arhan'),(300,'Shad'),(400,'Arhan'))) # using len()
# print(d)      
# print(len(d)) # using len()
# print('key value of 100 is:',d.get(100))
# print('if 500 found then return otherwise safiq return:',d.get(500,'safiq')) # using get()
# print('deleted key:',d.pop(100)) # using pop()
# print('Deleted last element is:',d.popitem()) # using popitem()
# print('All keys in d:',d.keys()) # using keys()
# # for k in d.keys(): 
# #     print(k)
# print('All values in d:',d.values())
# print('All items in d:',d.items())
# # for k,v in d.items():
# #     print('items in d:',k,':',v)
# d1=d.copy() # using copy() for duplicate dict
# print('duplicate dict is:',d1)
# print(d.setdefault(600,'sangram')) # using setdefault() for update based on track
# print('if 200 found then print value otherwise amrut:',d.setdefault(200,'Amrut'))
# x={100:'Suuny',200:'Bunny'}
# d.update(x) # x dict added to dict d
# print(d)

#Wap to take dictionary and print sum of vlaues
# d=eval(input('Enter dictionary to sum values:'))
# s=sum(d.values())
# print('Sum',s)

#WAP to find number of vowels present inside word
# word=input('Enter any word')
# vowel={'a','e','i','o','u'}
# d={}
# for x in word:
#     if x in vowel:
#         d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,'Occured',v,'times')

# WAP to feed name & marks and result nark based on provided input name
n=int(input('Enter number of student'))
d={}
for i in range(n):
    name=input('Enter student name')
    marks=input('Enter marks of given name')
    d[name]=marks
while True:
    name=input('Enter student name to find')
    marks=d.get(name,-1)
    if marks==-1:
        print('Student not found')
    else:
        print('student',name, 'have marks is',marks)
    option=input('Do you want to find anoather name:(y|n)')
    if option=='n':
        break
print('Thanks for using Applicationn')
    