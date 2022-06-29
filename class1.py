class student:
    def __init__(self, Name, Marks):
        self.name=Name
        self.marks=Marks
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
            # sadf

stu1 = student("harry", 50)
stu2 = student("ram", 30)
print(stu1.name, stu1.check_pass_fail())
print(stu2.name, stu2.check_pass_fail())