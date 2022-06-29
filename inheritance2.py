class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    
    def printname(self):
        print(self.firstname, self.lastname)

# create object by using person class

x= person("Ram", "Raj")
x.printname()