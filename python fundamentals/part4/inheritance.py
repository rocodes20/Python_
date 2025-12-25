# reusing the attributes and functions from a parent class

class Employee:
    def __init__(self):
        self.start_time = "9am"
        self.end_time = "5pm"
class Teacher(Employee):
    def __init__(self,subject):
        super().__init__()
        self.subject = subject
t1 = Teacher("maths")

print(t1.start_time,t1.subject)