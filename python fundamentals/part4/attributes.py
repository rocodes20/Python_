class Student:
    college = "Abc College" # class attribute

    def __init__(self,name,gpa):
        self.name = name # instance attribute
        self.gpa = gpa

stu1 = Student("Rohit",8.04)
print(stu1.name,stu1.gpa,stu1.college)
