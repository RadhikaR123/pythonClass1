class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        # self.passyear = year
    
    def printname(self):
        print(self.firstname, self.lastname)

# create object bu using person class
# asdsad

# x= person("/am", "Raj")
# x.printname()?

class student(person):
    def __init__(self, fname, lname, year):
        person.__init__(self, fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "in the year", self.graduationyear)
    
x=student("radhi", "raj", 2009)
x.welcome()
