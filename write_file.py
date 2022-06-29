people=open("exersice.txt","a")

people.write("sourabh-meerut")

for i in range(5):
    name=input("enter your name :")
    city=input("enter your city:")

    record=name+'-'+city
    people.write(record)
    people.write("\n")
people.close()