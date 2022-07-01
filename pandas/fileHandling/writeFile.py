f = open("demofile.txt","w")
f.write("I am Radhika Rajoriya working on file handling.\nthis is my very first file.")
f.write("\n I am here to test my skills over file handling")

f.close()


# f1 = open ('/home/navgurukul/Desktop/pythonClass/demofile.txt',"x")
# it will return an error b because this file already exist


f2= open("/home/navgurukul/Desktop/pythonClass/demofile.txt","a")
f2.write("\n I am again appending this text to the file")

f2.close()

file = open("/home/navgurukul/Desktop/pythonClass/demofile.txt","r")
print(file.read())
