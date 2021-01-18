class student:
    schoolName = "KV"
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self,nm):
        self.name = nm

    def setAge(self,ag):
        self.age = ag

    #@classmethod
    def setSchoolName(self,schlnm):
        schoolName = schlnm

    @staticmethod
    def myStaticHello():
        print("HELLO WORLD")



if __name__  == "__main__":
    print(student.myStaticHello())
    s1 = student("satya",31)
    s2 = student("swati",28)
    print(s1.getName(),s1.getAge())
    s1.setName("sat")
    print(s1.getName(),s1.getAge())
    print(s2.setSchoolName("DAV"))
    print(s2.getName(), s2.getAge(),s2.schoolName)

