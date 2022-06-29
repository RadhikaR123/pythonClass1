

obj1=open("exersice.txt","r")
count=0
str1=" "

# by looping through the file, we can read the whole file line by line....
while str1:
    str1=obj1.readline()
    print(str1)
    count=count+1
print(count-1)

# obj1.close()

print(obj1.readline())          #it prints only first line of file

print(obj1.read())

# if we want to read only a few character, then use

print(obj1.read(5))


obj1.close()