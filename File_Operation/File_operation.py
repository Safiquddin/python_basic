#   1. write a python program to read an entire text file
file = open('sample.txt', 'r')
for each in file:
    print(each)

#########--------OR-------#######
file1 = open('sample.txt', 'r')                   
print(file1.read())

#########--------OR-------#######
with open('sample.txt') as f:
    for line in f:
        print(line)



#   2. write a python program to read first n character of a file and where n is from user
file2 = open('sample.txt', 'r')
n = int(input("Please Enter a number of Character : "))
for i in range(n):
    char = file2.read(n)
    print(char)


#   3. write a python program to apend text to a file and display a text
File3 = open("sample1.txt", 'a')
File3.write("\nI am Linesh.")
File3.write("\nI have an total 3.8 years of experiance in cloud technology.")
File3.write("\nRelevent experiance in AWS 3.8 years.")
Text = open("sample1.txt")
print(Text.read())

#   4. write a python program to read first 3 lines of a file
file4 = open('sample.txt', 'r')
num = int(input("Please Enter a number of Line : "))
for i in range(num):
    line = file4.readline()
    print(line)

#   5. write a python program to read a file line and store it into a string and Display it
#   6. write a python program to read a file line by line and store it into a list.
#   7. write a python program to find longest word
def longestword(filename):
	with open(filename,'r+') as f:
		words = f.read().split()
		max_len_word = max(words,key=len)
		max_len = len(max(words,key=len))		
		print('maximum lenth word in file :',max_len_word)
		print('lenth is : ',max_len)

longestword('sample.txt')

#   8. write a python program to copy the contents of a file to another file