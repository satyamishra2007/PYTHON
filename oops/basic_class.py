class student:
    schoolName = 'Govt ss'  # class varaible

    def __init__(self, name, age, rollno):
        self.name = name  # Instance Variable
        self.age = age
        self.rollno = rollno

    # __str__ and __repr__ method in python

    #     def __repr__(self):
    #         print("representation  method in python")
    #         #return [self.name,self.age]
    #         return "repr : returns string"
    #         #return {'name':self.name, 'age':self.age}

    #     def __str__(self):
    #         print("To string  method in python")
    #         #return [self.name,self.age]
    #         return 'Person(name='+self.name+', age='+str(self.age)+ ')'

    # The getter's and setters  for Instance Variable
    def setName(self, nm):
        self.name = nm

    def setAge(self, ag):
        self.Age = ag

    def setRollno(self, rno):
        self.rollno = rno

    def setMarks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getTotalMarks(self):
        total = 0
        total = self.m1 + self.m2 + self.m3
        return total

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getRollno(self):
        return self.rollno

    # Static Method

    @staticmethod
    def greetings():
        return "Hi All, Welcom"

    @classmethod
    def updateSchoolName(cls, name):  # expect cls keyword
        student.schoolName = name


if __name__ == "__main__":
    s1 = student("satya", 30, 123)

# print(s1)
# print(s1.__str__())      # String representation of object .Only returns string type
# print(s1.__repr__())     # Return type can be anything may be dict,tuple,list or string

"""
Difference between __str__ and __repr__ functions
__str__ must return string object whereas __repr__ can return any python expression.
If __str__ implementation is missing then __repr__ function is used as fallback. 
There is no fallback if __repr__ function implementation is missing.
If __repr__ function is returning String representation of the object, 
we can skip implementation of __str__ function.
"""

s1.rollno = 156  # Modifying the instance variable
s1.setMarks(50, 50, 50)
print(student.greetings(), s1.getName(), s1.getAge(), s1.getRollno(), s1.schoolName, s1.getTotalMarks())

s2 = student('swati', 26, 143)
student.updateSchoolName('KV')
# student.schoolName = 'KV'
s2.setMarks(40, 40, 40)
print(student.greetings(), s2.getName(), s2.getAge(), s2.getRollno(), s2.schoolName, s2.getTotalMarks())


