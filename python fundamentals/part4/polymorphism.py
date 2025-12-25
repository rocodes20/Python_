#polymorphism -> many forms
#function overriding
class Employee:
    def get_designation(self):
        print("Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Teacher")

t1 = Teacher()
t1.get_designation()

#duck typing same like function overriding but does not have any relation within them both cls are independent
#yet the fucntion does the same job
#walk like duck & quack like duck -> duck